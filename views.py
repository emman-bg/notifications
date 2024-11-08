from flask import jsonify
import re


def validate_phone_number(phone):
    pattern = r"^\+?[1-9]\d{1,14}$"
    return bool(re.match(pattern, phone))

def validate_email_address(email):
    pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

class NotificationFactory:
    def get_handler(data_type):
        if data_type == 'sms':
            return SMSHandler()
        elif data_type == 'email':
            return EmailHandler()
        else:
            raise ValueError

class NotificationHandler:
    def send_notification(self, recipient, message):
        from app import db
        from models import Notification

        if not recipient:
            return jsonify({"error": "Recipient is required."}), 400

        if not message:
            return jsonify({"error": "Message is required."}), 400

        if isinstance(self, SMSHandler):
            if not validate_phone_number(recipient):
                return jsonify({"error": "Invalid phone number"}), 40

        if isinstance(self, EmailHandler):
            if not validate_email_address(recipient):
                return jsonify({"error": "Invalid email"}), 400


        new_sms = Notification(recipient=recipient, message=message)

        db.session.add(new_sms)
        db.session.commit()

        return jsonify(f'{new_sms.message}'), 201


class SMSHandler(NotificationHandler):
    def send_notification(_, recipient, message):
        return super().send_notification(recipient, message)


class EmailHandler(NotificationHandler):
    def send_notification(_, recipient, message):
        return super().send_notification(recipient, message)