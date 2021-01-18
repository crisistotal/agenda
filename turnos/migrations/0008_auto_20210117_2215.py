# Generated by Django 3.1.3 on 2021-01-18 01:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turnos', '0007_auto_20210117_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='responsable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Responsable'),
        ),
    ]
