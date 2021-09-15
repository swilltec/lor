"""
Django settings for production project.
"""
import os
from dotenv import load_dotenv

from .base import *


load_dotenv()  # take environment variables from .env.

DEBUG = False
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# Security setup
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_REFERRER_POLICY =None
CSRF_COOKIE_SAMESITE = 'Lax'

#Email setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('MAIL_SERVER')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('MAIL_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('MAIL_PASSWORD')
