from django.db import models
from app_auth.models import User
from admini.models import Hopital, PersonnelMedical

class Commune(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Patient(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id_hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE)
    id_personnel = models.ForeignKey(PersonnelMedical, on_delete=models.CASCADE)
    id_commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    age = models.IntegerField()
    telephone = models.CharField(max_length=15)
    statut = models.CharField(max_length=50, default='suspect')
