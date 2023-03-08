import uuid
from django.db import models

# Create your models here.
class Ticket(models.Model):
    
    is_available = models.BooleanField(default = True)
    is_sold = models.BooleanField(default = False, blank=True)
    event_name = models.CharField(max_length=255, default="", blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=False, null=False)
    description = models.CharField(max_length=300, default="", blank=True)
    creation_date = models.DateField(auto_now_add=True)
    sales_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.event_name
    
    class Meta:
        ordering = ['creation_date']
        
