from django.db import models

# Create your models here.
class CollectModel(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name