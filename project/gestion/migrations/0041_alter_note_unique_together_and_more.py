# Generated by Django 4.2.1 on 2023-07-09 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0040_alter_note_num_cours_alter_note_num_et'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='note',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='notec2',
            unique_together=set(),
        ),
    ]