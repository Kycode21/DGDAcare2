from django.urls import path
from .views import *
from .dashboard import dashboard

urlpatterns = [
  path('dashboard', dashboard, name='dashboard'),
  path('ajout_hopital', ajout_hopital, name='ajout_hopital'),
  path('update_hopital/<int:id>', update_hopital, name='update_hopital'),
  path('delete_hopital/<int:id>', delete_hopital, name='delete_hopital'),
  path('ajout_recept', ajout_recept, name='ajout_recept'),
  path('update_recept/<int:id>', update_recept, name='update_recept'),
  path('delete_recept/<int:id>', delete_recept, name='delete_recept'),
  path('ajout_pers', ajout_pers, name='ajout_pers'),
  path('update_pers/<int:id>', update_pers, name='update_pers'),
  path('delete_pers/<int:id>', delete_pers, name='delete_pers'),
  path('compte', compte, name='compte_admin'),
  path('update_compte/<int:id>', update_compte, name='update_compte_admin'),
]
