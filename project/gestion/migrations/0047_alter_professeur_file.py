# Generated by Django 4.2.1 on 2023-07-10 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0046_alter_professeur_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professeur',
            name='file',
            field=models.FileField(upload_to='static/'),
        ),
    ]
