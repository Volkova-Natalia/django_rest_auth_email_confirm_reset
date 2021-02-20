from django.test import TestCase

from .registration import RegistrationIntegrationTestCase
from .login import LoginIntegrationTestCase
from .logout import LogoutIntegrationTestCase
from .auth_info import AuthInfoIntegrationTestCase
from .confirmation import ConfirmationIntegrationTestCase
from .password_reset import PasswordResetIntegrationTestCase
from .password_reset_confirmation import PasswordResetConfirmationIntegrationTestCase


# Create your tests here.
class IntegrationTestCase(TestCase):
    RegistrationTestCase = RegistrationIntegrationTestCase
    LoginTestCase = LoginIntegrationTestCase
    LogoutTestCase = LogoutIntegrationTestCase
    AuthInfoTestCase = AuthInfoIntegrationTestCase
    ConfirmationTestCase = ConfirmationIntegrationTestCase
    PasswordResetTestCase = PasswordResetIntegrationTestCase
    PasswordResetConfirmationTestCase = PasswordResetConfirmationIntegrationTestCase

    test_user = {
        'email': 'email_test@test-mail.com',
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
        cls.confirmation = cls.ConfirmationTestCase(user=cls.test_user)
        cls.confirmation.setUpTestData()
        cls.password_reset = cls.PasswordResetTestCase(user=cls.test_user)
        cls.password_reset.setUpTestData()
        cls.password_reset_confirmation = cls.PasswordResetConfirmationTestCase(user=cls.test_user)
        cls.password_reset_confirmation.setUpTestData()

    def setUp(self):
        super().setUp()
        self.registration.setUp()
        self.login.setUp()
        self.logout.setUp()
        self.auth_info.setUp()
        self.confirmation.setUp()
        self.password_reset.setUp()
        self.password_reset_confirmation.setUp()

    def tearDown(self):
        self.registration.tearDown()
        self.login.tearDown()
        self.logout.tearDown()
        self.auth_info.tearDown()
        self.confirmation.tearDown()
        self.password_reset.tearDown()
        self.password_reset_confirmation.tearDown()
        super().tearDown()

    # ======================================================================
    # success
    # ======================================================================

    def test_registration_confirmation_login_logout_password_reset_login_logout_success(self):
        client = None

        client = self.auth_info.execute(client=client, is_authenticated=False)
        self.auth_info.test()

        client = self.registration.execute(client=client)
        self.registration.test()

        client = self.auth_info.execute(client=client, is_authenticated=False)
        self.auth_info.test()


        client = self.confirmation.execute(client=client)
        self.confirmation.test()

        client = self.auth_info.execute(client=client, is_authenticated=True)
        self.auth_info.test()


        client = self.logout.execute(client=client)
        self.logout.test()

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


        client = self.password_reset.execute(client=client)
        self.password_reset.test()

        client = self.auth_info.execute(client=client, is_authenticated=False)
        self.auth_info.test()


        client = self.password_reset_confirmation.execute(client=client)
        self.password_reset_confirmation.test()

        client = self.auth_info.execute(client=client, is_authenticated=True)
        self.auth_info.test()


        client = self.logout.execute(client=client)
        self.logout.test()

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
