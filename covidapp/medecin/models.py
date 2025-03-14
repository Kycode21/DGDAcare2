from django.db import models
from app_auth.models import User
from Receptionniste.models import *

class Rendez_vous(models.Model):
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    motif = models.CharField(max_length=50)
    date_rdv = models.DateField()
    statut = models.CharField(max_length=50, default='en cours')

    def __str__(self):
        return self.id_patient.id_user.username


class Antecedent(models.Model):
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.id_patient.id_user.username


class Consultation(models.Model):
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('terminée', 'Terminée')
    ]
    
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    sat_oxyg = models.IntegerField()
    freq_resp = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default='en_cours')

    def __str__(self):
        return f"Consultation de {self.id_patient.id_user.username} le {self.date}"

class Hospitalisation(models.Model):
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    motif = models.CharField(max_length=50)
    date_ent = models.DateField()
    date_sort = models.DateField()
    statut = models.CharField(max_length=50, default='en cours')

    def __str__(self):
        return self.id_patient.id_user.username


# Nouvelle classe Prescription qui remplace l'ancienne
class Prescription(models.Model):
    TYPE_CHOICES = [
        ('medicaments', 'Médicaments'),
        ('soins', 'Soins infirmiers'),
        ('examens', 'Examens'),
        ('hospitalisation', 'Hospitalisation'),
        ('equipement', 'Équipement médical'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(User, on_delete=models.CASCADE)
    date_prescription = models.DateTimeField(auto_now_add=True)
    type_prescription = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    statut = models.CharField(max_length=20, default='en_cours')
    
    def __str__(self):
        return f"Prescription pour {self.patient.nom} par Dr. {self.medecin.username}"