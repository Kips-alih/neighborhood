# Generated by Django 2.2.24 on 2022-01-04 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0005_auto_20220104_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborapp.Location'),
        ),
    ]