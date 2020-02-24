import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Elite.settings')

from django.core.wsgi import get_wsgi_application
from whitenose.django import DjangoWhiteNoise
application = get_wsgi_application()
application = DjangoWhiteNoise(application)