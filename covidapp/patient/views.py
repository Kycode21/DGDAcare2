from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Receptionniste.models import Patient  # Supprimé DossierMedical
from .models import Prescription, Consultation  # Ajouté Consultation
from django.contrib import messages
from app_auth.models import User

@login_required
def liste_dossiers(request):
    if request.user.role == 'medecin':
        # Remplacer DossierMedical par Consultation
        consultations = Consultation.objects.filter(
            id_patient__id_medecin__id_user=request.user
        )
        return render(request, 'medecin/liste_dossiers.html', {
            'consultations': consultations,
            'title': 'Consultations'
        })
    return redirect('connexion')

@login_required
def cloturer_dossier(request, id):
    if request.user.role == 'medecin':
        consultation = get_object_or_404(Consultation, id=id)
        consultation.statut = 'terminée'  # Ajoutez ce champ dans le modèle Consultation si nécessaire
        consultation.save()
        messages.success(request, "Consultation clôturée avec succès")
        return redirect('liste_dossiers')
    return redirect('connexion')

# ... le reste du fichier reste inchangé ...