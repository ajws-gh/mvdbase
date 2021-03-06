# Generated by Django 3.2.3 on 2021-06-09 10:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_auto_20210607_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='url',
        ),
        migrations.AddField(
            model_name='movie',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='yt_url',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='YouTube URL'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='film_genre',
            field=models.PositiveSmallIntegerField(choices=[(8, 'Science fiction'), (4, 'Fantasy'), (7, 'Romance'), (11, 'Other'), (5, 'Historical'), (1, 'Adventure'), (0, 'Action'), (9, 'Thriller'), (10, 'Western'), (2, 'Comedy'), (3, 'Crime and mystery'), (6, 'Horror')], default=11),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='movies.movie'),
        ),
    ]
