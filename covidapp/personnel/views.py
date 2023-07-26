from email import message
from turtle import title
from django.shortcuts import get_object_or_404, render, redirect
from Receptionniste.models import Patient
from admini.models import Hopital, PersonnelMedical
from .models import *
from django.contrib import messages
from covidapp import settings
from django.core.mail import send_mail


def suivi(request):
    if request.user.is_authenticated:
        title = 'Liste des patients'
        id_user = request.user.id
        personnel = PersonnelMedical.objects.get(id_user__id=id_user)
        id_hopital = personnel.id_hopital
        patient_suspect = Patient.objects.filter(
            id_personnel=id_user, statut='suspect', id_hopital=id_hopital)
        patient_contamine = Patient.objects.filter(
            id_personnel=id_user, statut='positif', id_hopital=id_hopital)
        if request.method == 'GET':
            suspect = request.GET.get('suspect')
            contamines = request.GET.get('contamines')
            if suspect is not None:
                patient_suspect = Patient.objects.filter(
                    id_personnel=id_user, statut='suspect', id_user__username__icontains=suspect)
            if contamines is not None:
                patient_contamine = Patient.objects.filter(
                    id_personnel=id_user, statut='positif', id_user__username__icontains=contamines)
        return render(request, 'personnel/suivi.html', {
            'title': title,
            'patient_suspects': patient_suspect,
            'patient_contamines': patient_contamine
        })
    else:
        return redirect('connexion')


def suspect(request, id):
    if request.user.is_authenticated:
        title = 'Liste des patients'
        patient = get_object_or_404(Patient, id_user__id=id)
        return render(request, 'personnel/suspect.html', {
            'title': title,
            'patient': patient,
        })
    else:
        return redirect('connexion')


def contamines(request, id):
    if request.user.is_authenticated:
        title = 'Liste des patients'
        id_user = request.user.id
        personnel = PersonnelMedical.objects.get(id_user__id=id_user)
        id_hopital = personnel.id_hopital
        patient = get_object_or_404(Patient, id_user__id=id)
        hopitals = Hopital.objects.exclude(nom=id_hopital)
        consultations = Consultation.objects.filter(id_patient=id)
        antecedent = Antecedent.objects.filter(id_patient=id)
        if request.method == 'POST':
            hopital = int(request.POST.get('hopital'))
            hopital_patient = Hopital.objects.get(id=hopital)
            update = Patient.objects.get(id_user__id=id)
            update.id_hopital = hopital_patient
            update.save()
            return redirect('suivi')
        return render(request, 'personnel/contamines.html', {
            'title': title,
            'patient': patient,
            'hopitals': hopitals,
            'consultations': consultations,
            'antecedents': antecedent
        })
    else:
        return redirect('connexion')


def test_negatif(request, id):
    if request.user.is_authenticated:
        id_patient = get_object_or_404(Patient, id_user_id=id)
        update = Patient.objects.get(id_user__id=id)
        update.statut = 'negatif'
        update.save()
        return redirect('suivi')
    else:
        return redirect('connexion')


def test_positif(request, id):
    if request.user.is_authenticated:
        id_patient = get_object_or_404(Patient, id_user_id=id)
        update = Patient.objects.get(id_user__id=id)
        update.statut = 'positif'
        update.save()
        return redirect('suivi')
    else:
        return redirect('connexion')


def deces(request, id):
    if request.user.is_authenticated:
        id_patient = get_object_or_404(Patient, id_user_id=id)
        update = Patient.objects.get(id_user__id=id)
        update.statut = 'deces'
        update.save()
        return redirect('suivi')
    else:
        return redirect('connexion')


def gueri(request, id):
    if request.user.is_authenticated:
        id_patient = get_object_or_404(Patient, id_user_id=id)
        update = Patient.objects.get(id_user__id=id)
        update.statut = 'guerie'
        update.save()
        return redirect('suivi')
    else:
        return redirect('connexion')


def rendez_vous(request):
    if request.user.is_authenticated:
        title = 'Rendez-vous'
        id_user = request.user.id
        personnel = PersonnelMedical.objects.get(id_user__id=id_user)
        id_hopital = personnel.id_hopital
        patient_contamine = Patient.objects.filter(
            id_personnel=id_user, statut='positif', id_hopital=id_hopital)
        if request.method == 'POST':
            patient = int(request.POST.get('patient'))
            id_patient = Patient.objects.get(id_user__id=patient)
            motif = request.POST.get('motif').lower()
            daterend = request.POST.get('daterend')
            Rendez_vous.objects.create(
                id_patient=id_patient, motif=motif, date_rdv=daterend)
            messages.success(request, "Rendez-vous enregistré")
            sujet = "CovidAPP RDC"
            message = "Vous avez un nouveau rendez-vous, veillez consulter votre compte pour plus de détaille"
            expediteur = settings.EMAIL_HOST_USER
            destinateur = [id_patient.id_user.email]
            send_mail(sujet, message, expediteur,
                      destinateur, fail_silently=True)
        rendez_vous = Rendez_vous.objects.filter(
            id_patient__id_personnel=id_user, statut='en cours')
        return render(request, 'personnel/rendez_vous.html', {
            'title': title,
            'patient_contamines': patient_contamine,
            'rendez_vous': rendez_vous
        })
    else:
        return redirect('connexion')


