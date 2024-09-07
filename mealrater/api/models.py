from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg, Count

#Meal(title, done
# desc, done
# numberof
# rates,
# avg rating)

class Meal(models.Model):
    title=models.CharField(max_length=32)
    description=models.TextField(max_length=300)

    def number_of_rates(self):
        rating= Rating.objects.filter(meal=self)
        return len(rating)

    def avg_rate(self):
        sum=0
        ratings=Rating.objects.filter(meal=self)

        for rate in ratings:
            sum+=rate.stars
        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return 0

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)


