# Generated by Django 2.0rc1 on 2017-12-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='products/images/'),
        ),
    ]
