from .base import BaseView
from ..models import User
from ..emails.tokens import user_email_confirmation_token

from django.contrib.auth import login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode


class ConfirmationView(BaseView):

    # --------------------------------------------------

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and user_email_confirmation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            # return redirect('home')
            return self.response_200(data={'message': 'Thank you for your email confirmation. Now you can login your account.'})
        else:
            return self.response_400(data={'error': 'Confirmation link is invalid!'})
