from rest_framework import serializers
from ..models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'name',
            'password',
            # 'groups',
            # 'user_permissions',
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
            'date_joined'
        )

    def save(self, **kwargs):
        user = User.objects.create_user(email=self.data['email'],
                                        password=self.data['password'])
        user.save()
