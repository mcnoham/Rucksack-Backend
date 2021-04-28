from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=0)
    description = models.TextField(max_length=500, default='')

    def str(self):  # unicode for Python 2
        return self.user.username

class TransportationTag(models.TextChoices):
    CAR = 'Car'
    TRAIN = 'Train'
    PLANE = 'Plane'
    MOTORCYCLE = 'Motorcycle'
    BICYCLE = 'Bicycle'

class AccommodationTag(models.TextChoices):
    HOTEL = 'Hotel'
    HOSTEL = 'Hostel'
    CONDO = 'Condo'
    CAMP = 'Campsite'

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default='')
    budget = models.IntegerField(default=0)
    duration_magnitude = models.IntegerField(default=0)
    duration_unit = models.CharField(max_length=10, default='')
    location_tag = models.CharField(max_length=20, default='')
    transportation_tag = models.TextField(choices=TransportationTag.choices, default='')
    accommodation_tag = models.TextField(choices=AccommodationTag.choices, default='')
    itinerary_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    number_of_ratings = models.IntegerField(default=0)
    

    def str(self):
        return self.itinerary_title + self.user.username

    def save(self, **kwargs):
        self.location_tag = self.location_tag.lower()
        return super(Itinerary, self).save( **kwargs)

    def getItinerary(location):
        context = []
        _itineraryList = Itinerary.objects.filter(location_tag__icontains=location)

        for i in _itineraryList:
            context.append(i)

        return context

    def updateRating(self,rating):
        self.itinerary_rating = ((self.itinerary_rating * self.number_of_ratings) + rating)/(self.number_of_ratings + 1)
        self.number_of_ratings = self.number_of_ratings + 1
        self.save()


class Rating (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, default=0)

# function is needed to create an authentication token for each user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
