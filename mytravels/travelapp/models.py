from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):        
    city = models.CharField(max_length=300, blank = True)
    country = models.CharField(max_length=300, blank = True)
    
    def __str__(self):
        return self.city
        
class Report(models.Model):

    RATING_CHOICES = (
      (1, 'Not Recommended'),
      (2, 'Below Average'),
      (3, 'Average'),
      (4, 'Recommended'),
      (5, 'Must Not Miss'),
    )
    
    EASE_CHOICES = (
      (1, 'Not Worth It'),
      (2, 'Difficult'),
      (3, 'Organized'),
      (4, 'Simple'),
    )

    destination = models.ForeignKey(Destination)
    rating = models.IntegerField(default=1, blank = True, choices=RATING_CHOICES)
    easeOfTravel = models.IntegerField(default=1, blank = True, choices=EASE_CHOICES)
    topSights = models.CharField(max_length=300, blank = True)
    summary = models.CharField(max_length=300, blank = True)
    blog = models.TextField(blank = True)
    picture = models.ImageField('destination picture', upload_to='uploadedimg/', default='uploadedimg/default.jpg', blank=True)
    
    def __str__(self):
        return self.destination.city