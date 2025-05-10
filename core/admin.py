from django.contrib import admin
from .models import Donation, DonationStatus

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'food_type', 'pickup_time', 'current_status')
    list_filter = ('donor_type', 'food_type')
    search_fields = ('donor_name', 'pickup_address')

@admin.register(DonationStatus)
class DonationStatusAdmin(admin.ModelAdmin):
    list_display = ('donation', 'status', 'timestamp')
    list_filter = ('status',)
    search_fields = ('donation__donor_name', 'notes')
    date_hierarchy = 'timestamp'