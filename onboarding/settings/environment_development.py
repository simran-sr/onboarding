#-------------------------------------------------------------------------------
# DATABASES
#-------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'onboarding.sqlite3'),
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': '127.0.0.1',
        # 'PORT': '',
    }
}

ALLOWED_HOSTS = ["*"]