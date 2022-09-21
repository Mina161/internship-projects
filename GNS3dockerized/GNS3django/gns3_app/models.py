from django.db import models

# Create your models here.
class Router(models.Model):
    name = models.CharField(max_length=200)
    device_type = models.CharField(max_length=200)
    host = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    port = models.IntegerField()
    
    def __str__(self):
        return self.name+" @ "+self.host+":"+str(self.port)