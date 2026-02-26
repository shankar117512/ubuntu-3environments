from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ["your-staging-domain.up.railway.app"]

DATABASES = {
    "default": dj_database_url.config()
}
