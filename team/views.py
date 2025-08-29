from .models import TeamMember
from .serializers import TeamSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [AllowAny]
