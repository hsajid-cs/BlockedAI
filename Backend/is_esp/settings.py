from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-aqyjop*gi4d!5svd5f1me-4*7ow85*z_=tbz+m6!3auu@)t2be'
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

# CORS policy
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000', 
]
CORS_ALLOW_HEADERS = [
    'content-type', 'authorization',  
]

# Turn off django's default interface for testing
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

# Root URL location
ROOT_URLCONF = 'is_esp.urls'

# WSGI application
WSGI_APPLICATION = 'is_esp.wsgi.application'

# Language and Time
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Static files 
STATIC_URL = 'static/'
