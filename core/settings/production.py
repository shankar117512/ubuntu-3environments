from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ["ubuntu-3environments-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ["https://ubuntu-3environments-production.up.railway.app"]

DATABASES = {
    "default": dj_database_url.config()
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
