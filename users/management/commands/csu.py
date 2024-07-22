from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@example.com',
            is_staff=True,
            is_superuser=True,
            first_name='Admin',
            last_name='User'
        )

        user.set_password('77777777')
        user.save()
