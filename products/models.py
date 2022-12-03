from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Категории"""
    product_categorias = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.product_categorias

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Продукт"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_cover = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.FloatField(null=True)
    categorias = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.author.username}_{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Review(models.Model):
    """Отзывы"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}_{self.product}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
