# Generated by Django 2.2.24 on 2022-01-04 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0007_auto_20220104_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
