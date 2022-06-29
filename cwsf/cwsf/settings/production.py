from .defaults import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')