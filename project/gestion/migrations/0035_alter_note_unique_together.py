# Generated by Django 4.2.1 on 2023-07-09 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0034_notemodule_module'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='note',
            unique_together={('num_et', 'num_cours')},
        ),
    ]
