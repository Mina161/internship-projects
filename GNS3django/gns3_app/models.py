from django.db import models

# Create your models here.
class Router(models.Model):
    name = models.CharField(max_length=200)
    device_type = models.CharField(max_length=200)
    ip = models.CharField(max_length=16)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name+" @ "+self.ip