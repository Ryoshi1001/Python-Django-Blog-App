"""
WSGI config for django_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import os
import sys
from django.core.management import call_command
from decouple import config
from django.core.wsgi import get_wsgi_application

# Add your project directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')

# Get the WSGI application
application = get_wsgi_application()

# Check for environment variable and create superuser if needed
if config('CREATE_SUPERUSER', default='False') == 'True':
    try:
        # Create superuser using the management command
        call_command('create_superuser')
    except Exception as e:
        print(f"Error creating superuser: {e}")
