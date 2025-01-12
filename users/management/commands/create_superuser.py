from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create a superuser if specified in environment variables'

    def handle(self, *args, **kwargs):
        if os.environ.get('CREATE_SUPERUSER') == 'True':
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
            
            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.WARNING('Superuser already exists'))
            else:
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
