# -*- coding: utf-8 -*-

import os
import sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'hzp.settings'
app_apth = "/disk1/hzpDjango/hzp"
sys.path.append(app_apth)
application = django.core.handlers.wsgi.WSGIHandler()
