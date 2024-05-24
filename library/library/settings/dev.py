from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = "django-insecure-gcm17dd*1&crzhqlze)c-2qh5&26!fz+p=6hsol^jcpcmmvj+w"
=======
SECRET_KEY = "django-insecure-=gl!s+cdomtl^g&c-7%mxj4l5^-+f9l_in0np4@ba9op9+mr66"
>>>>>>> 1676cc63 (add)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
