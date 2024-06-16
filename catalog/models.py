from django.db import models


NULLABLE = {'blank': True,
            'null': True}

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование категории')
    category_description = models.TextField(verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    product_description = models.TextField(verbose_name='Описание продукта')
    product_image = models.ImageField(upload_to='products/', verbose_name='Изображение продукта', **NULLABLE)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория продукта', **NULLABLE,
                                         related_name='categories')
    product_price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, null=True)
    manufactured_at = models.DateField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)

    def __str__(self):
        return self.product_name



