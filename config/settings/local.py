from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='xo+x@mbnlcm(x&$_0yzek%5kxfmk%!1#&z*nz)n==k%du*r-x$')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
