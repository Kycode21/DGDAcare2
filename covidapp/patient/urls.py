from django.urls import path
from .views import *

urlpatterns = [ 
    path('', docs, name='docs'),
    path('rdv', rdv, name='rdv'),
    path('consult', consult, name='consult'),
    path('prescription', presc, name='presc')
]
