from celery import Celery
from flask_mail import Message, Mail
from config import *

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

def make_mail():
    mail = Mail()
    mail.init_app({
        "MAIL_SERVER": MAIL_SERVER,
        "MAIL_PORT": MAIL_PORT,
        "MAIL_USERNAME": MAIL_USERNAME,
        "MAIL_PASSWORD": MAIL_PASSWORD,
        "MAIL_USE_TLS": MAIL_USE_TLS,
        "MAIL_DEFAULT_SENDER": MAIL_DEFAULT_SENDER
    })
    return mail

@celery.task
def send_email(to, subject, body):
    mail = make_mail()
    msg = Message(subject, recipients=[to], body=body)
    with mail.connect() as conn:
        conn.send(msg)
