from . import BaseViewsTestCase

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from django.urls import reverse


# Create your tests here.
class BaseLogoutViewsTestCase(BaseViewsTestCase):
    user = None

    url = reverse('logout')

    status_code_expected = {
        'get': {
            'success': None,
            'fail': status.HTTP_405_METHOD_NOT_ALLOWED,
        },
        'post': {
            'success': status.HTTP_200_OK,
            'fail': status.HTTP_401_UNAUTHORIZED,
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
            'success': None,
            'fail': None,
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
        assert_message = assert_message + ' logout'
        super().base_test_get(response=response, success_fail=success_fail, assert_message=assert_message)

    def base_test_post(self, *, response, success_fail, assert_message=''):
        assert_message = assert_message + ' logout'
        super().base_test_post(response=response, success_fail=success_fail, assert_message=assert_message)

        if success_fail == 'success':
            pass
            # TODO check that the user is offline
        elif success_fail == 'fail':
            pass
            # TODO redirect - ? (begin)
            # self.assertEquals(response.url,
            #                   self.response_url_expected['post'][success_fail],
            #                   assert_message + ' response.url')
            # TODO redirect - ? (end)
            # TODO check that the user is online

    def base_test_put(self, *, response, success_fail, assert_message=''):
        assert_message = assert_message + ' logout'
        super().base_test_put(response=response, success_fail=success_fail, assert_message=assert_message)

    def base_test_delete(self, *, response, success_fail, assert_message=''):
        assert_message = assert_message + ' logout'
        super().base_test_delete(response=response, success_fail=success_fail, assert_message=assert_message)

    # ======================================================================
