from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    """
    Custom serializer for user registration
    """

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }


class CustomUserSerializer(UserSerializer):
    """
    Custom serializer for user details
    """

    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "is_verified",
            "created_at",
        )
        read_only_fields = ("id", "is_verified", "created_at")
