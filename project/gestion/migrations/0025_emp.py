# Generated by Django 4.2.1 on 2023-07-04 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0024_cours_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours1', models.CharField(max_length=100)),
                ('cours2', models.CharField(max_length=100)),
                ('prof1', models.IntegerField()),
                ('prof2', models.IntegerField()),
                ('num_classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.classe')),
            ],
        ),
    ]
