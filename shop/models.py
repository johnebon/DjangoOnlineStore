from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 255, blank = False, null = False)
    description = models.TextField(blank = False, null = False)
    price = models.PositiveIntegerField(blank = False, null = False)
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)
    rating = models.IntegerField(blank = True, null = True)
    
    def __str__(self):
        return self.name