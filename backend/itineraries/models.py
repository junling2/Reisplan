from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Itinerary(models.Model):
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    startDate = models.DateField()
    endDate = models.DateField()
    familyFriendly = models.BooleanField()
    image = models.FileField(upload_to='images/', blank=True, null=True)
    trip_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    waypoint = models.ManyToManyField('WayPoint')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} {}".format(self.destination, self.startDate)

class WayPoint(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True)

class Attraction(models.Model):
    name = models.CharField(max_length=50)
    waypoint = models.ForeignKey(WayPoint, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class FoodStop(models.Model):
    name = models.CharField(max_length=50)
    waypoint = models.ForeignKey(WayPoint, on_delete=models.CASCADE)
    price = models.CharField(max_length=3, null=True)

class Bed(models.Model):
    name = models.CharField(max_length=50)
    waypoint = models.ForeignKey(WayPoint, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)



