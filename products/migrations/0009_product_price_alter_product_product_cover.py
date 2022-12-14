# Generated by Django 4.1.3 on 2022-11-27 07:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_product_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_cover',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
