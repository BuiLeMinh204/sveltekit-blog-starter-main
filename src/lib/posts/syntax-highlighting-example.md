---
title: "Deliverable 4"
date: "2025-06-03"
updated: "2025-06-03"
categories:
  - "sveltekit"
  - "web"
  - "css"
  - "markdown"
coverImage: "/images/linus-nylund-Q5QspluNZmM-unsplash.jpg"
coverWidth: 16
coverHeight: 9
excerpt: This post shows you how syntax highlighting works here.
---

---
## 1. GIỚI THIỆU ĐỀ TÀI

*1.1. Mục tiêu*

• Xây dựng hệ thống gửi email tự động phục vụ cho các nhu cầu như: thông báo, xác nhận tài khoản, báo cáo, marketing,...

•	Quản lý danh sách người nhận, nội dung email và lịch gửi một cách dễ dàng và hiệu quả.

•	Tích hợp tính năng gửi email hàng loạt (bulk email) và cá nhân hóa nội dung (ví dụ: chèn tên người nhận).

•	Áp dụng kiến thức về lập trình Java, mạng, giao thức SMTP, cơ sở dữ liệu và bảo mật vào một ứng dụng thực tế.

•	Cung cấp giao diện trực quan, dễ sử dụng để người dùng có thể thao tác nhanh chóng.

•	Hỗ trợ các chức năng nâng cao như: tạo mẫu email (template), lên lịch gửi (schedule), thống kê email đã gửi/thành công/lỗi,...

*1.2. Lý do chọn đề tài*

•	Email là một công cụ giao tiếp không thể thiếu trong môi trường làm việc hiện đại, đặc biệt là trong doanh nghiệp, trường học, dịch vụ khách hàng,...

•	Nhiều tổ chức cần tự động hóa việc gửi email để tiết kiệm thời gian, giảm sai sót, nâng cao hiệu quả công việc.

•	Việc xây dựng ứng dụng gửi email giúp áp dụng kiến thức lý thuyết vào bài toán thực tế, nâng cao kỹ năng lập trình và hiểu biết về các giao thức truyền thông như SMTP, TLS,...

•	Tính ứng dụng cao: phần mềm có thể được sử dụng trong nhiều lĩnh vực như: thương mại điện tử, giáo dục, quản lý nhân sự, tiếp thị, chăm sóc khách hàng,...

•	Tạo nền tảng để phát triển các hệ thống nâng cao hơn như: CRM, hệ thống marketing automation, hệ thống quản lý khách hàng,...

*1.3. Mô tả tổng quan hệ thống*

Hệ thống gửi email tự động là một phần mềm cho phép người dùng quản lý và gửi email đến một hoặc nhiều người nhận một cách hiệu quả và nhanh chóng. Hệ thống được thiết kế để hỗ trợ các nhu cầu thực tế như: gửi thông báo, xác nhận đăng ký, chăm sóc khách hàng, email marketing, hoặc gửi báo cáo định kỳ.

Ứng dụng có giao diện người dùng thân thiện, cho phép người dùng nhập nội dung email, chọn danh sách người nhận, đính kèm tệp và gửi email trực tiếp từ hệ thống thông qua giao thức SMTP. Ngoài ra, hệ thống còn hỗ trợ các tính năng nâng cao như lên lịch gửi, theo dõi trạng thái gửi (đã gửi thành công/thất bại), và quản lý mẫu email.

*Hệ thống bao gồm 2 thành phần chính:*

1.	Giao diện người dùng (User Interface)

o	Cho phép người dùng nhập tiêu đề, nội dung, người nhận, tệp đính kèm.

o	Có thể lựa chọn gửi ngay hoặc lên lịch gửi vào thời điểm định trước.

o	Hiển thị lịch sử gửi email và trạng thái gửi.

2.	Bộ xử lý nghiệp vụ (Business Logic Layer)

o	Kiểm tra định dạng email, xử lý tệp đính kèm, kết nối tới máy chủ SMTP.

o	Gửi email theo đúng lịch trình.

o	Ghi log và trạng thái gửi email vào hệ thống.

