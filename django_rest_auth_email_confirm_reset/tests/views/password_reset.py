from . import CommonViewsTestCase
from .base import BasePasswordResetViewsTestCase

from rest_framework.exceptions import ErrorDetail


# Create your tests here.
class PasswordResetViewsTestCase(CommonViewsTestCase):
    registered_user = {
        'email': 'email_000@test-mail.com',
        'password': 'password_000',
    }

    base_action_test_case = BasePasswordResetViewsTestCase

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

        action = self.base_action_test_case(self.registered_user.copy())
        client, response = action.post(client=None)
        action.data_expected['post'][success_fail] = {
            'email': self.registered_user['email']
        }
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    # ======================================================================
    # fail
    # ======================================================================

    # ----- POST -----

    def test_post_email_required_fail(self):
        method = 'post'
        success_fail = 'fail'

        action = self.base_action_test_case(self.registered_user.copy())
        del action.user['email']
        client, response = action.post(client=None)
        action.data_expected[method][success_fail] = {
            'email': [ErrorDetail(string='This field is required.', code='required')]
        }
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    def test_post_email_invalid_fail(self):
        method = 'post'
        success_fail = 'fail'

        action = self.base_action_test_case(self.registered_user.copy())
        action.user['email'] = 'incorrect_email'
        client, response = action.post(client=None)
        action.data_expected[method][success_fail] = {
            'email': [ErrorDetail(string='Enter a valid email address.', code='invalid')]
        }
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    def test_post_email_null_fail(self):
        method = 'post'
        success_fail = 'fail'

        action = self.base_action_test_case(self.registered_user.copy())
        action.user['email'] = None
        client, response = action.post(client=None)
        action.data_expected[method][success_fail] = {
            'email': [ErrorDetail(string='This field may not be null.', code='null')]
        }
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    def test_post_email_blank_fail(self):
        method = 'post'
        success_fail = 'fail'

        action = self.base_action_test_case(self.registered_user.copy())
        action.user['email'] = ''
        client, response = action.post(client=None)
        action.data_expected[method][success_fail] = {
            'email': [ErrorDetail(string='This field may not be blank.', code='blank')]
        }
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    def test_post_user_is_not_exists_fail(self):
        method = 'post'
        success_fail = 'fail'

        action = self.base_action_test_case(self.registered_user.copy())
        pos_at_sign = action.user['email'].find('@')
        action.user['email'] = action.user['email'][:pos_at_sign] + '_another' + action.user['email'][pos_at_sign:]
        client, response = action.post(client=None)
        action.data_expected[method][success_fail] = {
            'email': [ErrorDetail(string='user with this email was not found.', code='invalid')]
        }
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
