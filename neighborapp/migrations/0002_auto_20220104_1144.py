# Generated by Django 2.2.24 on 2022-01-04 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='neighbourhood',
            new_name='neighborhood',
        ),
    ]
