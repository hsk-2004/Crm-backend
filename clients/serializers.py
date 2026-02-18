from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    since = serializers.DateField(read_only=True)

    class Meta:
        model = Client
        fields = [
            'id', 'name', 'company', 'email', 'phone',
            'health', 'industry', 'revenue', 'mrr',
            'assigned', 'since', 'converted_from_lead',
        ]
        read_only_fields = ['id', 'since']
