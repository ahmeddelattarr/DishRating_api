from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg, Count

class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=300)

    def number_of_ratings(self):
        return self.ratings.count()

    def avg_rating(self):
        return self.ratings.aggregate(Avg('stars'))['stars__avg'] or 0

    def __str__(self):
        return self.title

class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'meal'),)
        indexes = [
            models.Index(fields=['user', 'meal']),
        ]