from distutils.command.register import register
from django.contrib import admin
from .models import *

admin.site.register([Commune, Patient])
