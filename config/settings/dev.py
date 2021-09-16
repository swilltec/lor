"""
Django settings for development project.
"""
from .base import *

DEBUG = True
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-6mfjq8y1lwwtuy)jp9h1l_y=5m+kd(p-8_%=_sa=jr@ez9^g2*') 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'