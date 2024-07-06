# Generated by Django 4.2.1 on 2023-06-23 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0015_rename_matiere_professeur_sexe'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='num_opt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.option'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='num_classe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.classe'),
            preserve_default=False,
        ),
    ]
