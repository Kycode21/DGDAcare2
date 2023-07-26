from Receptionniste.models import *
from personnel.models import *
from .models import *
from django.shortcuts import render
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, '')


def dashboard(request):
    title = 'Tableau de bord'
    now = datetime.today().strftime('%A %d %B %Y, %H:%M')
    positif = Patient.objects.filter(statut='positif').count()
    guerie = Patient.objects.filter(statut='guerie').count()
    deces = Patient.objects.filter(statut='deces').count()
    cumul = positif + guerie + deces
    positif_negatif = Patient.objects.exclude(statut='suspect').count()
    if positif < positif_negatif:
        if positif_negatif != 0:
            taux_positivite = int((positif/positif_negatif)*100)
        else:
            taux_positivite = 0
    else:
        taux_positivite = 0
    hospitalise = Hospitalisation.objects.filter(statut='en cours').count()
    if hospitalise < positif:
        if positif != 0:
            taux_hospitalisation = int((hospitalise/positif)*100)
        else:
            taux_hospitalisation = 0
    else:
        taux_hospitalisation = 0
    hospital = Hopital.objects.all().count()
    receptionniste = Receptionniste.objects.all().count()
    age1 = Patient.objects.filter(age__gte=0, age__lte=9, statut='positif').count()
    age2 = Patient.objects.filter(
        age__gte=10, age__lte=19, statut='positif').count()
    age3 = Patient.objects.filter(
        age__gte=20, age__lte=29, statut='positif').count()
    age4 = Patient.objects.filter(
        age__gte=30, age__lte=39, statut='positif').count()
    age5 = Patient.objects.filter(
        age__gte=40, age__lte=49, statut='positif').count()
    age6 = Patient.objects.filter(
        age__gte=50, age__lte=59, statut='positif').count()
    age7 = Patient.objects.filter(
        age__gte=60, age__lte=69, statut='positif').count()
    age8 = Patient.objects.filter(
        age__gte=70, age__lte=79, statut='positif').count()
    age9 = Patient.objects.filter(
        age__gte=80, age__lte=89, statut='positif').count()
    age10 = Patient.objects.filter(age__gte=90, statut='positif').count()
    bandal = Patient.objects.filter(
        id_commune__nom='bandal', statut='positif').count()
    barumbu = Patient.objects.filter(
        id_commune__nom='barumbu', statut='positif').count()
    bumbu = Patient.objects.filter(
        id_commune__nom='bumbu', statut='positif').count()
    gombe = Patient.objects.filter(
        id_commune__nom='gombe', statut='positif').count()
    kalamu = Patient.objects.filter(
        id_commune__nom='kalamu', statut='positif').count()
    kasavubu = Patient.objects.filter(
        id_commune__nom='kasavubu', statut='positif').count()
    kimbaseke = Patient.objects.filter(
        id_commune__nom='kimbaseke', statut='positif').count()
    kinshasa = Patient.objects.filter(
        id_commune__nom='kinshasa', statut='positif').count()
    kintambo = Patient.objects.filter(
        id_commune__nom='kintambo', statut='positif').count()
    kinsenso = Patient.objects.filter(
        id_commune__nom='kinsenso', statut='positif').count()
    lemba = Patient.objects.filter(
        id_commune__nom='lemba', statut='positif').count()
    limete = Patient.objects.filter(
        id_commune__nom='limete', statut='positif').count()
    lingwala = Patient.objects.filter(
        id_commune__nom='lingwala', statut='positif').count()
    makala = Patient.objects.filter(
        id_commune__nom='makala', statut='positif').count()
    maluku = Patient.objects.filter(
        id_commune__nom='maluku', statut='positif').count()
    masina = Patient.objects.filter(
        id_commune__nom='masina', statut='positif').count()
    matete = Patient.objects.filter(
        id_commune__nom='matete', statut='positif').count()
    montngafula = Patient.objects.filter(
        id_commune__nom='mont-ngafula', statut='positif').count()
    ndjili = Patient.objects.filter(
        id_commune__nom='ndjili', statut='positif').count()
    ngaba = Patient.objects.filter(
        id_commune__nom='ngaba', statut='positif').count()
    ngaliema = Patient.objects.filter(
        id_commune__nom='ngaliema', statut='positif').count()
    ngiringiri = Patient.objects.filter(
        id_commune__nom='ngiringiri', statut='positif').count()
    nsele = Patient.objects.filter(
        id_commune__nom='nsele', statut='positif').count()
    selembau = Patient.objects.filter(
        id_commune__nom='selembau', statut='positif').count()
    return render(request, 'admin/dashboard.html', {
        'title': title,
        'now': now,
        'positif': positif,
        'guerie': guerie,
        'deces': deces,
        'cumul': cumul,
        'taux_positivite': taux_positivite,
        'taux_hospitalisation': taux_hospitalisation,
        'positif_negatif': positif_negatif,
        'hospitalise': hospitalise,
        'hopital': hospital,
        'receptionniste': receptionniste,
        'age1': age1,
        'age2': age2,
        'age3': age3,
        'age4': age4,
        'age5': age5,
        'age6': age6,
        'age7': age7,
        'age8': age8,
        'age9': age9,
        'age10': age10,
        'bandal': bandal,
        'barumbu': barumbu,
        'bumbu': bumbu,
        'gombe': gombe,
        'kalamu': kalamu,
        'kasavubu': kasavubu,
        'kimbaseke': kimbaseke,
        'kinshasa': kinshasa,
        'kintambo': kintambo,
        'kinsenso': kinsenso,
        'lemba': lemba,
        'limete': limete,
        'lingwala': lingwala,
        'makala': makala,
        'maluku': maluku,
        'masina': masina,
        'matete': matete,
        'montngafula': montngafula,
        'ndjili': ndjili,
        'ngaba': ngaba,
        'ngaliema': ngaliema,
        'ngiringiri': ngiringiri,
        'nsele': nsele,
        'selembau': selembau
    })
