from django.db import models
from app_auth.models import User

class Hopital(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Receptionniste(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id_hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_user.username

class PersonnelMedical(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id_hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_user.username
