from django.shortcuts import get_object_or_404, redirect, render
from app_auth.generate_password import generate_password
from .models import *
from admini.models import *
from app_auth.models import User
from django.contrib import messages
from covidapp import settings
from medecin.models import Consultation, Prescription    
from django.core.mail import send_mail


def ajout_patient(request):
    if request.user.is_authenticated:
        title = 'Patients'
        id_user = request.user.id
        receptionniste = Receptionniste.objects.get(id_user__id=id_user)
        id_hopital = receptionniste.id_hopital
        personnels = PersonnelMedical.objects.filter(id_hopital=id_hopital)
        communes = Commune.objects.all()
        patients = Patient.objects.filter(
            id_hopital=id_hopital, id_personnel__id_hopital=id_hopital, statut='suspect') | Patient.objects.filter(
            id_hopital=id_hopital, id_personnel__id_hopital=id_hopital, statut='positif')
        transfert = Patient.objects.filter(id_hopital=id_hopital).exclude(
            id_personnel__id_hopital=id_hopital)
        if request.method == 'POST':
            nom = request.POST['nom'].lower()
            postnom = request.POST['postnom'].lower()
            prenom = request.POST['prenom'].lower()
            email = request.POST['email']
            motdepasse = generate_password()
            photo = request.FILES['photo']
            role = 'patient'
            print(motdepasse)
            if User.objects.filter(email=email):
                messages.error(
                    request, "L'adresse mail saisie est déjà utilisée !")
            else:
                user = User.objects.create_user(
                    username=nom, first_name=postnom, last_name=prenom, email=email, password=motdepasse, photo=photo, role=role)
                personnel = int(request.POST['personnel'])
                id_personnel = PersonnelMedical.objects.get(
                    id_user__id=personnel)
                commune = int(request.POST['commune'])
                id_commune = Commune.objects.get(id=commune)
                age = int(request.POST['age'])
                telephone = request.POST['telephone']
                statut = 'suspect'
                Patient.objects.create(
                    id_user=user, id_personnel=id_personnel, id_hopital=id_hopital, id_commune=id_commune, age=age, telephone=telephone, statut=statut)
                if user is not None:
                    messages.success(
                        request, "Le patient est enregistré avec succès")
                    sujet = "Bienvenu dans CovidApp, une App pour gérer les patients"
                    message = "Nom d'utilisateur : " + nom + "\n" + "Mot de passe : " + motdepasse
                    expediteur = settings.EMAIL_HOST_USER
                    destinateur = [email]
                    send_mail(sujet, message, expediteur,
                              destinateur, fail_silently=True)
        if request.method == 'GET':
            name = request.GET.get('recherche')
            if name is not None:
                patients = Patient.objects.filter(
                    id_hopital=id_hopital, id_user__username__icontains=name)
        return render(request, 'receptionniste/ajout_patient.html', {
            'title': title,
            'communes': communes,
            'personnels': personnels,
            'patients': patients,
            'transfert': transfert
        })
    else:
        return redirect('connexion')


def update_patient(request, id):
    if request.user.is_authenticated:
        title = 'Patients'
        id_user = request.user.id
        receptionniste = Receptionniste.objects.get(id_user__id=id_user)
        id_hopital = receptionniste.id_hopital
        personnels = PersonnelMedical.objects.filter(id_hopital=id_hopital)
        patient = get_object_or_404(Patient, id_user__id=id)
        if request.method == 'POST':
            nom = request.POST.get('nom').lower()
            postnom = request.POST.get('postnom').lower()
            prenom = request.POST.get('prenom').lower()
            personnel = int(request.POST.get('personnel'))
            id_personnel = PersonnelMedical.objects.get(id_user__id=personnel)
            update_user = User.objects.get(id=id)
            update_user.username = nom
            update_user.first_name = postnom
            update_user.last_name = prenom
            update_user.save()
            update_patient = Patient.objects.get(id_user__id=id)
            update_patient.id_personnel = id_personnel
            update_patient.save()
            sujet = "Message de mise à jour, Covidapp Rdc"
            message = "Votre nom d'utilisateur a été modifié, voici le nouveau nom d'utilisateur: " + nom
            expediteur = settings.EMAIL_HOST_USER
            destinateur = [update_user.email]
            send_mail(sujet, message, expediteur,
                      destinateur, fail_silently=True)
            return redirect('ajout_patient')
        return render(request, 'receptionniste/update_patient.html', {
            'title': title,
            'patient': patient,
            'personnels': personnels
        })
    else:
        return redirect('connexion')


def delete_patient(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        object = User.objects.get(id=id)
        object.delete()
        return redirect('ajout_patient')
    else:
        return redirect('connexion')


def liste_hosp(request):
    title = 'Hospitalisation'
    id_user = request.user.id
    receptionniste = Receptionniste.objects.get(id_user__id=id_user)
    id_hopital = receptionniste.id_hopital
    liste_hospitalisation = Hospitalisation.objects.filter(
        id_patient__id_hopital=id_hopital)
    return render(request, 'receptionniste/liste_hosp.html', {
        'title': title,
        'hospitalisations': liste_hospitalisation
    })


def compte_recept(request):
    if request.user.is_authenticated:
        title = 'Mon compte'
        id = request.user.id
        user = User.objects.get(id=id)
        return render(request, 'receptionniste/compte.html', {
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
        return redirect('compte_recept')
    return render(request, 'receptionniste/update_compte.html', {
        'title': title,
    })
