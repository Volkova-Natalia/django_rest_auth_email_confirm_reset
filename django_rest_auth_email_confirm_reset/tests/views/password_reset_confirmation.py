from . import CommonViewsTestCase
from .base import BasePasswordResetConfirmationViewsTestCase
from .base import BasePasswordResetViewsTestCase

from rest_framework.exceptions import ErrorDetail


# Create your tests here.
class PasswordResetConfirmationViewsTestCase(CommonViewsTestCase):
    registered_user = {
        'email': 'email_000@test-mail.com',
        'password': 'password_000',
    }

    base_action_test_case = BasePasswordResetConfirmationViewsTestCase

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

    def reset_password(self):
        reset_password = BasePasswordResetViewsTestCase(self.registered_user)
        client, response = reset_password.post(client=None)
        return client

    # ======================================================================
    # success
    # ======================================================================

    # ----- PUT -----

    def test_put_success(self):
        success_fail = 'success'
        new_password = self.registered_user['password'] + '_new'

        client = self.reset_password()
        action = self.base_action_test_case(user=self.registered_user.copy())
        action.base_test_put_success__password_fail(success_fail=success_fail, new_password=new_password, client=client)

    # ======================================================================
    # fail
    # ======================================================================

    # ----- PUT -----

    def test_put_link_is_invalid_fail(self):
        method = 'put'
        success_fail = 'fail'
        new_password = self.registered_user['password'] + '_new'

        client = self.reset_password()
        action = self.base_action_test_case(user=self.registered_user.copy())
        action.user['password'] = new_password
        action.data_expected[method][success_fail] = {
            'error': 'Password reset confirmation link is invalid!'
        }

        confirmation_link = action.get_confirmation_link()
        confirmation_args = action.get_confirmation_args(confirmation_link=confirmation_link)
        incorrect_confirmation_args = confirmation_args.copy()
        token_last_symbol = confirmation_args['token'][-1]
        if token_last_symbol == 'a':
            incorrect_token_last_symbol = 'b'
        else:
            incorrect_token_last_symbol = 'a'
        incorrect_confirmation_args['token'] = (confirmation_args['token'][:-1] + incorrect_token_last_symbol)
        action.set_url(uidb64=confirmation_args['uidb64'], token=incorrect_confirmation_args['token'])

        client, response = action.put(client=client)
        action.base_test_put(response=response, success_fail=success_fail, assert_message='views')

    def test_put_password_required_fail(self):
        method = 'put'
        success_fail = 'fail'
        new_password = "deleted_field"

        client = self.reset_password()
        action = self.base_action_test_case(user=self.registered_user.copy())
        del action.user['password']
        action.data_expected[method][success_fail] = {
            # 'password': [ErrorDetail(string='This field is required.', code='required')]
            'detail': ErrorDetail(string='JSON parse error - Expecting value: line 1 column 1 (char 0)',
                                  code='parse_error')
        }
        action.base_test_put_success__password_fail(success_fail=success_fail, new_password=new_password, client=client)

    def test_put_password_null_fail(self):
        method = 'put'
        success_fail = 'fail'
        new_password = None

        client = self.reset_password()
        action = self.base_action_test_case(user=self.registered_user.copy())
        action.data_expected[method][success_fail] = {
            'password': [ErrorDetail(string='This field may not be null.', code='null')]
        }
        action.base_test_put_success__password_fail(success_fail=success_fail, new_password=new_password, client=client)

    def test_put_password_blank_fail(self):
        method = 'put'
        success_fail = 'fail'
        new_password = ""

        client = self.reset_password()
        action = self.base_action_test_case(user=self.registered_user.copy())
        action.data_expected[method][success_fail] = {
            'password': [ErrorDetail(string='This field may not be blank.', code='blank')]
        }
        action.base_test_put_success__password_fail(success_fail=success_fail, new_password=new_password, client=client)

    # ----- GET -----

    def test_get_fail(self):
        method = 'get'
        self.base_test_405_fail(method=method)

    # ----- POST -----

    def test_post_fail(self):
        method = 'post'
        self.base_test_405_fail(method=method)

    # ----- DELETE -----

    def test_delete_fail(self):
        method = 'delete'
        self.base_test_405_fail(method=method)

    # ======================================================================
