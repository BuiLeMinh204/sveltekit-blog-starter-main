from celery import Celery
from flask import Flask
from flask_mail import Mail, Message
from config import *
import os

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")

celery = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

flask_app = Flask(__name__)
flask_app.config.update(
    MAIL_SERVER=MAIL_SERVER,
    MAIL_PORT=MAIL_PORT,
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_USE_TLS=MAIL_USE_TLS,
    MAIL_DEFAULT_SENDER=MAIL_DEFAULT_SENDER
)

mail = Mail(flask_app)

@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 5})
def send_email(self, to, subject, body):
    with flask_app.app_context():
        print(f"📨 Sending email to {to}...")
        msg = Message(subject=subject, recipients=[to], body=body)
        mail.send(msg)
        print("✅ Email sent successfully")
