from django.db import models
from django.conf import settings
from parking.models import ParkingSpace
from django.core.validators import MinValueValidator
from django.utils import timezone
import uuid

# Create your models here.
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('A', 'Active'),
        ('E', 'Expired'),
        ('X', 'Canceled')
    ]
    
    reservation_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE, related_name='reservations')
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    payment_status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Reservation {self.reservation_id} - {self.user.username}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            duration_hours = (self.end_time - self.start_time).total_seconds() / 3600
            self.amount = self.parking_space.parking_lot.price_per_hour * duration_hours
        
        super().save(*args, **kwargs)
    
    @property
    def duration_hours(self):
        return (self.end_time - self.start_time).total_seconds() / 3600
    
    @property
    def is_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time and self.status == 'A'

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CC', 'Credit Card'),
        ('DC', 'Debit Card'),
        ('UPI', 'UPI Payment'),
        ('NB', 'Net Banking'),
        ('WL', 'Digital Wallet'),
        ('CS', 'Cash')
    ]
    
    PAYMENT_STATUS = [
        ('P', 'Pending'),
        ('S', 'Successful'),
        ('F', 'Failed'),
        ('R', 'Refunded')
    ]
    
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=3, choices=PAYMENT_METHODS, default='CC')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default='P')
    payment_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment for {self.reservation} - {self.get_payment_status_display()}"