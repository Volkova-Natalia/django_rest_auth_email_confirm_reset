from . import BaseViewsTestCase

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from django.urls import reverse


# Create your tests here.
class BasePasswordResetViewsTestCase(BaseViewsTestCase):
    end_point_name = 'password_reset'
    user = None

    url = reverse(end_point_name)

    status_code_expected = {
        'get': {
            'success': None,
            'fail': status.HTTP_405_METHOD_NOT_ALLOWED,
        },
        'post': {
            'success': status.HTTP_200_OK,
            'fail': status.HTTP_400_BAD_REQUEST,
        },
        'put': {
            'success': None,
            'fail': status.HTTP_405_METHOD_NOT_ALLOWED,
        },
        'delete': {
            'success': None,
            'fail': status.HTTP_405_METHOD_NOT_ALLOWED,
        }
    }

    data_expected = {
        'get': {
            'success': None,
            'fail': {
                'detail': ErrorDetail(string='Method "GET" not allowed.', code='method_not_allowed')
            },
        },
        'post': {
            'success': None,    # is set in test
            'fail': None,   # is set in test
        },
        'put': {
            'success': None,
            'fail': {
                'detail': ErrorDetail(string='Method "PUT" not allowed.', code='method_not_allowed')
            },
        },
        'delete': {
            'success': None,
            'fail': {
                'detail': ErrorDetail(string='Method "DELETE" not allowed.', code='method_not_allowed')
            },
        }
    }

    # ======================================================================

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(user=user, *args, **kwargs)

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        self.data_expected['post']['success'] = None
        self.data_expected['post']['fail'] = None
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    def get(self, *, client=None):
        client, response = super().get(client=client, url=self.url, data=None)
        return client, response

    def post(self, *, client=None):
        try:
            client, response = super().post(client=client, url=self.url, data={'email': self.user['email']})
        except:
            client, response = super().post(client=client, url=self.url, data=None)
        return client, response

    def put(self, *, client=None):
        client, response = super().put(client=client, url=self.url, data=None)
        return client, response

    def delete(self, *, client=None):
        client, response = super().delete(client=client, url=self.url, data=None)
        return client, response

    # ======================================================================

    def base_test_get(self, *, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + self.end_point_name
        super().base_test_get(response=response, success_fail=success_fail, assert_message=assert_message)

    def base_test_post(self, *, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + self.end_point_name
        super().base_test_post(response=response, success_fail=success_fail, assert_message=assert_message)

    def base_test_put(self, *, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + self.end_point_name
        super().base_test_put(response=response, success_fail=success_fail, assert_message=assert_message)

    def base_test_delete(self, *, response, success_fail, assert_message=''):
        assert_message = assert_message + ' ' + self.end_point_name
        super().base_test_delete(response=response, success_fail=success_fail, assert_message=assert_message)

    # ======================================================================