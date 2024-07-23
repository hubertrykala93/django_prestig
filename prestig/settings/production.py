from .base import *

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = "/home/szymonlevy/domains/globalestatehub.com.pl/public_python/public/static/"
MEDIA_ROOT = "/home/szymonlevy/domains/globalestatehub.com.pl/public_python/public/media/"

SECURE_HSTS_SECONDS = 500000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
