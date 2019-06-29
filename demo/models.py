from django.db import models

# Create your models here.


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True, unique = True)
    data = models.TextField(blank=True)
