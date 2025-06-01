from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail
from tasks import send_email

app = Flask(__name__)
CORS(app)

# ✅ Cấu hình email (dùng Mailtrap làm ví dụ)
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'YOUR_MAILTRAP_USERNAME'
app.config['MAIL_PASSWORD'] = 'YOUR_MAILTRAP_PASSWORD'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# ✅ Khởi tạo Flask-Mail (để tasks.py có thể dùng)
mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.get_json()
    to = data.get('to')
    subject = data.get('subject')
    body = data.get('body')

    # ✅ Gửi task cho Celery
    send_email.delay(to, subject, body)

    return jsonify({"message": "Email has been queued."})

if __name__ == '__main__':
    app.run(debug=True)
