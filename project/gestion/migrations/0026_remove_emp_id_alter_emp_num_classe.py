# Generated by Django 4.2.1 on 2023-07-04 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0025_emp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='id',
        ),
        migrations.AlterField(
            model_name='emp',
            name='num_classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.classe'),
        ),
    ]
