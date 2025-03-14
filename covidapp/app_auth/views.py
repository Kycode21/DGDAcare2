from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'app_auth/home.html')


def connexion(request):
    if request.method == 'POST':
        nom = request.POST.get('nom').lower()
        motdepasse = request.POST.get('motdepasse')  # Sans le .lower()
        
        # Ajout de prints pour débugger
        print(f"Tentative de connexion avec : {nom}")
        
        user = authenticate(request, username=nom, password=motdepasse)
        
        if user is not None:
            print(f"Utilisateur trouvé avec le rôle : {user.role}")
            login(request, user)
            
            if user.role == 'admin':
                return redirect('dashboard')
            elif user.role == 'receptionniste':
                return redirect('ajout_patient')
            elif user.role == 'personnel':
                return redirect('suivi')
            elif user.role == 'patient':
                return redirect('docs')
        else:
            print("Authentification échouée")
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
            
    return render(request, 'app_auth/connexion.html')

    
def deconnexion(request):
    logout(request)
    return redirect('connexion')