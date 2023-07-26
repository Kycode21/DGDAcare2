from django.shortcuts import get_object_or_404, render, redirect
from app_auth.generate_password import generate_password
from .models import *
from django.contrib import messages
from covidapp import settings
from django.core.mail import send_mail


def ajout_hopital(request):
    if request.user.is_authenticated:
        title = 'Hopital'
        hopitals = Hopital.objects.all()
        if request.method == 'POST':
            nom = request.POST.get('nom').lower()
            if Hopital.objects.filter(nom=nom):
                messages.error(request, "L'hopital existe déjà !")
            else:
                Hopital.objects.create(nom=nom)
                messages.success(request, "Hopital ajouté avec succès")
        return render(request, 'admin/ajout_hopital.html', {
            'title': title,
            'hopitals': hopitals
        })
    else:
        return redirect('connexion')


def update_hopital(request, id):
    if request.user.is_authenticated:
        title = 'Hopital'
        hopital = get_object_or_404(Hopital, id=id)
        if request.method == 'POST':
            nom = request.POST.get('nom')
            update = Hopital.objects.get(id=id)
            update.nom = nom
            update.save()
            return redirect('ajout_hopital')
        return render(request, 'admin/update_hopital.html', {
            'title': title,
            'hopital': hopital
        })
    else:
        return redirect('connexion')


def delete_hopital(request, id):
    if request.user.is_authenticated:
        hopital = get_object_or_404(Hopital, id=id)
        hopital.delete()
        return redirect('ajout_hopital')
    else:
        return redirect('connexion')


def ajout_recept(request):
    if request.user.is_authenticated:
        title = 'Réceptionniste'
        hopitals = Hopital.objects.all()
        receptionnistes = Receptionniste.objects.all().order_by('id_user__username')
        if request.method == 'POST':
            nom = request.POST.get('nom').lower()
            postnom = request.POST.get('postnom').lower()
            prenom = request.POST.get('prenom').lower()
            email = request.POST.get('email')
            photo = request.FILES.get('photo')
            motdepasse = generate_password()
            role = 'receptionniste'
            print(motdepasse)
            if User.objects.filter(email=email):
                messages.error(
                    request, "L'adresse mail est déjà utilisée !")
            else:
                user = User.objects.create_user(
                    username=nom, first_name=postnom, last_name=prenom, email=email, password=motdepasse, photo=photo, role=role)

                hopital = int(request.POST.get('hopital'))
                id_hopital = Hopital.objects.get(id=hopital)
                Receptionniste.objects.create(
                    id_user=user, id_hopital=id_hopital)
                if user is not None:
                    messages.success(
                        request, "Réceptionniste ajouté avec succés")
                    sujet = "Bienvenu dans CovidApp, une App pour gérer les patients"
                    message = "Nom d'utilisateur : " + nom + "\n" + "Mot de passe : " + motdepasse
                    expediteur = settings.EMAIL_HOST_USER
                    destinateur = [email]
                    send_mail(sujet, message, expediteur,
                              destinateur, fail_silently=True)
        return render(request, 'admin/ajout_recept.html', {
            'title': title,
            'hopitals': hopitals,
            'receptionnistes': receptionnistes,
        })
    else:
        return redirect('connexion')


def update_recept(request, id):
    if request.user.is_authenticated:
        title = 'Réceptionniste'
        user = get_object_or_404(User, id=id)
        hopital = Hopital.objects.all()
        if request.method == 'POST':
            nom = request.POST['nom'].lower()
            postnom = request.POST['postnom'].lower()
            prenom = request.POST['prenom'].lower()
            hopital = int(request.POST.get('hopital'))
            id_hopital = Hopital.objects.get(id=hopital)
            update = User.objects.get(id=id)
            update_hopital = Receptionniste.objects.get(id_user__id=id)
            update.username = nom
            update.first_name = postnom
            update.last_name = prenom
            update_hopital.id_hopital = id_hopital
            update.save()
            update_hopital.save()
            sujet = "Message de mise à jour, Covidapp Rdc"
            message = "Votre nom d'utilisateur a été modifié, voici le nouveau nom d'utilisateur: " + nom
            expediteur = settings.EMAIL_HOST_USER
            destinateur = [update.email]
            send_mail(sujet, message, expediteur,
                      destinateur, fail_silently=True)
            return redirect('ajout_recept')
        return render(request, 'admin/update_recept.html', {
            'title': title,
            'user': user,
            'hopital': hopital
        })
    else:
        return redirect('connexion')


