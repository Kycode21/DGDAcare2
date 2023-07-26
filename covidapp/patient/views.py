from django.shortcuts import render, redirect
from Receptionniste.models import Patient
from personnel.models import *

def docs(request):
    if request.user.is_authenticated:
        title = 'Mon dossier'
        id_user = request.user.id
        patient = Patient.objects.get(id_user__id=id_user)
        return render(request, 'patient/docs.html', {
            'title':title,
            'patient':patient,
        })
    else:
        return redirect('connexion')

def rdv(request):
    if request.user.is_authenticated:
        title='rendez-vous'
        id_user = request.user.id
        rendez_vous = Rendez_vous.objects.filter(id_patient=id_user)
        return render(request, 'patient/rdv.html', {
            'title':title,
            'rendez_vous': rendez_vous,
        })
    else:
        return redirect('connexion')

def consult(request):
    if request.user.is_authenticated:
        title = 'Consultation'
        id_user = request.user.id
        consultations = Consultation.objects.filter(id_patient=id_user)
        return render(request, 'patient/consult.html', {
            'title': title,
            'consultations': consultations,
        })
    else:
        return redirect('connexion')

def presc(request):
    if request.user.is_authenticated:
        title = 'Préscription'
        id_user = request.user.id
        prescription = Prescription.objects.filter(id_patient=id_user)
        return render(request, 'patient/prescription.html', {
            'title': title,
            'prescriptions': prescription
        })
    else:
        return redirect('connexion')