from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Receptionniste.models import DossierMedical, Patient
from .models import Prescription
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_auth.models import User

@login_required
def liste_dossiers(request):
    if request.user.role == 'medecin':
        dossiers = DossierMedical.objects.filter(statut='en_cours')
        return render(request, 'medecin/liste_dossiers.html', {
            'dossiers': dossiers,
            'title': 'Dossiers Médicaux'
        })
    return redirect('connexion')

@login_required
def cloturer_dossier(request, id):
    if request.user.role == 'medecin':
        dossier = get_object_or_404(DossierMedical, id=id)
        dossier.statut = 'cloture'
        dossier.save()
        messages.success(request, "Dossier clôturé avec succès")
        return redirect('liste_dossiers')
    return redirect('connexion')

@login_required
def liste_prescriptions(request):
    if request.user.role == 'medecin':
        prescriptions = Prescription.objects.filter(medecin=request.user)
        return render(request, 'medecin/liste_prescriptions.html', {
            'prescriptions': prescriptions,
            'title': 'Prescriptions'
        })
    return redirect('connexion')

@login_required
def nouvelle_prescription(request):
    if request.user.role == 'medecin':
        if request.method == 'POST':
            patient_id = request.POST.get('patient')
            type_prescription = request.POST.get('type_prescription')
            description = request.POST.get('description')
            
            patient = get_object_or_404(Patient, id=patient_id)
            
            Prescription.objects.create(
                patient=patient,
                medecin=request.user,
                type_prescription=type_prescription,
                description=description
            )
            messages.success(request, "Prescription créée avec succès")
            return redirect('liste_prescriptions')
            
        patients = Patient.objects.all()
        return render(request, 'medecin/nouvelle_prescription.html', {
            'patients': patients,
            'title': 'Nouvelle Prescription'
        })
    return redirect('connexion')

@login_required
def compte(request):
    if request.user.role == 'medecin':
        title = 'Mon compte'
        id = request.user.id
        user = User.objects.get(id=id)
        return render(request, 'medecin/compte.html', {
            'title': title,
            'user': user
        })
    return redirect('connexion')

@login_required
def update_compte(request, id):
    if request.user.role == 'medecin':
        title = 'Mon compte'
        user = get_object_or_404(User, id=id)
        if request.method == 'POST':
            photo = request.FILES['photo']
            update = User.objects.get(id=id)
            update.photo = photo
            update.save()
            return redirect('compte_medecin')
        return render(request, 'medecin/update_compte.html', {
            'title': title,
        })
    return redirect('connexion')