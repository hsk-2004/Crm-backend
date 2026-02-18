from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    # Expose date_added as 'date' to match frontend field name
    date = serializers.DateField(source='date_added', read_only=True)

    class Meta:
        model = Lead
        fields = [
            'id', 'name', 'company', 'email', 'phone',
            'status', 'source', 'value', 'assigned',
            'date', 'date_added',
        ]
        read_only_fields = ['id', 'date', 'date_added']
