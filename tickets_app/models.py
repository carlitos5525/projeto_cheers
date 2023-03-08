from django.db import models

# Create your models here.
class Ticket(models.Model):
    
    is_available = models.BooleanField(default = True)
    event_name = models.CharField(max_length=255, default="")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    def __str__(self):
        return self.name
    
