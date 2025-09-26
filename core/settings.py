import os
from pathlib import Path
from decouple import Csv, config
import dj_database_url
from datetime import timedelta

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = config("DJANGO_SECRET_KEY") 
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# --- CORS settings ---
CORS_ALLOW_ALL_ORIGINS = True  # development only
# In production, use:
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "https://your-frontend.com"
# ]

# Applications
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'django_filters',
    'drf_spectacular',
    'django_celery_results',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'request_logging',

    # Custom apps
    'users',
    'jobs',
    'applications',
]

# Custom user model
AUTH_USER_MODEL = 'users.User'

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'request_logging.middleware.LoggingMiddleware',
]

# Logging
REQUEST_LOGGING = {
    "LOGGER_NAME": "django.request",
    "LOG_LEVEL": "INFO",
    "EXCLUDE_PATHS": ["/health-check/"],
}

# URLs and Templates
ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'core.wsgi.application'

# Database
DATABASES = {
    "default": dj_database_url.config(default=config("DATABASE_URL", default="sqlite:///db.sqlite3"))
}

# REST framework + JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
        'anon': '100/day',
    }
}

# drf-spectacular (Swagger)
SPECTACULAR_SETTINGS = {
    'TITLE': 'Nexus Job Board API',
    'DESCRIPTION': 'Job Board backend for Project Nexus',
    'VERSION': '1.0.0',
}

# Celery (optional)
CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='amqp://guest:guest@localhost:5672//')
CELERY_RESULT_BACKEND = 'django-db'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Simple JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  #collectstatic will put everything here

# Enable GZip + Cache for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
