from django.db import models
import datetime
EXPIRY_CHOICES = [(1,"One Year"),(2,"Two Years"),(3,"Three Years"),(4,"Four Years"),(5,"Five Years"),]
class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField()
    license_date = models.DateField()
    license_expiry = models.IntegerField(choices=EXPIRY_CHOICES, default=1)
    class Meta:
        ordering = ['license_date']

    def isExpired(self):
        return (self.license_date.year + self.license_expiry) < datetime.date.today().year
    
    def __str__(self):
        return self.model+' - '+self.make


