from django.db import models
from movies.models import Movie
from django.contrib.auth.models import User
from django.db.models import Avg


class Actors(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    birthday = models.DateField(blank=False, help_text='(YYYY-MM-DD)')
    movie = models.ManyToManyField(Movie, related_name='actors', verbose_name='Movies')
    image = models.ImageField(upload_to='images')
    Filmweb_rating = models.DecimalField(max_digits=2, default=0, decimal_places=1, help_text='(1 - 9,9)')
    description = models.TextField(max_length=500, default='', help_text='Max - 500 characters')
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'surname', 'birthday'], name='unique_actor')
        ]
        ordering = ['name']

    @property
    def ratings(self):
        return self.rating.aggregate(avg_score=Avg('rating'))['avg_score']


class Ratings(models.Model):
    STARS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    review = models.TextField(max_length=150, help_text='Max - 150 characters')
    rating = models.PositiveSmallIntegerField(default=1, choices=STARS, help_text='(1 - 5)')
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE, related_name='rating')
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
