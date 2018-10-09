# Generated by Django 2.1.2 on 2018-10-09 05:28

from django.db import migrations, models
import test_shop_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_shop_app', '0006_auto_20181005_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('shop_photo', models.ImageField(upload_to=test_shop_app.models.image_folder, verbose_name='Изображение магазина')),
                ('manager_name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='test_shop_app.CartItem'),
        ),
    ]
