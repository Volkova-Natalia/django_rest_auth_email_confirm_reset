from . import BaseViewsTestCase

from ....utils import get_namespace

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from django.urls import reverse


# Create your tests here.
class BaseAuthInfoViewsTestCase(BaseViewsTestCase):
    end_point_name = 'auth_info'
    user = None

    namespace = get_namespace()
    url = reverse(namespace + end_point_name)

    status_code_expected = {
        'get': {
            'success': status.HTTP_200_OK,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': status.HTTP_405_METHOD_NOT_ALLOWED,
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
            'success': None,    # is set in test
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': {
                'detail': ErrorDetail(string='Method "POST" not allowed.', code='method_not_allowed')
            },
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
        self.data_expected['get']['success'] = None
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    def get(self, *, client=None):
        client, response = super().get(client=client, url=self.url, data=None)
        return client, response

    def post(self, *, client=None):
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
