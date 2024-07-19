from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category')
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'blog_title', 'created_at', 'count_views', 'blog_slug',)
    list_filter = ('is_published',)
    search_fields = ('blog_title', 'content',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'name', 'is_current', 'product')
    search_fields = ('number', 'name',)
