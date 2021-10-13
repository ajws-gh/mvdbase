from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Movie(models.Model):
    FILM_GENRES = [
        (0, 'Action'),
        (1, 'Adventure'),
        (2, 'Comedy'),
        (3, 'Crime and mystery'),
        (4, 'Drama'),
        (5, 'Fantasy'),
        (6, 'Historical'),
        (7, 'Horror'),
        (8, 'Romance'),
        (9, 'Science fiction'),
        (10, 'Thriller'),
        (11, 'Western'),
        (12, 'Other')
    ]
    added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=32, blank=False, help_text='Max - 150 characters')
    premiere = models.DateField(blank=False, help_text='(YYYY-MM-DD)')
    description = models.TextField(max_length=500, blank=False, help_text='Max - 500 characters')
    IMDB_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=False, help_text='(1 - 9,9)')
    poster = models.ImageField(upload_to='posters', blank=False, null=True)
    duration = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    film_genre = models.PositiveSmallIntegerField(default=12, choices=FILM_GENRES)
    director = models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    yt_url = models.CharField(max_length=225, blank=False, verbose_name='Trailer - YouTube URL',
                              help_text='Paste YouTube URL address or add it using our search bar')
    yt_id = models.CharField(max_length=225)
    yt_title = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['premiere', 'title'], name='unique_movie')
        ]
        ordering = ['title']

    @property
    def ratings(self):
        return self.rating.aggregate(avg_score=Avg('rating'))['avg_score']


class Rating(models.Model):
    STARS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    review = models.TextField(max_length=150, help_text='Max - 150 characters')
    rating = models.PositiveSmallIntegerField(default=1, choices=STARS, help_text='(1 - 5)')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rating')
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
