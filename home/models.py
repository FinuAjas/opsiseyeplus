from distutils.command.upload import upload
from email.mime import image
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='specs/')
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=300,null=True, blank=True,)

    def __str__(self):
        return self.name