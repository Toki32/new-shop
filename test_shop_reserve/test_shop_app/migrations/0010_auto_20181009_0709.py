# Generated by Django 2.1.2 on 2018-10-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_shop_app', '0009_auto_20181009_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='time',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Время работы'),
        ),
    ]