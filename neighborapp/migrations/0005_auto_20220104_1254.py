# Generated by Django 2.2.24 on 2022-01-04 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0004_neighborhood_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborapp.Location'),
        ),
    ]