Hệ thống sử dụng ngôn ngữ lập trình Java, thư viện JavaMail API để kết nối và gửi email qua giao thức SMTP (ví dụ: Gmail SMTP server). Cơ sở dữ liệu như MySQL hoặc SQLite có thể được tích hợp để lưu trữ thông tin người dùng và lịch sử gửi email.

*1.4. Các công nghệ và thư viện sử dụng*

| Công nghệ                   | Vai trò                                                                 |
|----------------------------|-------------------------------------------------------------------------|
| **Celery**                 | Xử lý tác vụ bất đồng bộ, hỗ trợ phân tán, đảm bảo khả năng chịu lỗi    |
| **Flask**                  | Giao tiếp với client, xử lý logic ban đầu, gửi task đến Celery          |
| **Redis**                  | Làm message broker truyền tải task và/hoặc lưu trữ kết quả task          |
| **Docker**                 | Triển khai các node trong môi trường container hóa                      |
| **Postman / Apache Bench**| Công cụ test API và thực hiện stress test                                |
| **VS Code**                | IDE chính để phát triển mã nguồn                                         |
| **Git + GitHub**           | Quản lý mã nguồn và lưu trữ dự án                                       |


## 2. Kiến trúc hệ thống

*2.1. Kiến trúc tổng thể*

| Thành phần                        | Vai trò                                                                                     |
|----------------------------------|---------------------------------------------------------------------------------------------|
| **Client (Web / Mobile)**        | Gửi yêu cầu HTTP đến server Flask (ví dụ: gửi email, xử lý file, tạo báo cáo...)           |
| **Flask Web API**                | - Nhận yêu cầu từ client  <br> - Xử lý logic ban đầu  <br> - Gửi task bất đồng bộ đến Celery qua Redis  <br> - Phản hồi ngay cho client |
| **Redis (Message Broker)**       | - Là hàng đợi trung gian truyền task từ Flask đến Celery  <br> - Đảm bảo lưu trữ task tạm thời  <br> - Phân phối task cho các worker |
| **Celery Worker(s)**             | - Nhận task từ Redis và xử lý  <br> - Có thể triển khai nhiều worker song song (có thể trên nhiều máy chủ)  <br> - Trả kết quả nếu cần |
| **Redis (Result Backend)** hoặc **Database** | - Lưu kết quả xử lý task (nếu hệ thống cần theo dõi trạng thái/kết quả)  <br> - Có thể là Redis, PostgreSQL, MongoDB… |
| **Flower / Prometheus (tuỳ chọn)** | - Theo dõi trạng thái worker, task đang chạy, task lỗi, thời gian xử lý...  <br> - Hữu ích cho giám sát và khắc phục sự cố |

*2.2. Vai trò các thành phần chính*

| Thành phần                        | Vai trò chính                                                                                                                                                  |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Client (Web / Mobile)**        | Gửi yêu cầu HTTP đến Flask, ví dụ: gửi email, tạo báo cáo, đăng ký người dùng…                                                                                 |
| **Flask Web API**                | Nhận yêu cầu từ client, kiểm tra dữ liệu, rồi đẩy task sang hàng đợi Celery qua Redis. <br>Flask phản hồi ngay cho client mà không cần đợi task xử lý xong.     |
| **Redis (Message Broker)**       | Là trung gian truyền thông giữa Flask và Celery. <br>Nó xếp hàng các task bất đồng bộ mà Flask gửi đến, để các worker của Celery lấy ra và xử lý.              |
| **Celery Worker**                | Là thành phần xử lý thực tế các task. <br>Worker đọc task từ Redis, xử lý (ví dụ gửi email, resize ảnh...), sau đó trả kết quả nếu cần. <br>Có thể mở rộng theo cụm. |
| **Redis (Result Backend)** hoặc **Database** | Nếu cần lưu lại kết quả task để client kiểm tra sau, <br>Celery có thể lưu vào Redis hoặc hệ quản trị CSDL như PostgreSQL, MongoDB.                         |
| **(Tuỳ chọn) Flower / Prometheus** | Công cụ giám sát để xem task đang chạy, task bị lỗi, thời gian xử lý, <br>worker có đang hoạt động không...                                                  |


