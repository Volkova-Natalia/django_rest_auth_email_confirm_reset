from .base import BaseView

from ..serializers import PasswordResetSerializer

from ..emails.send import send_user_email_password_reset_confirmation


class PasswordResetView(BaseView):

    # --------------------------------------------------

    def post(self, request, *args, **kwargs):
        """
        Send password reset confirmation link if possible.
        """
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.get_user()
            send_user_email_password_reset_confirmation(request=request, user=user)
            return self.response_200(data=serializer.data)
        return self.response_400(data=serializer.errors)
