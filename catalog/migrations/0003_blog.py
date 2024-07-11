# Generated by Django 4.2.13 on 2024-07-11 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100, verbose_name='Заголовок блога')),
                ('blog_slug', models.CharField(max_length=100, verbose_name='slug блога')),
                ('blog_content', models.TextField(verbose_name='Содержание блога')),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='Изображение блога')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_published', models.BooleanField(verbose_name='признак публикации')),
                ('count_views', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]