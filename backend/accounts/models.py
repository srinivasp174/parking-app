from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class User(AbstractUser):
    account_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_parking_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def __str__(self):
        return self.email if self.email else self.username