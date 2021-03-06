# Generated by Django 2.1.2 on 2018-10-05 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('test_shop_app', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('item_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_shop_app.Product')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='items',
            field=models.ManyToManyField(to='test_shop_app.BasketItem'),
        ),
    ]
