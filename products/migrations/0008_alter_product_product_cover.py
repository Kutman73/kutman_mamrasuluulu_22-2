# Generated by Django 4.1.3 on 2022-11-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_category_product_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
