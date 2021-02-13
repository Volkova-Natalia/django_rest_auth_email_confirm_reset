from . import CommonViewsTestCase
from .base import BaseLogoutViewsTestCase


# Create your tests here.
class LogoutViewsTestCase(CommonViewsTestCase):
    registered_user = {
        'email': 'email_000@mail.com',
        'password': 'password_000',
    }

    base_action_test_case = BaseLogoutViewsTestCase

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

    # ----- POST -----

    def test_post_success(self):
        success_fail = 'success'

        action = self.base_action_test_case(user=self.registered_user)
        client, client_login = action.client_login(client=None, user=self.registered_user)
        client, response = action.post(client=client)
        client, client_logout = action.client_logout(client=None, user=self.registered_user)
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    # ======================================================================
    # fail
    # ======================================================================

    # ----- POST -----

    def test_post_401_fail(self):
        success_fail = 'fail'

        action = self.base_action_test_case(user=self.registered_user)
        client, response = action.post(client=None)
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    # ----- GET -----

    def test_get_fail(self):
        method = 'get'
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
