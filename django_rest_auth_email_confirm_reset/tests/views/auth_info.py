from . import CommonViewsTestCase
from .base import BaseAuthInfoViewsTestCase


# Create your tests here.
class AuthInfoViewsTestCase(CommonViewsTestCase):
    registered_user = {
        'email': 'email_000@test-mail.com',
        'password': 'password_000',
    }

    base_action_test_case = BaseAuthInfoViewsTestCase

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        self.create_user(user=self.registered_user)
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================
    # success
    # ======================================================================

    # ----- GET -----

    def test_get_authenticated_success(self):
        success_fail = 'success'

        data_expected = {
            'is_authenticated': True
        }

        action = self.base_action_test_case(user=self.registered_user)
        client, client_login = action.client_login(client=None, user=self.registered_user)
        client, response = action.get(client=client)
        action.data_expected['get'][success_fail] = data_expected
        action.base_test_get(response=response, success_fail=success_fail, assert_message='views')

    def test_get_not_authenticated_success(self):
        success_fail = 'success'

        data_expected = {
            'is_authenticated': False
        }

        action = self.base_action_test_case(user=None)
        client = None
        client, response = action.get(client=client)
        action.data_expected['get'][success_fail] = data_expected
        action.base_test_get(response=response, success_fail=success_fail, assert_message='views')

    # ======================================================================
    # fail
    # ======================================================================

    # ----- GET -----

    # ----- POST -----

    def test_post_fail(self):
        method = 'post'
        self.base_test_405_fail(method=method)

    # ----- PUT -----

    def test_put_fail(self):
        method = 'put'
        self.base_test_405_fail(method=method)

    # ----- DELETE -----

    def test_delete_fail(self):
        method = 'delete'
        self.base_test_405_fail(method=method)

    # ======================================================================
