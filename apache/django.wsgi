import os
import sys

sys.path.append('/home/roca67/dev/django')
sys.path.append('/home/patricio/dev/django/proyecto')

os.environ['DJANGO_SETTINGS_MODULE'] = 'proyecto.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
