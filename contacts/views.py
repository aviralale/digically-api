from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Inquiry model with custom permissions:
    - GET (list/retrieve): Admin only
    - POST (create): Anyone
    - PUT/PATCH/DELETE: Admin only
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_permissions(self):
        """
        Instantiate and return the list of permissions that this view requires.
        """
        if self.action == "create":
            permission_classes = [AllowAny]
        else:  # list, retrieve, update, destroy
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
