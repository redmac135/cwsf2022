from .defaults import *

DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS=['https://localhost:8000','https://127.0.0.1:8000','http://localhost:8000','http://127.0.0.1:8000']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
    }
}

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False