from .base import *

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['notes.girlsgoit.org', 'notes-api.girlsgoit.org', 'ggit-notes-api.azurewebsites.net']
CORS_ORIGIN_WHITELIST = ('notes.girlsgoit.org', 'notes-api.girlsgoit.org', 'ggit-notes-api.azurewebsites.net')
CSRF_TRUSTED_ORIGINS = ['notes.girlsgoit.org', 'notes-api.girlsgoit.org']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}
