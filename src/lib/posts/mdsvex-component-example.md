---
title: "Deliverable 3"
date: "2025-03-06"
updated: "2025-03-06"
categories:
  - "minhbui"
coverImage: "/images/jerry-zhang-ePpaQC2c1xA-unsplash.jpg"
coverWidth: 16
coverHeight: 9
excerpt: Ấn vào để xem thêm ....
---

---
## 5. Triển khai hệ thống

Dưới đây là hướng dẫn cấu hình và khởi động Celery, phù hợp dùng cho tài liệu kỹ thuật, báo cáo hoặc triển khai thực tế:

*5.1. Cài đặt các gói cần thiết*

~~ pip install celery redis ~~

Nếu bạn dùng Flask, cài thêm flask tương ứng.

*5.2. Tạo file tasks.py – định nghĩa tác vụ gửi email*

~~ from celery import Celery ~~

~~ import smtplib ~~

*Khởi tạo Celery với Redis làm broker*

~~ app = Celery('email_tasks', broker='redis://localhost:6379/0') ~~

*5.3. Khởi động Redis*

Redis phải đang chạy để Celery sử dụng làm hàng đợi (Queue):

~~ redis-server ~~

*5.4. Khởi động Celery Worker*

Chạy lệnh sau trong thư mục chứa tasks.py:

~~ celery -A tasks worker --loglevel=info ~~

*5.5. Gọi tác vụ gửi email*

Trong Python, bạn có thể gọi Task như sau:

~~ from tasks import send_email ~~

~~ send_email.delay("someone@example.com", "Test Email", "This is a test message.") ~~

.delay() là phương thức để đẩy tác vụ vào hàng đợi Celery (gửi bất đồng bộ). Những kết quả đạt được khẳng định rằng mô hình kiến trúc và công nghệ lựa chọn trong dự án là hoàn toàn phù hợp, có thể triển khai thực tế cho các cơ sở khám chữa bệnh quy mô vừa và nhỏ.

## 6. Danh Sách Hoàn Thành Và Chưa Hoàn Thành.

*6.1. Hoàn Thành*

•	Thiết kế giao diện người dùng (UI) cho gửi và nhận email.

•	Cấu hình SMTP để gửi email (Gmail, Mailgun, hoặc dịch vụ SMTP khác).

•	Tạo API gửi email (sử dụng Node.js/Express hoặc framework khác).

•	Tích hợp frontend với backend để gửi email qua giao diện.

•	Kiểm thử chức năng gửi email (thành công & lỗi).

•	Hiển thị danh sách email đã gửi trên giao diện.

*6.2. Chưa Hoàn Thành*

•	Chưa upload tệp đính kèm từ local lên đám mây (cloud).

•	Các tệp vẫn đang nằm trên máy local hoặc chỉ lưu tạm thời trên server.

•	Chưa làm giao diện quản lý tệp đính kèm (xem, tải lại, xoá).

•	Chưa tối ưu bảo mật gửi email (DKIM, SPF, TLS...).

•	Chưa log chi tiết trạng thái gửi (queued, sent, failed, retry...).

•	Chưa triển khai trên server thật hoặc đám mây (deployment).

## 7. Kết Luận Và Đánh Giá

*7.1. Kết Luận*

Dự án email hiện đã hoàn thành phần lớn các chức năng cốt lõi phục vụ mục tiêu gửi email từ giao diện người dùng:

•	Người dùng có thể đăng nhập, gửi email, đính kèm tệp và theo dõi lịch sử gửi.

•	Hệ thống backend đã hoạt động ổn định với API gửi email, tích hợp SMTP.

Tuy nhiên, dự án vẫn còn những thiếu sót quan trọng, đặc biệt liên quan đến quản lý tệp đính kèm và lưu trữ đám mây, khiến việc mở rộng, triển khai thực tế hoặc đảm bảo dữ liệu lâu dài còn hạn chế.

*7.2. Đánh giá tổng thể*

| Tiêu chí                          | Đánh giá                                 |
|----------------------------------|------------------------------------------|
| Chức năng gửi email              | Hoàn chỉnh                               |
| UI/UX người dùng                 | Tạm ổn *(cần tinh chỉnh thêm)*           |
| Bảo mật và xác thực              | Có cơ bản, cần nâng cao                   |
| Quản lý file đính kèm            | Thiếu upload cloud                       |
| Lưu trữ và mở rộng dữ liệu       | Chưa có giải pháp lâu dài                |
| Độ hoàn thiện để triển khai      | Cần cải thiện và bổ sung                 |


*7.3. Đề xuất cải thiện tiếp theo*

1.	Xác minh email đăng ký bằng email token (tăng bảo mật).

2.	Triển khai logging nâng cao: theo dõi thất bại và retry.

3.	Chuẩn bị triển khai thực tế (production): dùng Docker, CI/CD, server hosting.
