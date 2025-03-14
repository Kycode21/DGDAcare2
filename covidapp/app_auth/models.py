from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('receptionniste', 'Réceptionniste'),
        ('medecin', 'Médecin'),
        ('labo', 'Responsable Laboratoire'),
        ('pharmacien', 'Pharmacien'),
    ]
    
    photo = models.ImageField(upload_to='images')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    