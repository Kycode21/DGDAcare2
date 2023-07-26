from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
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
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    sat_oxyg = models.IntegerField()
    freq_resp = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id_patient.id_user.username


class Prescription(models.Model):
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicament = models.CharField(max_length=50)
    quantite = models.IntegerField()
    posologie = models.CharField(max_length=50)

    def __str__(self):
        return self.id_patient.id_user.username


class Hospitalisation(models.Model):
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    motif = models.CharField(max_length=50)
    date_ent = models.DateField()
    date_sort = models.DateField()
    statut = models.CharField(max_length=50, default='en cours')

    def __str__(self):
        return self.id_patient.id_user.username
