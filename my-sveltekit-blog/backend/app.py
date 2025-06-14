from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail
from tasks import send_email

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'a7c19b0407d4f3'
app.config['MAIL_PASSWORD'] = '5ba9e78a1b86bf'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.get_json()
    to = data.get('to')
    subject = data.get('subject')
    body = data.get('body')

    send_email.delay(to, subject, body)

    return jsonify({"message": "Email has been queued."})

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/", methods=["GET"])
def index():
    return "✅ Flask backend is running!", 200

