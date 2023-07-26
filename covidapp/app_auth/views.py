from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'app_auth/home.html')


def connexion(request):
    if request.method == 'POST':
        nom = request.POST.get('nom').lower()
        motdepasse = request.POST.get('motdepasse').lower()
        user = authenticate(request, username=nom, password=motdepasse)
        if user is not None and user.role == 'admin':
            login(request, user)
            return redirect('dashboard')
        elif user is not None and user.role == 'receptionniste':
            login(request, user)
            return redirect('ajout_patient')
        elif user is not None and user.role == 'personnel':
            login(request, user)
            return redirect('suivi')
        elif user is not None and user.role == 'patient':
            login(request, user)
            return redirect('docs')
        else:
            messages.error(request, "Informations incorrectes")
    return render(request, 'app_auth/connexion.html')


def deconnexion(request):
    logout(request)
    return redirect('connexion')
