# Generated by Django 3.2.3 on 2021-06-07 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actors', '0004_auto_20210606_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
