from django.db import models
from django.urls import reverse

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
    slug = models.SlugField(max_length=200, db_index=True)
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

