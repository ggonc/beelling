from django.db import models

# Create your models here.
class Bill(models.Model):
    Name = models.CharField(max_length=100)
    Value = models.DecimalField(max_digits=10, decimal_places=2)
    DueDate = models.DateField()
    Category = models.CharField(max_length=50)
    IsActive = models.BooleanField()