"""
Django settings for bookstore_project project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', default=0))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',  # new

    # Third-party
    'crispy_forms',  # new
    'allauth',  # new
    'allauth.account',  # new

    # Local
    'users.apps.UsersConfig',  # new
    'pages.apps.PagesConfig',
]


# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # new

""" To use Crispy Forms we load crispy_forms_tags
at the top of a template and add {{
form|crispy }} to replace {{ form.as_p}}
for displaying form fields. We will take this
time to also add Bootstrap styling to the Submit button
 """

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore_project.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # new
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

WSGI_APPLICATION = 'bookstore_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# esto es la URL
STATIC_URL = '/static/'

# esto es para el local development
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# production development
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# en teoria esto no es necesario
""" The last setting is STATICFILES_FINDERS123 which tells Django how to look
for static
file directories.
It is implicitly set for us and although this is an optional
step, I prefer
to make it explicit in all projects. """

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# ###########USER CUSTOM MODEL##########
AUTH_USER_MODEL = 'users.CustomUser'  # new

# Le decime a django a donde enviar al usuario despues
# de un log in y log out
LOGIN_REDIRECT_URL = 'home'

# esto lo cambiamos porque implementamos el ALLAUTH
ACCOUNT_LOGOUT_REDIRECT = 'home'  # new
""" The issue is that django-allauth’s ACCOUNT_LOGOUT_REDIRECT
actually overrides the
built-in LOGOUT_REDIRECT_URL, however,
 since they both point to the homepage this
change may not be apparent. To future-proof
our application since maybe we don’t
want to always redirect to the homepage on logout,
we should be explicit here with
the logout redirect. """
# LOGOUT_REDIRECT_URL = 'home'

# django-allauth config
SITE_ID = 1  # new

# todo esto de allauth es para usar el email en lugar del
# usuario
AUTHENTICATION_BACKENDS = (  # esto esta pero no se ve en realidad
    # esta under the hood
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',  # new
)
# para consola
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # new

# si queremos agregar nuestro SMTP hay que hacer como
# el libro de djangoForBeginners
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# es el remember ME
# si ponemos  "none" aparece el tick
# si pones True no aparece pero siempre recuerda
# y False deducilo vos
# si no escribimos esto implicitamente, esta
# opcion es como que este en None
ACCOUNT_SESSION_REMEMBER = True  # new

# de fabria es True, por mas que no escribamos
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False  # new

# para usar el email y no el usuario para log in
ACCOUNT_USERNAME_REQUIRED = False  # new
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # new
ACCOUNT_EMAIL_REQUIRED = True  # new
ACCOUNT_UNIQUE_EMAIL = True  # new


# ###############

DEFAULT_FROM_EMAIL = 'admin@djangobookstore.com'
