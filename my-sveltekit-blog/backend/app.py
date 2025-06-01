from flask_cors import CORS
from flask import Flask, request, jsonify
from tasks import send_email

app = Flask(__name__)
CORS(app)

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
