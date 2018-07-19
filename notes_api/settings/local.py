from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ih^)lel1j*lu#^ok-g*-s0^hmwffdz^^w-fd(69w9s+a%6t%^^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
ALLOWED_HOSTS = ['*', 'localhost']
CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    )
}

