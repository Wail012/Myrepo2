# Generated by Django 4.2.1 on 2023-06-01 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_rename_option_etudiant_option1_alter_etudiant_cne'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='option1',
        ),
    ]
