import requests
import threading

def send_test_email(i):
    res = requests.post("http://localhost:5000/send-email", json={
        "to": "test@example.com",
        "subject": f"Test {i}",
        "body": "Stress test email."
    })
    print(f"#{i} - {res.status_code}: {res.json()}")

threads = []
for i in range(20): 
    t = threading.Thread(target=send_test_email, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
