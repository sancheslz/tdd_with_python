from .base import *
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ALLOWED_HOSTS = [
    '192.168.1.105'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../database/production.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../static'))
