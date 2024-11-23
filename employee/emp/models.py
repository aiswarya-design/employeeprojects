from django.db import models


# Create your models here.
class Emp(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to="image", null=True, blank=True)
