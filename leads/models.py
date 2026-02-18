from django.db import models
from django.conf import settings


class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('converted', 'Converted'),
        ('lost', 'Lost'),
    ]

    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(blank=True, default='')
    phone = models.CharField(max_length=30, blank=True, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    source = models.CharField(max_length=100, blank=True, default='')
    value = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    assigned = models.CharField(max_length=255, blank=True, default='')
    date_added = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='leads',
    )

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.name} ({self.status})"
