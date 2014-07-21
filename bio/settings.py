# -*- coding: utf-8 -*-
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
"""
Django settings for bio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0-7luo&5xu3qn4311ab)rf5p@&1b=kre2pi(j6$qvwfx!)+d=8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'www.bio-inbev.com'
]

SITE_ID=1


# Application definition

INSTALLED_APPS = (
    'suit',
    'suit_redactor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'mptt',
    'south',
    'page',
    'brand',
    'banner',
    'partner',
    'modeltranslation',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.i18n',
)


ROOT_URLCONF = 'bio.urls'

WSGI_APPLICATION = 'bio.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.i18n',
)
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'bio',
        'USER': 'jazdelu',
    'PASSWORD':'lushizhao1129',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


ugettext = lambda s: s

LANGUAGES = (
    ('en', ugettext(u'English')),
    ('zh-cn', ugettext(u'简体中文')),
)

LOCALE_PATHS = ( os.path.join(BASE_DIR, 'locale/'), )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'
MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'BIO-INBEV Website Manager',
    'HEADER_DATE_FORMAT': 'Y-m-d',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'MENU':(
        {'app':'auth','label':'User','icon':'icon-user'},
        {'app':'banner','label':'Banner','icon':'icon-leaf'},
        {'app':'brand','label':'Brand','icon':'icon-gift'},
        {'app':'page','label':'Page','icon':'icon-bookmark'},
        {'app':'partner','label':'Partner','icon':'icon-user'},
        {'label': 'Homepage', 'icon':'icon-leaf', 'url': '/'},
    ),
    # 'SEARCH_URL': '/admin/auth/user/',

    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # misc
    'LIST_PER_PAGE': 10
}

EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_HOST_USER = 'robot@minibobi.com'
EMAIL_HOST_PASSWORD = 'lushizhao1129'
DEFAULT_FROM_EMAIL = 'robot@minibobi.com'
SERVER_EMAIL = 'robot@minibobi.com'

