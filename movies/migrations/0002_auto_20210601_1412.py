# Generated by Django 3.2.3 on 2021-06-01 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movie',
            name='film_genre',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Western'), (6, 'Horror'), (2, 'Comedy'), (5, 'Historical'), (0, 'Action'), (9, 'Thriller'), (11, 'Other'), (7, 'Romance'), (3, 'Crime and mystery'), (8, 'Science fiction'), (4, 'Fantasy'), (1, 'Adventure')], default=11),
        ),
    ]
