# Generated by Django 4.2.1 on 2023-06-23 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0017_etudiant_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]