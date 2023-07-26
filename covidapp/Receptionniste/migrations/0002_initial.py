# Generated by Django 4.2.3 on 2023-07-16 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Receptionniste', '0001_initial'),
        ('app_auth', '0001_initial'),
        ('admini', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField()),
                ('telephone', models.CharField(max_length=15)),
                ('statut', models.CharField(default='suspect', max_length=50)),
                ('id_commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receptionniste.commune')),
                ('id_hopital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admini.hopital')),
                ('id_personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admini.personnelmedical')),
            ],
        ),
    ]
