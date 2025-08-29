from rest_framework import serializers
from .models import TeamMember


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ["id", "full_name", "designation", "profile_picture"]
        read_only_fields = ["id"]
