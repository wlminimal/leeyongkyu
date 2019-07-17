from .base import *
import environ

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

env = environ.Env()

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS')
SECRET_KEY = env('DJANGO_SECRET_KEY')