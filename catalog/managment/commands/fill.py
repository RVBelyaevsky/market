from datetime import datetime

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [{'product_name': 'apple', 'product_description': 'яблоко',
                         'product_category': 'fruits',
                         'product_price': 100, 'create_date': datetime.now()},
                        {'product_name': 'pineapple', 'product_description': 'ананас',
                         'product_category': 'fruits',
                         'product_price': 200, 'create_date': datetime.now()},
                        {'product_name': 'orange', 'product_description': 'апельсин',
                         'product_category': 'fruits',
                         'product_price': 300, 'create_date': datetime.now()},
                        ]
        products_for_create = []
        Product.objects.all().delete()
        for product in product_list:
            products_for_create.append(Product(**product))
        Product.objects.bulk_create(products_for_create)