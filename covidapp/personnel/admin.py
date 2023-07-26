from django.contrib import admin
from .models import *

admin.site.register([Consultation, Rendez_vous, Antecedent, Prescription, Hospitalisation])