from ..views.base import BasePasswordResetViewsTestCase


# Create your tests here.
class PasswordResetIntegrationTestCase(BasePasswordResetViewsTestCase):

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    def execute(self, *, client=None):
        success_fail = 'success'

        client, response = self.post(client=client)
        self.data_expected['post'][success_fail] = {
            'email': self.user['email']
        }
        self.base_test_post(response=response, success_fail=success_fail, assert_message='integration')

        return client

    # ======================================================================

    def test(self):
        assert_message = 'integration password_reset'
        pass
        # TODO

    # ======================================================================
