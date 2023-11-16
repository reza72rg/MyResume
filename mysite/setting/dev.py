from mysite.settings  import *


SECRET_KEY = 'django-insecure-p)md6j#%+vp_992m-cm3$p_!9jj9hy%o3l1f8_qrft06z-d0e@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# sites_framework
SITE_ID = 2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "assets"
]

X_FRAME_OPTIONS = "SAMEORIGIN"

