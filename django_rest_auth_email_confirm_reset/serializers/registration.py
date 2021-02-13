from rest_framework import serializers
from ..models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = (
        #     'username',
        #     'password'
        # )
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
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
        user = User.objects.create_user(username=self.data['username'],
                                        password=self.data['password'])
        user.save()
