
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4#jhq84=0@d*#=$j1%7ef4$#*$9dazlu$qr-_)9nebey-hzm1!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'besttaxi',
        'USER': 'postgres',
        'PASSWORD': 'test1234',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'NAME': 'besttaxitest',
        },
    }
}
