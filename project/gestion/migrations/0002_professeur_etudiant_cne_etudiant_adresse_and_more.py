# Generated by Django 4.2.1 on 2023-05-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CIN', models.IntegerField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('matiere', models.CharField(choices=[(' homme', 'homme'), ('femme', 'femme')], max_length=10)),
                ('tel', models.IntegerField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('titre', models.CharField(max_length=100)),
                ('salaire', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='CNE',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='adresse',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='anneebac',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='email',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='nom',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='prenom',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='tel',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='sexe',
            field=models.CharField(choices=[(' homme', 'homme'), ('femme', 'femme')], default=0, max_length=10),
        ),
    ]
