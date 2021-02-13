from rest_framework import serializers
from django.contrib.auth import authenticate, login
from abc import abstractmethod

from ..models import User


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=254, allow_blank=False, required=True)
    name = serializers.CharField(max_length=254, allow_blank=True, required=False)
    password = serializers.CharField(max_length=128, required=True)
    # is_staff = serializers.BooleanField(default=False, required=False)
    # is_active = serializers.BooleanField(default=True, required=False)
    # is_superuser = serializers.BooleanField(default=False, required=False)
    # last_login = serializers.DateTimeField(default=timezone.now, allow_blank=True, allow_null=True, required=False)
    # date_joined = serializers.DateTimeField(default=timezone.now, auto_now_add=True, required=False)

    # ======================================================================

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return data

    # ======================================================================

    def login(self, *, request):
        user = authenticate(email=self.validated_data['email'],
                            password=self.validated_data['password'])
        login(request, user)

    # ======================================================================

    @abstractmethod
    def update(self, instance, validated_data):
        pass

    @abstractmethod
    def create(self, validated_data):
        pass
