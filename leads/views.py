from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from .models import Lead
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lead.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'], url_path='convert-to-client')
    def convert_to_client(self, request, pk=None):
        """
        Converts a lead to a client:
        1. Creates a Client record using the lead's data.
        2. Deletes the lead.
        Returns the newly created client data.
        """
        lead = self.get_object()

        # Import here to avoid circular imports
        from clients.models import Client
        from clients.serializers import ClientSerializer

        with transaction.atomic():
            client = Client.objects.create(
                name=lead.name,
                company=lead.company,
                email=lead.email,
                phone=lead.phone,
                health='active',
                assigned=lead.assigned,
                converted_from_lead=lead.id,
                created_by=request.user,
            )
            lead.delete()

        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
