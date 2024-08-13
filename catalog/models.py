from django.db import models

from users.models import User

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
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория продукта',
                                         **NULLABLE,
                                         related_name='categories')
    product_price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, null=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)
    publication = models.BooleanField(verbose_name='Опубликовано', default=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)
        permissions = [('can_cancel_publication', 'can cancel publication of product'),
                       ('can_change_description', 'cab change description of product'),
                       ('can_change_product_category', 'cab change category of product')]

    def __str__(self):
        return self.product_name


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='Заголовок блога')
    blog_slug = models.CharField(max_length=100, verbose_name='slug блога', **NULLABLE)
    blog_content = models.TextField(verbose_name='Содержание блога')
    blog_image = models.ImageField(upload_to='blogs/', verbose_name='Изображение блога', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='признак публикации')
    count_views = models.IntegerField(verbose_name='количество просмотров', default=0)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return self.blog_title


class Version(models.Model):

    number = models.IntegerField(verbose_name='номер')
    name = models.CharField(max_length=100, verbose_name='название')
    is_current = models.BooleanField(verbose_name='признак актуальности')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
