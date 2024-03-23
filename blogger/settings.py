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

from environ import Env
env = Env()
Env.read_env()   # take environment variables from .env using env()


# https://stackoverflow.com/questions/76897614/cannot-import-name-load-dotenv-from-dotenv-with-django-docker
# https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env using  os.getenv()


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
DEBUG = False



ALLOWED_HOSTS = ['blogger-no5a.onrender.com','localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = [ 'https://*.onrender.com' ]

INTERNAL_IPS = (
    '127.0.0.1',
    'localhost:8000'
)



# Application definition
INSTALLED_APPS = [
    # My local app
    # ------------
   'blog.apps.BlogConfig',
   'user.apps.UserConfig',
   'pages.apps.PagesConfig',
    
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
    # https://pypi.org/project/django-cloudinary-storage/
    # because django-cloudinary-storage overwrites Django collectstatic command. If you are going to use it only for media files though, it is django.contrib.staticfiles which has to be first:
    'cloudinary_storage',          # Django Cloudinary Storage
    'cloudinary',                  # Django Cloudinary Storage

    "django.contrib.sites",     # sitemaps
    'django.contrib.sitemaps',  # sitemaps 



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
    
    
    # pip install django-bootstrap-datepicker-plus
    # https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Getting_Started.html#install
    "bootstrap_datepicker_plus",
   
   
   # pip install django-countries
   # https://pypi.org/project/django-countries/
   "django_countries",
   
    
]

SITE_ID = 1  # sitemap - we have only one site in our project, we can use 1.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # https://whitenoise.readthedocs.io/en/latest/
    "whitenoise.middleware.WhiteNoiseMiddleware",
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
                'blog.context_processors.context_topcomments_posts',
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
STATIC_URL = '/static/'
# https://whitenoise.readthedocs.io/en/latest/
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



STATICFILES_DIRS = [ BASE_DIR / "static"]  #for static folder than put in main project root(near mnage.py file),which contain static belong to all project
#STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)     also work ok

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # for collectstatic for deployment

# Media
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR,'media/')                            # default storage of media in development 
DEFAULT_FILE_STORAGE ='cloudinary_storage.storage.MediaCloudinaryStorage' # default storage of media in production

# https://pypi.org/project/django-cloudinary-storage/
# https://console.cloudinary.com/pm/c-afee3441808c64b2b27ef8b52a557c/developer-dashboard
from environ import Env
env = Env()
Env.read_env()   # take environment variables from .env using env()
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME'),
    'API_KEY'   : env('CLOUD_API_KEY'),
    'API_SECRET': env('CLOUD_API_SECRET')
}



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





#crispy-bootstrap5:
############################################# crispy-bootstrap5 settings ##############################################
# https://pypi.org/project/crispy-bootstrap5/      # need when use bootstrap5 with crispy form library
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"




 # https://pypi.org/project/django-ckeditor-5/ 
 # https://www.letscodemore.com/blog/how-to-add-ckeditor5-in-django/
customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload"
        ],
    },
    "comment": {
        "language": {"ui": "en", "content": "en"},
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
        ],
    },
    "extends": {
        "language": "en",
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        "toolbar": [
            "heading",
            "codeBlock",
            "|",
            "outdent",
            "indent",
            "|",
            "bold",
            "italic",
            "link",
            "underline",
            "strikethrough",
            "code",
            "subscript",
            "superscript",
            "highlight",
            "|",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "insertImage",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "mediaEmbed",
            "removeFormat",
            "insertTable",
            "sourceEditing",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
                "|",
                "toggleImageCaption",
                "|"
            ],
            "styles": [
                "full",
                "side",
                "alignLeft",
                "alignRight",
                "alignCenter",
            ],
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
            "tableProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
            "tableCellProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
        },
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
        "list": {
            "properties": {
                "styles": True,
                "startIndex": True,
                "reversed": True,
            }
        },
        "htmlSupport": {
            "allow": [
                {"name": "/.*/", "attributes": True, "classes": True, "styles": True}
            ]
        },
    },
}









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
EMAIL_BACKEND      = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@CodesCity'


#2) to send confirmation links by using your - SMTP Server of your Gmail or yahoo mail :
# -----------------------------------------
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'your_username@gmail.com'
# EMAIL_HOST_PASSWORD = 'yourpassword'         #Note: get 'yourpassword' from  #https://myaccount.google.com/apppasswords
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# DEFAULT_FROM_EMAIL = 'noreply@yourwebsitename'


# EMAIL_BACKEND = 'django_email_utils.backends.HTMLEmailBackend'
# EMAIL_HOST = 'smtp.your-smtp-server.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your_email@example.com'
# EMAIL_HOST_PASSWORD = 'your_password'

# Debug logging (enable temporarily)
#logging.basicConfig(level=logging.DEBUG)




# EMAIL_BACKEND       = os.getenv('EMAIL_BACKEND')
# EMAIL_HOST          = os.getenv('EMAIL_HOST')
# EMAIL_HOST_USER     = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_PORT          = os.getenv('EMAIL_PORT')
# EMAIL_USE_TLS       = os.getenv('EMAIL_USE_TLS')
# #EMAIL_USE_SSL      = os.getenv('EMAIL_USE_SSL')
# DEFAULT_FROM_EMAIL  = os.getenv('DEFAULT_FROM_EMAIL')

# EMAIL_DEBUG = True
# if not EMAIL_HOST_USER or not EMAIL_HOST_PASSWORD:
#     raise ValueError('Missing EMAIL_HOST_USER or EMAIL_HOST_PASSWORD in environment variables.')
 
 
 
 
 

############################################# Database settings ##############################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Development
# sqlite3
# DATABASES = {
#     'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#   }
#}


# Development
# postgresql_psycopg2
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',

#        'NAME': os.getenv('DB_NAME'),

#        'USER': os.getenv('DB_USER'),

#        'PASSWORD': os.getenv('DB_PASSWORD'),

#        'HOST': os.getenv('DB_HOST'),

#        'PORT': os.getenv('DB_PORT'),
#    }
 
#}  


# PRODUCTION
#https://django-environ.readthedocs.io/en/latest/quickstart.html 
# DATABASES = {
#     'default': dj_database_url.parse('postgres://...',conn_max_age=600,conn_health_checks=True)
# }
DATABASES = {
   'default': dj_database_url.parse(env('DATABASE_URL'), conn_max_age=600, conn_health_checks=True)
}


# print(DATABASES)


SITE_URL = 'https://blogger-no5a.onrender.com'


