from ..views.base import BaseAuthInfoViewsTestCase


# Create your tests here.
class AuthInfoIntegrationTestCase(BaseAuthInfoViewsTestCase):

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    def execute(self, *, client=None, is_authenticated=False):
        success_fail = 'success'

        client, response = self.get(client=client)
        self.data_expected['get'][success_fail] = {
            'is_authenticated': is_authenticated
        }
        self.base_test_get(response=response, success_fail=success_fail, assert_message='integration')

        return client

    # ======================================================================

    def test(self):
        assert_message = 'integration auth_info'
        pass
        # TODO

    # ======================================================================
