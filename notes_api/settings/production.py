from .base import *

DEBUG = False

# TODO [Marc] replace this with dynamic stuff from ENV
# SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['notes.girlsgoit.org']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}
