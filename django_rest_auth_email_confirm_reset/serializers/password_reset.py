from rest_framework import serializers
from abc import abstractmethod

from ..models import User


class PasswordResetSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=254, allow_blank=False, allow_null=False, required=True)
    # name = serializers.CharField(max_length=254, allow_blank=True, required=False)
    # password = serializers.CharField(max_length=128, required=True)
    # is_staff = serializers.BooleanField(default=False, required=False)
    # is_active = serializers.BooleanField(default=True, required=False)
    # is_superuser = serializers.BooleanField(default=False, required=False)
    # last_login = serializers.DateTimeField(default=timezone.now, allow_blank=True, allow_null=True, required=False)
    # date_joined = serializers.DateTimeField(default=timezone.now, auto_now_add=True, required=False)

    # ======================================================================

    def validate_email(self, email):
        user = None
        if User.objects.filter(email=email).exists():
            user = User.objects.filter(email=email).get()

        if user is None:
            raise serializers.ValidationError(
                'user with this email was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return email

    # ======================================================================

    def get_user(self):
        user = User.objects.filter(email=self.validated_data['email']).get()
        return user

    # ======================================================================

    @abstractmethod
    def update(self, instance, validated_data):
        pass

    @abstractmethod
    def create(self, validated_data):
        pass
