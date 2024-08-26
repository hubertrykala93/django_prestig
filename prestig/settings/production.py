from .base import *
import os

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = "/home/szymonlevy/domains/globalestatehub.com.pl/public_python/public/static/"
MEDIA_ROOT = "/home/szymonlevy/domains/globalestatehub.com.pl/public_python/public/media/"

SECURE_HSTS_SECONDS = 500000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST_PRODUCTION"),
        'PORT': os.environ.get("DB_PORT_PRODUCTION"),
    }
}
