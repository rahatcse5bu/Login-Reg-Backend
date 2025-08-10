from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser for testing purposes'

    def handle(self, *args, **options):
        if User.objects.filter(email='admin@example.com').exists():
            self.stdout.write(
                self.style.WARNING('Superuser admin@example.com already exists')
            )
            return

        try:
            user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created superuser: {user.email}\n'
                    f'Username: admin\n'
                    f'Password: admin123\n'
                    f'Access admin panel at: http://localhost:8000/admin/'
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {e}')
            )
