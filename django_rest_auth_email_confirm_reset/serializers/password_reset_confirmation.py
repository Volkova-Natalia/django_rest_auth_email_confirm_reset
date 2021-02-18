from rest_framework import serializers
from abc import abstractmethod


class PasswordResetConfirmationSerializer(serializers.Serializer):

    # email = serializers.EmailField(max_length=254, allow_blank=False, required=False)
    # name = serializers.CharField(max_length=254, allow_blank=True, required=False)
    password = serializers.CharField(max_length=128, allow_blank=False, allow_null=False, required=True)
    # is_staff = serializers.BooleanField(default=False, required=False)
    # is_active = serializers.BooleanField(default=True, required=False)
    # is_superuser = serializers.BooleanField(default=False, required=False)
    # last_login = serializers.DateTimeField(default=timezone.now, allow_blank=True, allow_null=True, required=False)
    # date_joined = serializers.DateTimeField(default=timezone.now, auto_now_add=True, required=False)

    # ======================================================================

    @abstractmethod
    def update(self, instance, validated_data):
        pass

    @abstractmethod
    def create(self, validated_data):
        pass
