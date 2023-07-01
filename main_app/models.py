from django.db import models

class Country(models.Model):

    name = models.CharField(max_length=200, default='Unnamed Country')
    image = models.URLField(max_length=400, default='No Image URL')
    capital = models.CharField(max_length=200, default='No Capital')
    language = models.CharField(max_length=200, default='No Language')
    currency = models.CharField(max_length=200, default='No Currency')
    population = models.IntegerField(default=0)

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
