import json

from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    """Команда для наполнения БД данными с JSON-файла"""

    @staticmethod
    def json_read_categories():
        """получение категорий с JSON-файла"""

        with open('catalog_data.json', encoding='utf-8') as f:
            content = json.load(f)

        categories = []
        for i in content:
            if i['model'] == 'catalog.category':
                categories.append({'pk': i['pk'], 'fields': i['fields']})

        return categories

    @staticmethod
    def json_read_products():
        """ получение продуктов с JSON-файла"""

        with open('catalog_data.json', encoding='utf-8') as f:
            content = json.load(f)

        products = []
        for i in content:
            if i['model'] == 'catalog.product':
                products.append({'pk': i['pk'], 'fields': i['fields']})

        return products

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'], category_name=category['fields']['category_name'],
                         category_description=category['fields']['category_description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product['pk'],
                        product_name=product['fields']['product_name'],
                        product_description=product['fields']['product_description'],
                        product_image=product['fields']['product_image'],
                        # product_category=Category.objects.get(pk=product['fields']['product_category']),
                        product_price=product['fields']['product_price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )

        Product.objects.bulk_create(product_for_create)