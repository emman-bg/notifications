import unittest
from unittest.mock import patch
from app import app
from views import SMSHandler, EmailHandler, NotificationFactory


class SMSHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

    @patch('app.db.session.add')
    @patch('app.db.session.commit')
    def test_send_sms_success(self, mock_commit, mock_add):
        mock_add.return_value = None
        mock_commit.return_value = None

        recipient = "1234567890"
        message = "Test Message"
        sms_handler = SMSHandler()
        response = sms_handler.send_notification(recipient, message)

        self.assertEqual(response[1], 201)

    @patch('app.db.session.add')
    @patch('app.db.session.commit')
    def test_send_sms_missing_fields(self, mock_commit, mock_add):
        mock_add.return_value = None
        mock_commit.return_value = None

        recipient = ""
        message = "Test Message"
        sms_handler = SMSHandler()
        response = sms_handler.send_notification(recipient, message)

        self.assertEqual(response[1], 400)


class EmailHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

    @patch('app.db.session.add')
    @patch('app.db.session.commit')
    def test_send_email_success(self, mock_commit, mock_add):
        mock_add.return_value = None
        mock_commit.return_value = None

        recipient = "test@gmail.com"
        message = "Test Message"
        email_handler = EmailHandler()
        response = email_handler.send_notification(recipient, message)

        self.assertEqual(response[1], 201)

    @patch('app.db.session.add')
    @patch('app.db.session.commit')
    def test_send_email_missing_fields(self, mock_commit, mock_add):
        mock_add.return_value = None
        mock_commit.return_value = None

        recipient = ""
        message = "Test Message"
        email_handler = EmailHandler()
        response = email_handler.send_notification(recipient, message)

        self.assertEqual(response[1], 400)


class NotificationFactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

    @patch('app.db.session.add')
    @patch('app.db.session.commit')
    def test_notification_factory(self, mock_commit, mock_add):
        mock_add.return_value = None
        mock_commit.return_value = None

        recipient = "1234567890"
        message = "Test message!"
        data_type = "sms"

        handler = NotificationFactory.get_handler(data_type)
        response = handler.send_notification(recipient, message)

        self.assertEqual(response[1], 201)