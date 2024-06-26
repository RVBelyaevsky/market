# Generated by Django 4.2.13 on 2024-06-12 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Наименование категории')),
                ('category_description', models.TextField(verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Наименование продукта')),
                ('product_description', models.TextField(verbose_name='Описание продукта')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображение продукта')),
                ('product_price', models.IntegerField(verbose_name='Цена')),
                ('created_at', models.DateField(verbose_name='Дата создания')),
                ('updated_at', models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения')),
                ('product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='catalog.category', verbose_name='Категория продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('product_name',),
            },
        ),
    ]
