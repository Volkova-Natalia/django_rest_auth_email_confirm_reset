from .base import BaseView
from ..serializers import PasswordResetConfirmationSerializer
from ..models import User
from ..emails.tokens import user_email_password_reset_token

from django.contrib.auth import login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode


class PasswordResetConfirmationView(BaseView):

    # --------------------------------------------------

    def put(self, request, uidb64, token, *args, **kwargs):
        """
        Check password reset confirmation link.
        Reset password if possible.
        """
        serializer = PasswordResetConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                uid = force_text(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None
            if user is not None and user_email_password_reset_token.check_token(user, token):
                user.is_active = True
                user.set_password(serializer.data['password'])
                user.save()
                login(request, user)
                # return redirect('home')
                return self.response_200(data={'message': 'Your password has been successfully reset.'})
            else:
                return self.response_400(data={'error': 'Password reset confirmation link is invalid!'})
        return self.response_400(data=serializer.errors)
