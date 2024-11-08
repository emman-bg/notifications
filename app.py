from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from views import SMSHandler, EmailHandler, NotificationFactory

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notifications.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/send-sms/", methods=['POST'])
def send_sms():
    recipient = request.form.get('recipient')
    message = request.form.get('message')

    return SMSHandler.send_notification(recipient, message)

@app.route("/send-email/", methods=['POST'])
def send_email():
    recipient = request.form.get('recipient')
    message = request.form.get('message')

    return EmailHandler.send_notification(recipient, message)

@app.route("/send-notification/", methods=['POST'])
def send_notification():
    data_type = request.form.get('type')
    recipient = request.form.get('recipient')
    message = request.form.get('message')

    handler = NotificationFactory.get_handler(data_type)

    return handler.send_notification(recipient, message)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)