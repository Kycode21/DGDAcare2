from django.urls import path
from .views import *

urlpatterns = [
    path('suivi', suivi, name='suivi'),
    path('suspect/<int:id>', suspect, name='suspect'),
    path('contamines/<int:id>', contamines, name='contamines'),
    path('test_negatif/<int:id>', test_negatif, name='test_negatif'),
    path('test_positif/<int:id>', test_positif, name='test_positif'),
    path('deces/<int:id>', deces, name='deces'),
    path('gueri/<int:id>', gueri, name='gueri'),
    path('rendez_vous/', rendez_vous, name='rendez_vous'),
    path('update_rdv/<int:id>', update_rdv, name='update_rdv'),
    path('annuler_rdv/<int:id>', annuler_rdv, name='annuler_rdv'),
    path('effectuer_rdv/<int:id>', effectuer_rdv, name='effectuer_rdv'),
    path('consultation/', consultation, name='consultation'),
    path('antecedent/', antecedent, name='antecedent'),
    path('prescription/', prescription, name='prescription'),
    path('hospitalisation/', hospitalisation, name='hospitalisation'),
    path('update_hosp/<int:id>', update_hosp, name='update_hosp'),
    path('terminer_hosp/<int:id>', terminer_hosp, name='terminer_hosp'),
    path('compte_pers/', compte, name='compte_per'),
    path('update_comp/<int:id>', update_compte, name='update_compte_per')
]
