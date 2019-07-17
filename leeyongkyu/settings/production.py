from .base import *
import environ

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

env = environ.Env()

#ALLOWED_HOSTS = ['pure-shore-88696.herokuapp.com', 'easternpresbyterian.church', 'www.easternpresbyterian.church']
SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS').split(',')

#pure-shore-88696.herokuapp.com,.easternpresbyterian.church