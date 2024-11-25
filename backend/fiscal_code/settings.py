import os, platform
from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv()

DOT_ENV_FILE = os.path.join(BASE_DIR, ".env")
if os.path.isfile(DOT_ENV_FILE):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY')

# Load environment variables from .env file
url = os.environ.get('URL')
input_filename = os.environ.get('INPUT_FILENAME')
output_filename = os.environ.get('OUTPUT_FILENAME')
header_row = ["Common_Name", "Common_Code"]
db_file = os.environ.get('DB_FILE')
table_name = os.environ.get('TABLE_NAME')
table_name_weather = os.environ.get('TABLE_NAME_WEATHER')
input_filename_weather = os.environ.get('INPUT_FILENAME_WEATHER')
weather_key = os.environ.get('WEATHER_KEY')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
server = platform.node()
if server == os.environ.get('SERVER_DEV'):
    DEBUG = True
else:
    DEBUG =False

ALLOWED_HOSTS = ['10.5.0.7','10.5.0.6','localhost','backend',]

CSRF_TRUSTED_ORIGINS = ['http://10.5.0.7:8080','http://localhost:8000']

# CORS urls to allow frontend requests
CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "http://localhost:80", "http://localhost:8080",]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    # user app
    'api',
    'weather',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # third party
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Whitenoise settings
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STORAGE = 'whitenoise.storage.ManifestStaticFilesStorage'

# REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

ROOT_URLCONF = 'fiscal_code.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fiscal_code.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')  # absolute path to the directory of all static files

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers':
    {
            'file': {  # Ensure correct handler name
                'level': os.environ.get('LOG_LEVEL'),
                'class': 'logging.handlers.RotatingFileHandler',  # No import needed
                'formatter': 'standard',
                'filename': os.path.join(BASE_DIR, 'logs', 'log.log'),
                'maxBytes': int(os.environ.get('LOG_MAX_BYTES')),  # Log file size
                'backupCount': int(os.environ.get('LOG_BACKUP_COUNT')),  # Keep 5 file di backup
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': os.environ.get('LOG_LEVEL'),
                'propagate': True,
            },
        },
}
