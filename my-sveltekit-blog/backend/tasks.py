from celery import Celery
from flask_mail import Message, Mail
from flask import Flask
from config import *

# ✅ Khởi tạo Flask app (cần để Flask-Mail hoạt động)
flask_app = Flask(__name__)
flask_app.config.update(
    MAIL_SERVER=MAIL_SERVER,
    MAIL_PORT=MAIL_PORT,
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_USE_TLS=MAIL_USE_TLS,
    MAIL_DEFAULT_SENDER=MAIL_DEFAULT_SENDER
)

# ✅ Khởi tạo Celery
celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

# ✅ Khởi tạo Flask-Mail với app
mail = Mail(flask_app)

@celery.task
def send_email(to, subject, body):
    with flask_app.app_context():  # đảm bảo có context Flask để gửi email
        msg = Message(subject, recipients=[to], body=body)
        mail.send(msg)
