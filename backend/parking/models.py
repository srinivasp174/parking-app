from django.db import models
from django.core.validators import MinValueValidator
import uuid

# Create your models here.
class ParkingLot(models.Model):
    lot_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    total_spaces = models.PositiveBigIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.location}"
    
    @property
    def available_spaces(self):
        return self.spaces.filter(status='A').count()
    
    @property
    def occupied_spaces(self):
        return self.spaces.filter(status='O').count()
    
    @property
    def reserved_spaces(self):
        return self.spaces.filter(status='R').count()
    
    @property
    def maintenance_spaces(self):
        return self.spaces.filter(status='M').count()

class ParkingSpace(models.Model):
    STATUS_CHOICES = [
        ('A', 'Available'),
        ('O', 'Occupied'),
        ('R', 'Reserved'),
        ('M', 'Maintenance')
    ]
    space_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE, related_name='spaces')
    space_number = models.CharField(max_length=10, null=False)
    floor = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    is_accessible = models.BooleanField(default=False, help_text="Space designed for accessibility needs")
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['parking_lot', 'space_number']
        
    def __str__(self):
        return f"{self.parking_lot.name} - Space {self.space_number}"