# Generated by Django 4.2.1 on 2023-07-09 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0030_smodule'),
    ]

    operations = [
        migrations.AddField(
            model_name='notemodule',
            name='num_cours',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gestion.cours'),
            preserve_default=False,
        ),
    ]
