from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status


class BaseView(APIView):
    content_type = 'application/json'

    # --------------------------------------------------

    def response_200(self, *, data):
        return Response(
            data=data,
            status=status.HTTP_200_OK,
            content_type=self.content_type
        )

    def response_201(self, *, data):
        return Response(
            data=data,
            status=status.HTTP_201_CREATED,
            content_type=self.content_type
        )

    # --------------------------------------------------

    def response_400(self, *, data):
        return Response(
            data=data,
            status=status.HTTP_400_BAD_REQUEST,
            content_type=self.content_type
        )

    def response_401(self):
        return Response(
            data=None,
            status=status.HTTP_401_UNAUTHORIZED,
            content_type=self.content_type
        )

    # --------------------------------------------------
