# Generated by Django 2.1.2 on 2018-10-12 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_shop_app', '0020_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
