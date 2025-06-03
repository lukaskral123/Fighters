from django.db import models

class Fighter(models.Model):
    name = models.CharField(max_length=100)
    weight_class = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
