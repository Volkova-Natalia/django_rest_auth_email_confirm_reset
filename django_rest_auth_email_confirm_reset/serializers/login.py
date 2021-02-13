from rest_framework import serializers
from django.contrib.auth import authenticate, login
from abc import abstractmethod


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=150, required=True)
    first_name = serializers.CharField(max_length=30, allow_blank=True, required=False)
    last_name = serializers.CharField(max_length=150, allow_blank=True, required=False)
    email = serializers.EmailField(allow_blank=True, required=False)
    password = serializers.CharField(max_length=128, required=True)
    # is_staff = serializers.BooleanField(default=False, required=False)
    # is_active = serializers.BooleanField(default=True, required=False)
    # is_superuser = serializers.BooleanField(default=False, required=False)
    # last_login = serializers.DateTimeField(default=timezone.now, required=False)
    # date_joined = serializers.DateTimeField(default=timezone.now, required=False)

    # ======================================================================

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return data

    # ======================================================================

    def login(self, *, request):
        user = authenticate(username=self.validated_data['username'],
                            password=self.validated_data['password'])
        login(request, user)

    # ======================================================================

    @abstractmethod
    def update(self, instance, validated_data):
        pass

    @abstractmethod
    def create(self, validated_data):
        pass
