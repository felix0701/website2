import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'

DEBUG = False

ALLOWED_HOSTS = ['*']


# Set your site ID (usually 1, but replace it if needed)
SITE_ID = 2

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uk',
    'django.contrib.sites',  # Add this line for Django sites framework
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'captcha',
    'social_django',

]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Define Google OAuth2 configuration
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    },
}
SOCIALACCOUNT_LOGIN_ON_GET=True
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Add this line
]

ROOT_URLCONF = 'connectai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'connectai.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
LOGIN_URL = '/login'
# Email Verification
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server.com'  # Replace with your SMTP server
EMAIL_PORT = 587  # Use the appropriate port
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your-password'  # Replace with your email password
LOGIN_REDIRECT_URL = '/feed' 
SIGNUP_REDIRECT_URL = '/fill_details'
LOGOUT_REDIRECT_URL = '/'

RECAPTCHA_PUBLIC_KEY = '6LealbMoAAAAAME17tKD1kbSbTMZm4iePE7IbXJj'
RECAPTCHA_PRIVATE_KEY = '6LealbMoAAAAAPEvQpLKIPysfkEE9lbzz2MJxC3Y'

CSRF_USE_SESSIONS = False