def delete_recept(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        user.delete()
        return redirect('ajout_recept')
    else:
        return redirect('connexion')


def ajout_pers(request):
    if request.user.is_authenticated:
        title = 'PersonnelMedical'
        hopitals = Hopital.objects.all()
        personnels = PersonnelMedical.objects.all().order_by('id_user__username')
        if request.method == 'POST':
            nom = request.POST.get('nom').lower()
            postnom = request.POST.get('postnom').lower()
            prenom = request.POST.get('prenom').lower()
            email = request.POST.get('email')
            photo = request.FILES.get('photo')
            motdepasse = generate_password()
            role = 'personnel'
            print(motdepasse)
            if User.objects.filter(email=email):
                messages.error(
                    request, "L'adresse mail est déjà utilisée !")
            else:
                user = User.objects.create_user(
                    username=nom, first_name=postnom, last_name=prenom, email=email, password=motdepasse, photo=photo, role=role)
                hopital = int(request.POST.get('hopital'))
                id_hopital = Hopital.objects.get(id=hopital)
                PersonnelMedical.objects.create(
                    id_user=user, id_hopital=id_hopital)
                if user is not None:
                    messages.success(
                        request, "Personnel médical ajouté avec succés")
                    sujet = "Bienvenu dans CovidApp, une App pour gérer les patients"
                    message = "Nom d'utilisateur : " + nom + "\n" + "Mot de passe : " + motdepasse
                    expediteur = settings.EMAIL_HOST_USER
                    destinateur = [email]
                    send_mail(sujet, message, expediteur,
                              destinateur, fail_silently=True)
        return render(request, 'admin/ajout_pers.html', {
            'title': title,
            'hopitals': hopitals,
            'personnels': personnels,
        })
    else:
        return redirect('connexion')


def update_pers(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        title = 'PersonnelMedical'
        hopital = Hopital.objects.all()
        if request.method == 'POST':
            nom = request.POST.get('nom').lower()
            postnom = request.POST.get('postnom').lower()
            prenom = request.POST.get('prenom').lower()
            hopital = int(request.POST.get('hopital'))
            id_hopital = Hopital.objects.get(id=hopital)
            update = User.objects.get(id=id)
            update_hopital = PersonnelMedical.objects.get(id_user__id=id)
            update.username = nom
            update.first_name = postnom
            update.last_name = prenom
            update_hopital.id_hopital = id_hopital
            update.save()
            update_hopital.save()
            sujet = "Message de mise à jour, Covidapp Rdc"
            message = "Votre nom d'utilisateur a été modifié, voici le nouveau nom d'utilisateur: " + nom
            expediteur = settings.EMAIL_HOST_USER
            destinateur = [update.email]
            send_mail(sujet, message, expediteur,
                      destinateur, fail_silently=True)
            return redirect('ajout_pers')
        return render(request, 'admin/update_pers.html', {
            'title': title,
            'user': user,
            'hopital': hopital
        })
    else:
        return redirect('connexion')


def delete_pers(request, id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id)
        user.delete()
        return redirect('ajout_pers')
    else:
        return redirect('connexion')


def compte(request):
    if request.user.is_authenticated:
        title = 'Mon compte'
        id = request.user.id
        user = User.objects.get(id=id)
        return render(request, 'admin/compte.html', {
            'title': title,
            'user': user
        })
    else:
        return redirect('connexion')


def update_compte(request, id):
    if request.user.is_authenticated:
        title = 'Mon compte'
        user = get_object_or_404(User, id=id)
        if request.method == 'POST':
            photo = request.FILES['photo']
            update = User.objects.get(id=id)
            update.photo = photo
            update.save()
            return redirect('compte_admin')
        return render(request, 'admin/update_compte.html', {
            'title': title,
        })
    else:
        return redirect('connexion')
