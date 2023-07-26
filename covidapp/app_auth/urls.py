from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('connexion', connexion, name='connexion'),
    path('deconnexion', deconnexion, name='deconnexion'),
]