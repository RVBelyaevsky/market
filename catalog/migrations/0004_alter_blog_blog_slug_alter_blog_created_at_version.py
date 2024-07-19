# Generated by Django 4.2.13 on 2024-07-17 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_slug',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slug блога'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='номер')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('is_current', models.BooleanField(verbose_name='признак актуальности')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product',
                                              verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
