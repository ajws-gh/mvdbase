# Generated by Django 3.2.3 on 2021-06-17 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0012_auto_20210613_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actors',
            options={'ordering': ['name']},
        ),
    ]