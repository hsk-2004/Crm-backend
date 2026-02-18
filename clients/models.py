from django.db import models
from django.conf import settings


class Client(models.Model):
    HEALTH_CHOICES = [
        ('active', 'Active'),
        ('at_risk', 'At Risk'),
        ('churned', 'Churned'),
        ('onboard', 'Onboarding'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(blank=True, default='')
    phone = models.CharField(max_length=30, blank=True, default='')
    health = models.CharField(max_length=20, choices=HEALTH_CHOICES, default='active')
    industry = models.CharField(max_length=100, blank=True, default='')
    revenue = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    mrr = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    assigned = models.CharField(max_length=255, blank=True, default='')
    since = models.DateField(auto_now_add=True)
    # Track which lead this client was converted from (optional)
    converted_from_lead = models.IntegerField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='clients',
    )

    class Meta:
        ordering = ['-since']

    def __str__(self):
        return f"{self.name} ({self.company})"
