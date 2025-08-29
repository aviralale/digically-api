from .models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "full_name",
            "email_address",
            "company_name",
            "service_needed",
            "budget_range",
            "project_details",
        ]
        read_only_fields = ["id"]
