#-------------------------------------------------------------------------------
# DATABASES
#-------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onboarding',
        'PORT': '3006',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'pass',
    }
}

ALLOWED_HOSTS = ["*"]