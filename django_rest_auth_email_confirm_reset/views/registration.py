from .base import BaseView

from ..serializers import RegistrationSerializer

from ..emails.send import send_user_email_confirmation


class RegistrationView(BaseView):

    # --------------------------------------------------

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()
            send_user_email_confirmation(request=request, user=user)
            return self.response_201(
                data={
                    'id': user.id,
                }
            )
        return self.response_400(data=serializer.errors)
