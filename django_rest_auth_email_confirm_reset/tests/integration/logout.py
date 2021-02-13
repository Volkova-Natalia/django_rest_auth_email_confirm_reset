from ..views.base import BaseLogoutViewsTestCase


# Create your tests here.
class LogoutIntegrationTestCase(BaseLogoutViewsTestCase):

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
        self.base_test_post(response=response, success_fail=success_fail, assert_message='integration')

        return client

    # ======================================================================

    def test(self):
        assert_message = 'integration logout'
        pass
        # TODO

    # ======================================================================
