import sys
globals().update(vars(sys.modules['temperate.settings']))

# Here you can override the DB settings for the environment
# prod/staging/dev, etc

DATABASES = {
    # "default" is the master here. Django requires that at least one database be aliased to default
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'temperate',
        'USER': 'joe',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        },
}

ENVIRONMENT = "dev"

SECRET_KEY = 'ao87eu%$2!b(xsek5glw@%f21s#nd2!zq3nnp-@=odz+up-f_3'
