from django.db import models

# Create your models here.
class Family(models.Model):
    user = models.CharField(max_length=255)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)

    def __str__(self):
        return self.user