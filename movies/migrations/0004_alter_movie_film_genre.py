# Generated by Django 3.2.3 on 2021-06-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_film_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='film_genre',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Action'), (10, 'Western'), (1, 'Adventure'), (3, 'Crime and mystery'), (5, 'Historical'), (4, 'Fantasy'), (6, 'Horror'), (11, 'Other'), (7, 'Romance'), (2, 'Comedy'), (8, 'Science fiction'), (9, 'Thriller')], default=11),
        ),
    ]
