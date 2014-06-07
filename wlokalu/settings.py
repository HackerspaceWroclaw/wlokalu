# Django settings for wlokalu project.

WLOKALU_USE_ADMIN_IFACE = False

WLOKALU_ROOT_DIR = __file__[0:__file__.rfind('/')]
WLOKALU_ROOT_DIR = WLOKALU_ROOT_DIR[0:WLOKALU_ROOT_DIR.rfind('/')]

# Logging configuration file (YAML or JSON, use appropriate extension)
WLOKALU_LOGGING_CONFIG = '%s/examples/logging.json' % (WLOKALU_ROOT_DIR)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
  # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
  'default': {
    # postgresql_psycopg2, postgresql, mysql, sqlite3 or oracle
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': '%s/db/wlokalu.db' % (WLOKALU_ROOT_DIR),
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
  }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '%s/static' % (WLOKALU_ROOT_DIR)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Where to store Django messages.
# Also available:  django.contrib.messages.storage.session.SessionStorage
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {
  message_constants.INFO: 'message',
}

# Generated with following code:
#   from random import choice
#   secret = ''.join([
#     choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
#     for i in range(50)
#   ])
#
# Make this unique, and don't share it with anybody.
#SECRET_KEY = '!727cf)#x@==2=9zanp#*9$lw@y=*qillclgj55o#-^wso71k5'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
#   'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'wlokalu.urls'

TEMPLATE_DIRS = (
  # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
  # Always use forward slashes, even on Windows.
  # Don't forget to use absolute paths, not relative paths.
  '%s/templates' % (WLOKALU_ROOT_DIR),
)

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  # Uncomment the next line to enable the admin:
  # 'django.contrib.admin',
  # Uncomment the next line to enable admin documentation:
  # 'django.contrib.admindocs',
)

LOGIN_URL = '/login'
TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.request', # enable `request' in templates
)

try:
  from settings_local import *
except ImportError:
  # nothing bad if no local settings, but Django could complain about missing
  # variable SECRET_KEY
  pass

if WLOKALU_USE_ADMIN_IFACE:
  INSTALLED_APPS += ("django.contrib.admin", "django.contrib.auth")
