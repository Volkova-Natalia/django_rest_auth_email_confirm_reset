from django.test import TestCase
from django.test.client import Client

from ....utils import validate_argument


# Create your tests here.
class BaseViewsTestCase(TestCase):
    content_type = 'application/json'

    user = None

    url = None

    status_code_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    data_expected = {
        'get': {
            'success': None,
            'fail': None,
        },
        'post': {
            'success': None,
            'fail': None,
        }
    }

    # ======================================================================

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    @validate_argument(name_argument='method', allowed_argument_values=['get', 'post', 'put', 'delete'])
    def method(self, *, method):
        return eval('self.' + method)

    @validate_argument(name_argument='method', allowed_argument_values=['get', 'post', 'put', 'delete'])
    def _client_method(self, *, method, client=None, url='', data=None):
        if not client:
            client = Client()
        response = eval('client.' + method)(
            path=url,
            data=data,
            content_type=self.content_type,
            HTTP_ACCEPT=self.content_type,
        )
        return client, response

    def get(self, *, client=None, url='', data=None):
        method = 'get'
        return self._client_method(method=method, client=client, url=url, data=data)

    def post(self, *, client=None, url='', data=None):
        method = 'post'
        return self._client_method(method=method, client=client, url=url, data=data)

    def put(self, *, client=None, url='', data=None):
        method = 'put'
        return self._client_method(method=method, client=client, url=url, data=data)

    def delete(self, *, client=None, url='', data=None):
        method = 'delete'
        return self._client_method(method=method, client=client, url=url, data=data)

    # ======================================================================

    @staticmethod
    def client_login(client=None, user={'username': '', 'password': ''}):
        if not client:
            client = Client()
        login = client.login(username=user['username'], password=user['password'])
        return client, login

    @staticmethod
    def client_logout(client=None, user={'username': '', 'password': ''}):
        if not client:
            client = Client()
        logout = client.logout()
        return client, logout

    # ======================================================================

    def _base_test_status_code(self, *, response, method, success_fail, assert_message=''):
        self.assertEquals(response.status_code,
                          self.status_code_expected[method][success_fail],
                          assert_message + ' test status_code')

    def _base_test_data(self, *, response, method, success_fail, assert_message=''):
        try:
            response_data = response.data
        except (AttributeError, NameError, TypeError, ValueError, Exception):
            response_data = None
        self.assertEquals(response_data,
                          self.data_expected[method][success_fail],
                          assert_message + ' test data')

    # ======================================================================

    @validate_argument(name_argument='method', allowed_argument_values=['get', 'post', 'put', 'delete'])
    def base_test_method(self, *, method):
        return eval('self.base_test_' + method)

    def base_test_get(self, *, response, success_fail, assert_message=''):
        method = 'get'
        assert_message = ' '.join([assert_message, success_fail, method.upper()])
        self._base_test_status_code(response=response, method=method, success_fail=success_fail, assert_message=assert_message)
        self._base_test_data(response=response, method=method, success_fail=success_fail, assert_message=assert_message)

    def base_test_post(self, *, response, success_fail, assert_message=''):
        method = 'post'
        assert_message = ' '.join([assert_message, success_fail, method.upper()])
        self._base_test_status_code(response=response, method=method, success_fail=success_fail, assert_message=assert_message)
        self._base_test_data(response=response, method=method, success_fail=success_fail, assert_message=assert_message)

    def base_test_put(self, *, response, success_fail, assert_message=''):
        method = 'put'
        assert_message = ' '.join([assert_message, success_fail, method.upper()])
        self._base_test_status_code(response=response, method=method, success_fail=success_fail, assert_message=assert_message)
        self._base_test_data(response=response, method=method, success_fail=success_fail, assert_message=assert_message)

    def base_test_delete(self, *, response, success_fail, assert_message=''):
        method = 'delete'
        assert_message = ' '.join([assert_message, success_fail, method.upper()])
        self._base_test_status_code(response=response, method=method, success_fail=success_fail, assert_message=assert_message)
        self._base_test_data(response=response, method=method, success_fail=success_fail, assert_message=assert_message)

    # ======================================================================
