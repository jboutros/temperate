DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os, sys
PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'temperate.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'nestcontrol',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    )

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = "temperate.wsgi.application"

LOGIN_REDIRECT_URL = '/'

# DATABASES and SECRET_KEY should be defined in local.py

try:
    from .local import *
except ImportError:
    pass
