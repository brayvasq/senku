from django.db import models

# Create your models here.
class Game(models.Model):
    max_level = models.DecimalField(max_digits=4, decimal_places=3)
    steps = models.DecimalField(max_digits=4, decimal_places=3)
    time = models.DecimalField(max_digits=4, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