## 3. Áp dụng các khái niệm phân tán

*3.1. Fault Tolerance trong Celery*

*1. Cơ chế Fault Tolerance của Celery*

Celery được thiết kế để không phụ thuộc vào một điểm duy nhất và có khả năng khôi phục các tác vụ lỗi một cách linh hoạt. Các cơ chế chính bao gồm:

    a) Task Acknowledgement (ACK)
•	Mỗi tác vụ chỉ được xác nhận hoàn thành khi worker xử lý thành công.

•	Nếu worker chết trước khi gửi ACK, task sẽ không bị mất, mà quay lại hàng đợi (re-queued).


    b) Tự động retry khi lỗi
•	Các task có thể cấu hình để retry khi thất bại

•	Hữu ích trong trường hợp lỗi tạm thời như mất kết nối tới server, timeout, API bị lỗi.

    c) Nhiều worker song song
•	Nhiều worker có thể cùng xử lý task từ hàng đợi → nếu một worker gặp sự cố, các worker còn lại tiếp tục hoạt động bình thường.

•	Worker có thể triển khai trên nhiều máy chủ khác nhau (distributed worker model).

    d) Message broker ổn định
•	Redis hoặc RabbitMQ đều có khả năng persist task và hoạt động ổn định trong môi trường phân tán.

•	Broker có thể thiết lập cluster hoặc failover để tránh single point of failure.

    e) Worker auto-restart
•	Worker có thể được giám sát và khởi động lại tự động bằng các công cụ như systemd, supervisor, docker restart, hoặc orchestrator như Kubernetes.

*2. Minh họa tình huống chịu lỗi*

•	Flask gửi task "send-email" đến Celery qua Redis.

•	Worker A nhận task, nhưng bất ngờ bị kill trước khi gửi email.

•	Task chưa được Accept → Redis sẽ giữ lại task.

•	Worker B (hoặc worker A sau khi restart) sẽ tiếp nhận lại task và tiếp tục xử lý.

*3. Đánh giá*

| Tiêu chí                                      | Đánh giá                                                       |
|----------------------------------------------|----------------------------------------------------------------|
| Mất task khi worker chết                     | Không *(nếu cấu hình đúng)*                                    |
| Khả năng retry khi task lỗi                  | Có, cấu hình linh hoạt                                         |
| Đảm bảo hoạt động khi một node hỏng          | Có                                                             |
| Yêu cầu thêm phần giám sát (monitoring)      | Cần để phát hiện lỗi và tự động restart                        |


 *3.2. Distributed Communication giữa các nút*
 
Celery sử dụng mô hình message queue-based communication thông qua một message broker như RabbitMQ, Redis, Amazon SQS… để thực hiện phân tán công việc:

•	Master process (producer) gửi task đến message broker.

•	Workers (consumer) nhận và xử lý task.

•	Có thể triển khai nhiều worker trên nhiều node vật lý – điều này tạo thành một hệ thống phân tán thật sự.

Celery sử dụng giao thức AMQP hoặc Redis Pub/Sub cho giao tiếp giữa các thành phần – đây là phương thức Asynchronous, Loosely coupled, đảm bảo hiệu suất và mở rộng linh hoạt.

*3.3. Sharding và Replication trong hệ thống Celery*

Dù Celery không có sharding ở cấp độ dữ liệu như database, nhưng ta có thể:
•	Chia cụm (cluster) worker theo queue:

o	Mỗi worker có thể lắng nghe một queue riêng (ví dụ: email_queue, report_queue), xem như một hình thức sharding theo chức năng.

•	Replication:

o	Ta có thể chạy nhiều worker xử lý cùng một queue, để tạo độ dư thừa (redundancy): nếu một worker chết, worker khác tiếp tục xử lý.

o	Dùng chiến lược task routing để kiểm soát dòng công việc theo vùng địa lý hoặc theo mức độ ưu tiên.

Đây là cách Celery mô phỏng Sharding và Replication theo góc nhìn task-level.

*3.4. Logging và Giám sát*

Celery hỗ trợ logging tích hợp và có thể mở rộng với các công cụ giám sát:

