from django.test import TestCase
from ...utils import ClassWithAbstractVariables
from ...models import User

from ...utils import validate_argument


# Create your tests here.
class CommonViewsTestCase(TestCase,
                          ClassWithAbstractVariables):

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    __required_class_variables = [
        "registered_user",          # example:   registered_user = {
                                    #                'email': 'email_000@mail.com',
                                    #                'password': 'password_000',
                                    #            }
        "base_action_test_case",    # example:   BaseAuthInfoViewsTestCase
    ]

    @classmethod
    def __init_subclass__(cls):
        super().__thisclass__.check_required_class_variables(child=cls)
        super().__init_subclass__()

    # ======================================================================

    @staticmethod
    def create_user(*, user=None):
        if user:
            user = User.objects.create_user(
                email=user['email'],
                password=user['password'],
            )
            user.save()
        return user

    # ======================================================================

    @validate_argument(name_argument='method', allowed_argument_values=['get', 'post', 'put', 'delete'])
    def base_test_405_fail(self, *, method):
        success_fail = 'fail'

        action = self.base_action_test_case(user=self.registered_user)
        client, response = action.method(method=method)(client=None)
        action.base_test_method(method=method)(response=response, success_fail=success_fail, assert_message='views')

    # ======================================================================
