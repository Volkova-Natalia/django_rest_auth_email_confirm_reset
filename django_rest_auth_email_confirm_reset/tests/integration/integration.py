from django.test import TestCase

from .registration import RegistrationIntegrationTestCase
from .login import LoginIntegrationTestCase
from .logout import LogoutIntegrationTestCase
from .auth_info import AuthInfoIntegrationTestCase


# Create your tests here.
class IntegrationTestCase(TestCase):
    RegistrationTestCase = RegistrationIntegrationTestCase
    LoginTestCase = LoginIntegrationTestCase
    LogoutTestCase = LogoutIntegrationTestCase
    AuthInfoTestCase = AuthInfoIntegrationTestCase

    test_user = {
        'username': 'username_test',
        'password': 'password_test',
    }

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.registration = cls.RegistrationTestCase(user=cls.test_user)
        cls.registration.setUpTestData()
        cls.login = cls.LoginTestCase(user=cls.test_user)
        cls.login.setUpTestData()
        cls.logout = cls.LogoutTestCase(user=cls.test_user)
        cls.logout.setUpTestData()
        cls.auth_info = cls.AuthInfoTestCase(user=cls.test_user)
        cls.auth_info.setUpTestData()

    def setUp(self):
        super().setUp()
        self.registration.setUp()
        self.login.setUp()
        self.logout.setUp()
        self.auth_info.setUp()

    def tearDown(self):
        self.registration.tearDown()
        self.login.tearDown()
        self.logout.tearDown()
        self.auth_info.tearDown()
        super().tearDown()

    # ======================================================================
    # success
    # ======================================================================

    def test_registration_login_logout_success(self):
        client = None

        client = self.auth_info.execute(client=client, is_authenticated=False)
        self.auth_info.test()

        client = self.registration.execute(client=client)
        self.registration.test()

        client = self.auth_info.execute(client=client, is_authenticated=False)
        self.auth_info.test()

        client = self.login.execute(client=client)
        self.login.test()

        client = self.auth_info.execute(client=client, is_authenticated=True)
        self.auth_info.test()

        client = self.logout.execute(client=client)
        self.logout.test()

        client = self.auth_info.execute(client=client, is_authenticated=False)
        self.auth_info.test()

    # ======================================================================
    # fail
    # ======================================================================

    # ======================================================================
