# Generated by Django 4.2.1 on 2023-07-09 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0039_alter_enote_unique_together_remove_note_id_enote_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='num_cours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.cours'),
        ),
        migrations.AlterField(
            model_name='note',
            name='num_et',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.etudiant'),
        ),
    ]