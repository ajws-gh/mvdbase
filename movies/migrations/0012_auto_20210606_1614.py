# Generated by Django 3.2.3 on 2021-06-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20210606_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='film_genre',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Western'), (7, 'Romance'), (3, 'Crime and mystery'), (11, 'Other'), (9, 'Thriller'), (2, 'Comedy'), (8, 'Science fiction'), (6, 'Horror'), (1, 'Adventure'), (4, 'Fantasy'), (5, 'Historical'), (0, 'Action')], default=11),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=32),
        ),
        migrations.AddConstraint(
            model_name='movie',
            constraint=models.UniqueConstraint(fields=('premiere', 'title'), name='unique_movie'),
        ),
        migrations.AlterModelTable(
            name='movie',
            table='movie',
        ),
    ]
