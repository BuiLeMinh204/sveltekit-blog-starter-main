CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

MAIL_SERVER = 'smtp.mailtrap.io'
MAIL_PORT = 587
MAIL_USERNAME = 'your_mailtrap_username'
MAIL_PASSWORD = 'your_mailtrap_password'
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_DEFAULT_SENDER = 'noreply@example.com'