def update_rdv(request, id):
    if request.user.is_authenticated:
        title = 'Rendez-vous'
        rdv = get_object_or_404(Rendez_vous, id=id)
        if request.method == 'POST':
            motif = request.POST.get('motif')
            daterend = request.POST.get('daterend')
            update = Rendez_vous.objects.get(id=id)
            update.motif = motif
            update.date_rdv = daterend
            update.save()
            return redirect('rendez_vous')
        return render(request, 'personnel/update_rdv.html', {
            'title': title,
            'rdv': rdv
        })
    else:
        return redirect('connexion')


def annuler_rdv(request, id):
    if request.user.is_authenticated:
        rdv = get_object_or_404(Rendez_vous, id=id)
        id_rdv = Rendez_vous.objects.get(id=id)
        id_rdv.delete()
        return redirect('rendez_vous')
    else:
        return redirect('connexion')


def effectuer_rdv(request, id):
    if request.user.is_authenticated:
        rdv = get_object_or_404(Rendez_vous, id=id)
        update = Rendez_vous.objects.get(id=id)
        update.statut = 'fin'
        update.save()
        return redirect('rendez_vous')
    else:
        return redirect('connexion')


def consultation(request):
    if request.user.is_authenticated:
        title = 'Consultation'
        id_user = request.user.id
        patients = Patient.objects.filter(
            id_personnel=id_user, statut='positif')
        if request.method == 'POST':
            patient = int(request.POST.get('patient'))
            id_patient = Patient.objects.get(id_user__id=patient)
            temperature = int(request.POST.get('temperature'))
            sat_oxyg = int(request.POST.get('sat_oxyg'))
            freq_resp = int(request.POST.get('freq_resp'))
            description = request.POST.get('description')
            Consultation.objects.create(id_patient=id_patient, temperature=temperature,
                                        sat_oxyg=sat_oxyg, freq_resp=freq_resp, description=description)
            messages.success(request, 'Enregistrement réussi')
            return redirect('consultation')
        return render(request, 'personnel/consultation.html', {
            'title': title,
            'patients': patients
        })
    else:
        return redirect('connexion')


def antecedent(request):
    if request.user.is_authenticated:
        title = 'antecedent'
        id_user = request.user.id
        patients = Patient.objects.filter(
            id_personnel=id_user, statut='positif')
        if request.method == 'POST':
            patient = int(request.POST.get('patient'))
            id_patient = Patient.objects.get(id_user__id=patient)
            nom = request.POST.get('nom')
            Antecedent.objects.create(id_patient=id_patient, nom=nom)
            messages.success(request, "Enregistrement réussi")
        return render(request, 'personnel/antecedent.html', {
            'title': title,
            'patients': patients
        })
    else:
        return redirect('connexion')


def prescription(request):
    if request.user.is_authenticated:
        title = 'Préscription'
        id_user = request.user.id
        patients = Patient.objects.filter(
            id_personnel=id_user, statut='positif')
        if request.method == 'POST':
            patient = int(request.POST.get('patient'))
            id_patient = Patient.objects.get(id_user__id=patient)
            medicament = request.POST.get('medicament')
            quantite = request.POST.get('quantite')
            posologie = request.POST.get('posologie')
            Prescription.objects.create(
                id_patient=id_patient, medicament=medicament, quantite=quantite, posologie=posologie)
            messages.success(request, 'Enregistrement réussi')

            return redirect('prescription')
        return render(request, 'personnel/prescription.html', {
            'title': title,
            'patients': patients
        })
    else:
        return redirect('connexion')


def hospitalisation(request):
    title = 'Hospitalisation'
    id_user = request.user.id
    patients = Patient.objects.filter(id_personnel=id_user, statut='positif')
    hospitalisation = Hospitalisation.objects.filter(
        id_patient__id_personnel=id_user, statut='en cours')
    if request.method == 'POST':
        patient = int(request.POST.get('patient'))
        id_patient = Patient.objects.get(id_user__id=patient)
        motif = request.POST.get('motif')
        dateent = request.POST.get('dateent')
        datesort = request.POST.get('datesort')
        Hospitalisation.objects.create(
            id_patient=id_patient, motif=motif, date_ent=dateent, date_sort=datesort)
        messages.success(request, 'Enregistrement réussi')
        return redirect('hospitalisation')
    return render(request, 'personnel/hospitalisation.html', {
        'title': title,
        'patients': patients,
        'hospitalisation': hospitalisation
    })


def update_hosp(request, id):
    title = 'Hospitalisation'
    id_hosp = get_object_or_404(Hospitalisation, id=id)
    if request.method == 'POST':
        datesort = request.POST.get('datesort')
        id_hosp.date_sort = datesort
        id_hosp.save()
        return redirect('hospitalisation')
    return render(request, 'personnel/update_hosp.html', {
        'title': title,
    })


def terminer_hosp(request, id):
    id_hosp = get_object_or_404(Hospitalisation, id=id)
    id_hosp.statut = 'termine'
    id_hosp.save()
    return redirect('hospitalisation')


def compte(request):
    title = 'Mon compte'
    id = request.user.id
    user = User.objects.get(id=id)
    return render(request, 'personnel/compte.html', {
        'title': title,
        'user': user
    })


def update_compte(request, id):
    title = 'Mon compte'
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        update = User.objects.get(id=id)
        update.photo = photo
        update.save()
        return redirect('compte_per')
    return render(request, 'personnel/update_compte.html', {
        'title': title,
    })
