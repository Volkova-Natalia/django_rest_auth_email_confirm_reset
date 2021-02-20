# This file sets up and configures Django. It's used by scripts that need to
# execute as if running in a Django server.
import os
import django
from django.conf import settings


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "django_rest_auth_email_confirm_reset"))

FRONTEND_SCHEME = 'http'
FRONTEND_HOST = 'localhost:3000'


def boot_django():
    if not settings.configured:
        settings.configure(
            BASE_DIR=BASE_DIR,
            DEBUG=True,
            ALLOWED_HOSTS=[
                '127.0.0.1',
                'localhost',
            ],
            INSTALLED_APPS=[
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'rest_framework',
                'corsheaders',
                'django_rest_auth_email_confirm_reset',
            ],
            MIDDLEWARE=[
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'corsheaders.middleware.CorsMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ],
            ROOT_URLCONF='django_rest_auth_email_confirm_reset.urls',
            TEMPLATES=[
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [
                        os.path.join(BASE_DIR, 'templates'),
                    ]
                    ,
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
            ],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            },
            AUTH_USER_MODEL='django_rest_auth_email_confirm_reset.User',
            AUTH_PASSWORD_VALIDATORS=[
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
            ],

            LANGUAGE_CODE='en-us',
            TIME_ZONE="UTC",
            USE_I18N=True,
            USE_L10N=True,
            USE_TZ=True,

            STATIC_URL='/static/',
            STATICFILES_DIRS=[
                os.path.join(BASE_DIR, 'static'),
                os.path.join(BASE_DIR),  # for swagger.json
                os.path.join(os.path.dirname(BASE_DIR)),  # for swagger.json
            ],

            EMAIL_USE_TLS=True,
            EMAIL_HOST='smtp.gmail.com',
            EMAIL_HOST_USER='your-email@gmail.com',
            EMAIL_HOST_PASSWORD='your-email-password',
            EMAIL_PORT=587,

            EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',

            FRONTEND_SCHEME=FRONTEND_SCHEME,
            FRONTEND_HOST=FRONTEND_HOST,

            CORS_ALLOW_ALL_ORIGINS=False,
            CORS_ALLOWED_ORIGINS=[FRONTEND_SCHEME + r'://' + FRONTEND_HOST],
            CORS_ALLOW_CREDENTIALS=True,
            CSRF_TRUSTED_ORIGINS=[FRONTEND_HOST],
        )
        django.setup()
