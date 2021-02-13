from .base import BaseView


class AuthInfoView(BaseView):

    # --------------------------------------------------

    def get(self, request, *args, **kwargs):
        is_authenticated = (request.successful_authenticator is not None)
        return self.response_200(
            data={
                'is_authenticated': is_authenticated,
            }
        )
