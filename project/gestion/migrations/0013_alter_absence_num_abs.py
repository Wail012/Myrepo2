# Generated by Django 4.2.1 on 2023-06-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_salle_remove_classe_nplace_profsalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='num_abs',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]