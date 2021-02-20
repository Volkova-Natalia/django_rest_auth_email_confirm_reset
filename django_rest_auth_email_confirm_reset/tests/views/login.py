from . import CommonViewsTestCase
from .base import BaseLoginViewsTestCase

from rest_framework.exceptions import ErrorDetail


# Create your tests here.
class LoginViewsTestCase(CommonViewsTestCase):
    registered_user = {
        'email': 'email_000@test-mail.com',
        'password': 'password_000',
    }

    base_action_test_case = BaseLoginViewsTestCase

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

        action = self.base_action_test_case(data_post)
        client, response = action.post(client=None)
        action.data_expected['post'][success_fail] = data_post.copy()
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    # ======================================================================
    # fail
    # ======================================================================

    # ----- POST -----

    # ----- field_is_not_correct -----

    def _test_post_field_is_not_correct_fail(self, *, field_is_not_correct=[]):
        success_fail = 'fail'

        """
            data_post = self.registered_user
            EXPECT
            fields from field_is_not_correct (suffix '_another' is added to each field)
        """
        data_post = self.registered_user.copy()
        for field in field_is_not_correct:
            if field == 'email':
                pos_at_sign = data_post[field].find('@')
                data_post[field] = data_post[field][:pos_at_sign] + '_another' + data_post[field][pos_at_sign:]
            else:
                data_post[field] = data_post[field] + '_another'

        action = self.base_action_test_case(data_post)
        client, response = action.post(client=None)
        # action.data_expected['post'][success_fail] = {
        #     'non_field_errors': ['user with this email and password was not found.']
        # }
        action.data_expected['post'][success_fail] = {
            'non_field_errors': [ErrorDetail(string='user with this email and password was not found.',
                                             code='invalid')]
        }
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    def test_post_email_is_not_correct_fail(self):
        self._test_post_field_is_not_correct_fail(field_is_not_correct=['email'])

    def test_post_password_is_not_correct_fail(self):
        self._test_post_field_is_not_correct_fail(field_is_not_correct=['password'])

    def test_post_email_password_is_not_correct_fail(self):
        self._test_post_field_is_not_correct_fail(field_is_not_correct=['email', 'password'])

    # ----- field_required -----

    def _test_post_field_required_fail(self, *, field_required=[]):
        success_fail = 'fail'

        """
            data_post = self.registered_user
            WITHOUT
            fields from field_required
        """
        data_post = {}
        for field_registered_user in self.registered_user:
            if field_registered_user not in field_required:
                data_post[field_registered_user] = self.registered_user[field_registered_user]

        action = self.base_action_test_case(data_post)
        client, response = action.post(client=None)
        """
            ErrorDetail (code='required')
            IN
            fields from field_required
        """
        action.data_expected['post'][success_fail] = {}
        # for field in field_required:
        #     action.data_expected['post'][success_fail][field] = ['This field is required.']
        for field in field_required:
            action.data_expected['post'][success_fail][field] = [ErrorDetail(string='This field is required.',
                                                                             code='required')]
        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    def test_post_email_required_fail(self):
        self._test_post_field_required_fail(field_required=['email'])

    def test_post_password_required_fail(self):
        self._test_post_field_required_fail(field_required=['password'])

    def test_post_email_password_required_fail(self):
        self._test_post_field_required_fail(field_required=['email', 'password'])

    # ----- data_out_is_none -----

    def test_post_data_out_is_none_fail(self):
        success_fail = 'fail'

        data_post = None

        action = self.base_action_test_case(data_post)
        client, response = action.post(client=None)
        # action.data_expected['post'][success_fail] = {
        #     'email': ['This field is required.'],
        #     'password': ['This field is required.']
        # }
        action.data_expected['post'][success_fail] = {
            'email': [ErrorDetail(string='This field is required.', code='required')],
            'password': [ErrorDetail(string='This field is required.', code='required')]
        }

        action.base_test_post(response=response, success_fail=success_fail, assert_message='views')

    # TODO test ValidationError(
    #                 'This user has been deactivated.'
    #             )

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
