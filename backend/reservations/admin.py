from django.contrib import admin
from .models import Reservation, Payment

class PaymentInline(admin.StackedInline):
    """Inline admin for Payment"""
    model = Payment
    can_delete = False
    extra = 0

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Admin interface for Reservation model"""
    list_display = ('reservation_id', 'user', 'vehicle_number', 'start_time', 'end_time', 'status', 'amount', 'payment_status')
    list_filter = ('status', 'payment_status', 'created_at')
    search_fields = ('reservation_id', 'user__username', 'user__email', 'vehicle_number')
    readonly_fields = ('reservation_id', 'created_at', 'updated_at')
    inlines = [PaymentInline]
    date_hierarchy = 'start_time'
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Admin interface for Payment model"""
    list_display = ('reservation', 'amount', 'payment_method', 'payment_status', 'payment_date')
    list_filter = ('payment_method', 'payment_status', 'payment_date')
    search_fields = ('reservation__reservation_id', 'transaction_id')
    readonly_fields = ('payment_date', 'last_updated')