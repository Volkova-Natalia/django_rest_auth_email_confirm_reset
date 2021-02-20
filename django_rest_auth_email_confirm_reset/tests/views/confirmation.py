from . import CommonViewsTestCase
from .base import BaseConfirmationViewsTestCase
from .base import BaseRegistrationViewsTestCase


# Create your tests here.
class ConfirmationViewsTestCase(CommonViewsTestCase):
    registered_user = {
        'email': 'email_000@test-mail.com',
        'password': 'password_000',
    }

    base_action_test_case = BaseConfirmationViewsTestCase

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

    def register_another_user(self):
        data_post = self.registered_user.copy()
        pos_at_sign = data_post['email'].find('@')
        data_post['email'] = data_post['email'][:pos_at_sign] + '_another' + data_post['email'][pos_at_sign:]
        data_post['password'] = data_post['password'] + '_another'

        registration = BaseRegistrationViewsTestCase(data_post)
        client, response = registration.post(client=None)

        another_user = data_post.copy()
        return client, another_user

    # ======================================================================
    # success
    # ======================================================================

    # ----- POST -----

    def test_post_success(self):
        method = 'post'
        success_fail = 'success'

        client, another_user = self.register_another_user()
        action = self.base_action_test_case(user=another_user)

        confirmation_link = action.get_confirmation_link()
        confirmation_args = action.get_confirmation_args(confirmation_link=confirmation_link)
        action.set_url(uidb64=confirmation_args['uidb64'], token=confirmation_args['token'])

        client, response = action.post(client=client)
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    # ======================================================================
    # fail
    # ======================================================================

    # ----- POST -----

    def test_post_link_is_invalid_fail(self):
        method = 'post'
        success_fail = 'fail'

        client, another_user = self.register_another_user()
        action = self.base_action_test_case(user=another_user)

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

        client, response = action.post(client=client)
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    def test_post_one_time_link_fail(self):
        """
        You cant not use the link twice.
        """
        method = 'post'
        success_fail = 'fail'

        client, another_user = self.register_another_user()
        action = self.base_action_test_case(user=another_user)

        confirmation_link = action.get_confirmation_link()
        confirmation_args = action.get_confirmation_args(confirmation_link=confirmation_link)
        action.set_url(uidb64=confirmation_args['uidb64'], token=confirmation_args['token'])

        client, response = action.post(client=client)
        success_fail = 'success'
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')
        client, response = action.post(client=client)
        success_fail = 'fail'
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
