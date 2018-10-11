from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length= 200, db_index=True)
    slug = models.SlugField(max_length= 200, db_index=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_kek', kwargs={'category_slug': self.slug})


class Brand(models.Model):

    name = models.CharField(max_length= 200, db_index=True)

    def __str__(self):
        return self.name

def image_folder(instanse, filename):
    filename= instanse.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instanse.slug, filename)



class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField()
    image = models.ImageField(upload_to= image_folder, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_kek', kwargs={'product_slug': self.slug})


class CartItem(models.Model):

    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    qty= models.PositiveIntegerField(default=1)
    item_total= models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "В корзине {0}".format(self.product.name)



class Cart(models.Model):

    items = models.ManyToManyField(CartItem,blank=True)
    basket_total= models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)


class Shop(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True, default='store_1')
    time = models.CharField(max_length=200, db_index=True, verbose_name="Время работы")
    address = models.TextField(blank=True, verbose_name="Адрес")
    shop_photo= models.ImageField(upload_to= image_folder, verbose_name="Изображение магазина")
    manager_name = models.CharField(max_length=200, db_index=True, verbose_name="Имя упр.")
    mapurl= models.TextField(blank=True, verbose_name="Скрипт карты")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop', kwargs={'shop_slug': self.slug})

ORDER_STATUS_CHOICES = (
    ('Принят в обработку', 'Принят в обработку'),
    ('Выполняется', 'Выполняется'),
    ('Оплачен', 'Оплачен')
)

class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    buying_type = models.CharField(max_length=40, choices=(('Самовывоз', 'Самовывоз'),
        ('Доставка', 'Доставка')), default='Самовывоз')
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    email = models.EmailField(default='kekvald@yandex.ru')
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0])

    def __unicode__(self):
        return "Заказ №{0}".format(str(self.id))