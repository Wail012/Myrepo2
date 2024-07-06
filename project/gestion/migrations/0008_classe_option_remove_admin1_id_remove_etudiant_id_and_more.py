# Generated by Django 4.2.1 on 2023-06-01 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_rename_admin_admin1'),
    ]

    operations = [
        migrations.CreateModel(
            name='classe',
            fields=[
                ('num_classe', models.IntegerField(primary_key=True, serialize=False)),
                ('nplace', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='option',
            fields=[
                ('nom', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='admin1',
            name='id',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='id',
        ),
        migrations.RemoveField(
            model_name='professeur',
            name='id',
        ),
        migrations.AlterField(
            model_name='admin1',
            name='id1',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='CNE',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='CIN',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='module',
            fields=[
                ('nom', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.option')),
            ],
        ),
        migrations.CreateModel(
            name='cours',
            fields=[
                ('nom', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='absence',
            fields=[
                ('num_abs', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('execuse', models.TextField()),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.cours')),
                ('num_et', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='option',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gestion.option'),
            preserve_default=False,
        ),
    ]