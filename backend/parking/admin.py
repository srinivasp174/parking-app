from django.contrib import admin
from .models import ParkingLot, ParkingSpace

class ParkingSpaceInline(admin.TabularInline):
    """Inline admin for ParkingSpace"""
    model = ParkingSpace
    extra = 1

@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    """Admin interface for ParkingLot model"""
    list_display = ('name', 'location', 'pin_code', 'price_per_hour', 'total_spaces', 'available_spaces', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'location', 'address', 'pin_code')
    inlines = [ParkingSpaceInline]

@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    """Admin interface for ParkingSpace model"""
    list_display = ('space_number', 'parking_lot', 'floor', 'status', 'is_accessible')
    list_filter = ('status', 'is_accessible', 'parking_lot')
    search_fields = ('space_number', 'parking_lot__name')