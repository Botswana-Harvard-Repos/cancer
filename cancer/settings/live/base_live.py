import os

from ..base import *
from ..logging import LOGGING

DEBUG = False

ETC_DIR = os.path.join('/etc', APP_NAME, 'live')

LIVE_SYSTEM = 'LIVE'
KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')
AUTO_CREATE_KEYS = False

MYSQL_DIR = os.path.join('/etc', APP_NAME, 'live', 'mysql.conf')

with open(os.path.join(ETC_DIR, 'secret_key')) as f:
    SECRET_KEY = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': MYSQL_DIR,
        },
    },
}

INDEX_PAGE = 'https://cancer.bhp.org.bw'

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

STATIC_ROOT = os.path.expanduser('~/static/live/')

# edc_sync / sync files
EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None