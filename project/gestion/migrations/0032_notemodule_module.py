# Generated by Django 4.2.1 on 2023-07-09 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0031_notemodule_num_cours'),
    ]

    operations = [
        migrations.AddField(
            model_name='notemodule',
            name='module',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gestion.module'),
            preserve_default=False,
        ),
    ]
