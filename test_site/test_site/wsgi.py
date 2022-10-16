"""
WSGI config for test_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
# add the hellodjango project path into the sys.path
sys.path.append('/home/pi/Documents/Django_files/djenv/test_site')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/pi/Documents/Django_files/djenv/lib/python3.5/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_site.settings")

application = get_wsgi_application()
