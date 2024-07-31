from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
# for admin
class AdminPanel(models.Model):
    code: models.CharField(max_length=10, unique=True)

# for addstylist
class Stylist(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    bookeddates = models.TextField(default="") # JSON-serialized (text) version of your list

class Appointment(models.Model):
    name = models.CharField(max_length=40)
    contact = models.IntegerField(default=0)
    package = models.CharField(max_length=25, default="Barat Makeup")
    stylistname = models.CharField(max_length=40)
    appointmentdate = models.TextField(default="")
    bookingdate = models.TextField(default="")
    totalamount = models.TextField(default="")
    description = models.TextField(null=True)


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    message = models.TextField()
    date = models.DateTimeField()
