# Generated by Django 4.2.1 on 2023-06-23 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0016_classe_num_opt_note_num_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='classe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.classe'),
            preserve_default=False,
        ),
    ]
