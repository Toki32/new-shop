# Generated by Django 2.1.2 on 2018-10-12 08:51

from django.db import migrations, models
import test_shop_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_shop_app', '0021_remove_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=0, upload_to=test_shop_app.models.image_folder, verbose_name='Изображение товара'),
        ),
    ]