from . import CommonViewsTestCase
from .base import BaseRegistrationViewsTestCase

from ...models import User

from rest_framework.exceptions import ErrorDetail


# Create your tests here.
class RegistrationViewsTestCase(CommonViewsTestCase):
    registered_user = {
        'username': 'username_000',
        'password': 'password_000',
    }

    base_action_test_case = BaseRegistrationViewsTestCase

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

        data_post = self.registered_user.copy()
        data_post['username'] = data_post['username'] + '_another'
        data_post['password'] = data_post['password'] + '_another'

        action = self.base_action_test_case(data_post)
        client, response = action.post(client=None)
        action.data_expected['post'][success_fail] = data_post.copy()
        action.data_expected['post'][success_fail]['last_login'] = None
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

        count_users_expected = 2
        count_users = User.objects.count()
        self.assertEquals(count_users, count_users_expected)

        user = User.objects.all()[count_users-1]
        for field in data_post.keys():
            if field != 'password':
                self.assertEquals(getattr(user, field), data_post[field])
            else:
                self.assertNotEquals(getattr(user, field), data_post[field])
                self.assertEquals(user.check_password(data_post[field]), True)

    # ======================================================================
    # fail
    # ======================================================================

    # ----- POST -----

    def test_post_user_exists_fail(self):
        success_fail = 'fail'

        data_post = self.registered_user.copy()
        data_post['password'] = data_post['password'] + '_another'

        action = self.base_action_test_case(data_post)
        client, response = action.post(client=None)
        # action.data_expected['post'][success_fail] = {
        #     'username': ['A user with that username already exists.']
        # }
        action.data_expected['post'][success_fail] = {
            'username': [ErrorDetail(string='A user with that username already exists.', code='unique')]
        }
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

        count_users_expected = 1
        count_users = User.objects.count()
        self.assertEquals(count_users, count_users_expected)

    def test_post_data_out_is_none_fail(self):
        success_fail = 'fail'

        data_post = None

        action = self.base_action_test_case(data_post)
        client, response = action.post(client=None)
        # action.data_expected['post'][success_fail] = {
        #     'username': ['This field is required.'],
        #     'password': ['This field is required.']
        # }
        action.data_expected['post'][success_fail] = {
            'username': [ErrorDetail(string='This field is required.', code='required')],
            'password': [ErrorDetail(string='This field is required.', code='required')]
        }
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

        count_users_expected = 1
        count_users = User.objects.count()
        self.assertEquals(count_users, count_users_expected)

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
