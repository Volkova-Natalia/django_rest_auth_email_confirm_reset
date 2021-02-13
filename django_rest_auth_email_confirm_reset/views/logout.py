from .base import BaseView

from django.contrib.auth import logout


class LogoutView(BaseView):

    # --------------------------------------------------

    def post(self, request, *args, **kwargs):
        if request.successful_authenticator is None:
            return self.response_401()
        logout(request)
        return self.response_200(data=None)
