from django.db import models

class AutohausREST(models.Model):
    brand_auto = models.CharField(max_length=100)
    model_auto = models.CharField(max_length=100)
    engine_fuel = models.CharField(max_length=100)
    engine_volume = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    auto_img = models.ImageField(upload_to='img/')
    price = models.PositiveIntegerField(default=0)
