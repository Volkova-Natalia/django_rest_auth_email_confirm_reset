from .base import BaseView

from ..serializers import LoginSerializer


class LoginView(BaseView):

    # --------------------------------------------------

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.login(request=request)
            return self.response_200(data=serializer.data)
        return self.response_400(data=serializer.errors)
