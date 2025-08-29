from .models import TeamMember
from .serializers import TeamSerializer
from rest_framework import viewsets


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamSerializer
