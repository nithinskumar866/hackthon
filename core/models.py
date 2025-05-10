from django.db import models

class Donation(models.Model):
    DONOR_TYPES = (
        ('restaurant', 'Restaurant'),
        ('individual', 'Individual'),
        ('other', 'Other'),
    )
    
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    donor_phone = models.CharField(max_length=20)
    donor_type = models.CharField(max_length=20, choices=DONOR_TYPES)
    food_type = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    description = models.TextField()
    pickup_address = models.TextField()
    pickup_time = models.DateTimeField()
    expiry_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def current_status(self):
        """Returns the latest status of the donation"""
        status = self.statuses.last()  # Uses the related_name from DonationStatus
        return status.status if status else 'No status available'

    def __str__(self):
        return f"{self.donor_name} - {self.food_type}"

class DonationStatus(models.Model):
    STATUS_CHOICES = (
        ('listed', 'Listed'),
        ('claimed', 'Claimed'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    )
    
    donation = models.ForeignKey(
        Donation,
        on_delete=models.CASCADE,
        related_name='statuses'  # Added related_name for easier access
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        get_latest_by = 'timestamp'
        ordering = ['-timestamp']  # Newest first by default

    def __str__(self):
        return f"{self.donation} - {self.status}"