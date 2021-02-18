from . import BaseViewsTestCase

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from django.urls import reverse

from django.core import mail


# Create your tests here.
class BaseConfirmationViewsTestCase(BaseViewsTestCase):
    end_point_name = 'confirmation'
    user = None

    uidb64 = 'Ab'
    token = 'ab01cd-e2345678f90gh123456i7j8k9l0mno12'
    url_args = [uidb64, token]

    url = reverse(end_point_name, args=url_args)

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
            'success': {
                'message': 'Thank you for your email confirmation. Now you can login your account.'
            },
            'fail': {
                'error': 'Confirmation link is invalid!'
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
        self.set_url(uidb64='Ab', token='ab01cd-e2345678f90gh123456i7j8k9l0mno12')
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    def set_url(self, uidb64, token):
        self.uidb64 = uidb64
        self.token = token
        self.url_args = [self.uidb64, self.token]

        self.url = reverse(self.end_point_name, args=self.url_args)
        return self.url

    def get_confirmation_link(self):
        email_message = mail.outbox[-1].body
        pos_confirmation_link_start = email_message.find(r'http')
        pos_confirmation_link_stop = email_message.rfind(r'/')  # url ends with '/'
        confirmation_link = email_message[pos_confirmation_link_start:pos_confirmation_link_stop+1]
        return confirmation_link

    def get_confirmation_args(self, confirmation_link):
        confirmation_args = {
            'uidb64': None,
            'token': None,
        }
        pos_last_slash = confirmation_link.rfind(r'/')  # url ends with '/'
        _confirmation_link = confirmation_link[:pos_last_slash]     # cut last '/'

        pos_last_slash = _confirmation_link.rfind(r'/')     # '/' before token
        if pos_last_slash >= 0:
            token = _confirmation_link[pos_last_slash+1:]
            _confirmation_link = confirmation_link[:pos_last_slash]     # cut '/' + token
            confirmation_args['token'] = token
            pos_last_slash = _confirmation_link.rfind(r'/')     # '/' before uidb64
            if pos_last_slash >= 0:
                uidb64 = _confirmation_link[pos_last_slash+1:]
                # _confirmation_link = confirmation_link[:pos_last_slash]     # cut '/' + uidb64
                confirmation_args['uidb64'] = uidb64

        return confirmation_args

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
