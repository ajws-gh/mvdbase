# Generated by Django 3.2.3 on 2021-06-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('premiere', models.DateField()),
                ('description', models.TextField(default='', max_length=300)),
                ('IMDB_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters')),
                ('duration', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('film_genre', models.PositiveSmallIntegerField(choices=[(1, 'Adventure'), (5, 'Historical'), (2, 'Comedy'), (9, 'Thriller'), (10, 'Western'), (7, 'Romance'), (4, 'Fantasy'), (8, 'Science fiction'), (0, 'Action'), (11, 'Other'), (3, 'Crime and mystery'), (6, 'Horror')], default=11)),
                ('url', models.CharField(blank=True, max_length=225, null=True)),
                ('yt_id', models.CharField(blank=True, max_length=225, null=True)),
                ('yt_title', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
    ]
