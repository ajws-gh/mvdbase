# Generated by Django 3.2.3 on 2021-06-01 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_film_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='film_genre',
            field=models.PositiveSmallIntegerField(choices=[(7, 'Romance'), (0, 'Action'), (4, 'Fantasy'), (9, 'Thriller'), (8, 'Science fiction'), (10, 'Western'), (1, 'Adventure'), (2, 'Comedy'), (6, 'Horror'), (11, 'Other'), (3, 'Crime and mystery'), (5, 'Historical')], default=11),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=350)),
                ('stars', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
