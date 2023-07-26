from django.urls import path
from .views import *

urlpatterns = [
   path('ajout_patient', ajout_patient, name='ajout_patient'),
   path('update_patient/<int:id>', update_patient, name='update_patient'),
   path('delete_patient/<int:id>', delete_patient, name='delete_patient'),
   path('liste_hosp', liste_hosp, name='liste_hosp'),
   path('compte', compte_recept, name='compte_recept'),
   path('update_compte/<int:id>', update_compte, name='update_compte_recept'),
]