# Generated by Django 2.2.24 on 2022-01-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0011_auto_20220107_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='area_administrator',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='health_tell',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='police_tell',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
