"""
Django settings for blogger project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# https://stackoverflow.com/questions/76897614/cannot-import-name-load-dotenv-from-dotenv-with-django-docker
# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env. 


# https://pypi.org/project/django-database-url/
import dj_database_url


# Add the following line to the top of your code
from django.core.exceptions import ImproperlyConfigured



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY'),




# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



ALLOWED_HOSTS = ['*']




# Application definition
INSTALLED_APPS = [
    # https://django-jazzmin.readthedocs.io/installation/
    # Add jazzmin to your INSTALLED_APPS before django.contrib.admin
    'jazzmin',
    
    # Build-in app
    # -------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My local apps
   'blog.apps.BlogConfig',
   'user.apps.UserConfig',
   'pages.apps.PagesConfig',

   # Third party apps
   #-----------------
   # https://django-phonenumber-field.readthedocs.io/en/latest/
    "phonenumber_field",
   
    # https://pypi.org/project/django-bootstrap-v5/
    'bootstrap5',
    
    # https://fontawesome.com/docs/web/use-with/python-django#add-the-font-awesome-free-requirement-and-app
   'fontawesomefree',
   
    # crispy-bootstrap5
    # https://github.com/django-crispy-forms/crispy-bootstrap5?tab=readme-ov-file
    "crispy_forms",
    "crispy_bootstrap5",
     
    # django-ckeditor
    # https://pypi.org/project/django-ckeditor/
    # https://pypi.org/project/django-ckeditor/#installation
    #'ckeditor',
    #'ckeditor_uploader',
    
    # https://pypi.org/project/django-ckeditor-5/
    'django_ckeditor_5',
    'ckeditor_uploader',
    
    
    # pip install django-bootstrap-datepicker-plus
    # https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Getting_Started.html#install
    "bootstrap_datepicker_plus",
   
   
   # pip install django-countries
   # https://pypi.org/project/django-countries/
   "django_countries",
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogger.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],       # or you can write only    'DIRS':[BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # Other context processors
                'blog.context_processors.context_categories',
                'blog.context_processors.context_topposts',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogger.wsgi.application'







# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'

STATICFILES_DIRS = [ BASE_DIR / "static"]  #for static folder than put in main project root(near mnage.py file),which contain static belong to all project
#STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)     also work ok

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # for collectstatic for deployment



# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')




# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



############################################# custom user model settings ##############################################
# AUTH_USER_MODEL = "myapp.MyUser"
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
AUTH_USER_MODEL = 'user.UserModel'



######################################### Twilio Account SID and Auth Token settings ##############################################
# Twilio Account SID and Auth Token

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')

TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

# Twilio phone number used for sending SMS messages
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')






############################################# Database settings ##############################################

# PRODUCTION
# DATABASES = {
#     'default': dj_database_url.parse(os.environ.get('DATABASE_URL'),conn_max_age=600,conn_health_checks=True)                                              
# }


#https://django-environ.readthedocs.io/en/latest/quickstart.html 
import environ
env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': dj_database_url.parse(
           'postgres://blogger_db_ca0j_user:aOBm5pIJEWzj6YczxXrhpbQwuM5aArYQ@dpg-cmslkaacn0vc73bjkh40-a.oregon-postgres.render.com/blogger_db_ca0j',
            conn_max_age=600,
            conn_health_checks=True,
    )
 }
# print(DATABASES)




# DATABASES = {
#     'default': dj_database_url.parse(
#         'postgres://...',
#         conn_max_age=600,
#         conn_health_checks=True,
#     )
# }








#crispy-bootstrap5:
############################################# crispy-bootstrap5 settings ##############################################
# https://pypi.org/project/crispy-bootstrap5/      # need when use bootstrap5 with crispy form library
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# django-ckeditor setting 
####################################### django-ckeditor setting ##############################################
# https://pypi.org/project/django-ckeditor/#installation
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
}

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}

# https://baronchibuike.medium.com/hey-i-will-be-showing-you-how-you-can-implement-ckeditor-to-your-django-project-in-less-than-5mins-6fb66deb8f4b
CKEDITOR_UPLOAD_PATH = "uploads"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_THUMBNAIL_SIZE = (300, 300)
 # CKEDITOR_THUMBNAIL_SIZE = (300, 300)

CKEDITOR_IMAGE_QUALITY = 40

CKEDITOR_BROWSE_SHOW_DIRS = True

CKEDITOR_ALLOW_NONIMAGE_FILES = True

CKEDITOR_FORCE_JPEG_COMPRESSION = True




############################################# messages.ERROR ##############################################
# https://docs.djangoproject.com/en/4.2/ref/contrib/messages/
# https://stackoverflow.com/questions/55202684/does-bootstrap-django-error-message-has-no-red-color
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}



############################################# EMAIL settings ##############################################
# https://www.abstractapi.com/guides/django-send-email
# At this stage, we are going to configure email backend to send confirmation links. that done by tow ways:

# 1) to send confirmation links in console:
# -----------------------------------------
# EMAIL_BACKEND      = 'django.core.mail.backends.console.EmailBackend'
# DEFAULT_FROM_EMAIL = 'noreply@CodesCity'


#2) to send confirmation links by using your - SMTP Server of your Gmail:
# -----------------------------------------
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'your_username@gmail.com'
# EMAIL_HOST_PASSWORD = 'yourpassword'         #Note: get 'yourpassword' from  #https://myaccount.google.com/apppasswords
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# DEFAULT_FROM_EMAIL = 'noreply@yourwebsitename'


#EMAIL_BACKEND       = os.getenv('EMAIL_BACKEND')
#EMAIL_HOST          = os.getenv('EMAIL_HOST')
#EMAIL_HOST_USER     = os.getenv('EMAIL_HOST_USER') 
#EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
#EMAIL_PORT          = os.getenv('EMAIL_PORT')
#EMAIL_USE_TLS       = os.getenv('EMAIL_USE_TLS')
#EMAIL_USE_SSL       = os.getenv('EMAIL_USE_SSL')
#DEFAULT_FROM_EMAIL  = os.getenv('DEFAULT_FROM_EMAIL')



#3) to send confirmation links by using your - SMTP Server of your Yahoo mail:
# https://kinsta.com/blog/yahoo-smtp-settings/#:~:text=SMTP%20Server%3A%20smtp.mail.,TLS%3A%20Yes%20(if%20available)
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
