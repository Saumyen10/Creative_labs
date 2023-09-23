from django.db import models

# Create your models here.

class File (models.Model):
    name = models.CharField(null=True, blank=True,max_length=100)
    file = models.FileField(max_length=100,null=True, blank=True,upload_to='files/')

    def __str__(self):
        return self.name