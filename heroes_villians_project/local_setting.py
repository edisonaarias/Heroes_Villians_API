# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p@bsr+g8cca_@fcrx%=os0mom^1)ltcya^wxt!j-_fg+55@#*f'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villians_database',
        'HOST': 'localhost', 
        'USER': 'root',
        'PASSWORD': '555429ea',      
    }
}