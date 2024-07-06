# Generated by Django 4.2.1 on 2023-05-06 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_professeur_etudiant_cne_etudiant_adresse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='CNE',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='adresse',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='anneebac',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='prenom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='sexe',
            field=models.CharField(choices=[(' homme', 'homme'), ('femme', 'femme')], max_length=10),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='tel',
            field=models.IntegerField(max_length=100),
        ),
    ]
