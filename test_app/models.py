from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Autohaus(models.Model):
    brand_auto = models.CharField(max_length=100)
    model_auto = models.CharField(max_length=100)
    engine_fuel = models.CharField(max_length=100)
    engine_volume = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    auto_img = models.ImageField(upload_to='img/')
    price = models.PositiveIntegerField(default=0)

    options = models.ForeignKey('AutoOptions', on_delete=models.SET_NULL, blank=True, null=True)

class AutoOptions(models.Model):
    option_name = models.CharField(max_length=100)
    option_description = models.TextField()
    option_price = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.option_name