•	Flower: Web UI trực quan để theo dõi queue, worker, task, trạng thái (success, retry, failed), thời gian xử lý...

•	Tích hợp Prometheus / Grafana để thu thập metric về số lượng task, độ trễ, hiệu suất, thông qua các exporter.

•	Structured Logging: Dễ dàng tích hợp với các hệ thống log tập trung như ELK Stack (Elasticsearch, Logstash, Kibana) hoặc Sentry cho alert.

 Đây là phần rất quan trọng khi vận hành hệ thống ở môi trường Production.
 
*3.5. Stress Test: Mô phỏng tải và đánh giá hệ thống*

Celery có thể được kiểm tra hiệu năng bằng cách:

•	Viết script để tạo hàng nghìn task đồng thời (ví dụ gửi 10.000 email).

•	Đo đạc:

  o	Thời gian hoàn thành task trung bình.

  o	Tổng số task xử lý được trong 1 phút.

  o	Tỉ lệ lỗi khi tăng số lượng worker / queue.

•	Dùng time, locust, wrk, hoặc custom benchmark script để kiểm tra khả năng mở rộng.

•	Quan sát qua Flower hoặc Prometheus để xác định “điểm nghẽn”.

Kết quả giúp điều chỉnh số lượng worker, cấu hình broker, độ trễ retry, phân phối task tốt hơn.

## 4. Các tính năng tùy chọn

*4.1. Load Balancing (Cân bằng tải)*

Celery không có một load balancer nội tại, nhưng nó tự động phân phối công việc đều cho các Worker nhờ vào message Broker (Redis, RabbitMQ) hoạt động theo cơ chế FIFO hoặc round-robin.

    Cách hoạt động: 
     • Các Worker kết nối vào cùng một hàng đợi (queue).
     • Broker gửi tác vụ cho Worker rảnh sớm nhất hoặc theo thứ tự.
     • Nếu có nhiều hàng đợi (Named queue), bạn có thể điều phối Worker nào xử lý hàng đợi nào – một hình thức Manual Load Partitioning.
     
    Nâng cao:
    • Có thể dùng Prefetch Limit để giới hạn số task một Worker được "giữ tạm" trong bộ nhớ.
    • Kết hợp Celery với Kubernetes hoặc Docker Swarm để tự động Scale Worker theo tải.

    
*4.2. System Recovery sau lỗi*

Celery có khả năng khôi phục hệ thống sau lỗi dựa trên 3 yếu tố:

   1. Tự động Retry task:
      
•	Task có thể được cấu hình để Retry sau khi lỗi.

•	Hữu ích khi có lỗi tạm thời như mất kết nối Email Server, API timeout...

   2. Task không bị mất khi worker chết:
  
•	Task chỉ bị xóa khỏi hàng đợi nếu Worker Acknowledge (xác nhận) đã xử lý xong.

•	Nếu Worker chết đột ngột, task sẽ được trả lại hàng đợi.

   3. Worker tự động restart:

•	Có thể dùng Supervisor, Systemd hoặc Kubernetes để giám sát và tự động khởi động lại Worker khi bị Crash.


*4.3. Consistency của dữ liệu*

Celery không quản lý dữ liệu trực tiếp, nhưng tính nhất quán (consistency) phụ thuộc vào:

   *Trường hợp cần lưu kết quả (result backend):*
   
•	Sử dụng Redis, PostgreSQL, MongoDB... để lưu kết quả task.

•	Nếu worker hoàn thành nhưng fail khi lưu kết quả → có thể bị inconsistent.

   *Giải pháp cải thiện:*
   
•	Dùng cơ chế atomic transaction trong task để đảm bảo toàn vẹn

•	Sử dụng Idempotent Tasks (tác vụ có thể chạy lại nhiều lần mà không gây lỗi) để tránh ghi đè sai dữ liệu.

•	Tích hợp với hệ thống lưu trữ đảm bảo ACID (PostgreSQL, CockroachDB...).

# Kết Luận Chung: 

Celery không đảm bảo Consistency tuyệt đối như một hệ thống CSDL, nhưng có thể đảm bảo tính nhất quán ứng dụng nếu thiết kế task đúng cách.

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
