# Generated by Django 4.2.1 on 2023-07-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0020_etudiant1_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='parcours',
            field=models.CharField(choices=[(' Bac+2', 'Bac+2'), (' Bac+3', 'Bac+3'), (' Bac+4', 'Bac+4'), (' Bac+5', 'Bac+5')], default='Bac+2', max_length=10),
            preserve_default=False,
        ),
    ]