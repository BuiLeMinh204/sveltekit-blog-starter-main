---
title: "Deliverable 2"
date: "2025-06-03"
updated: "2025-06-03"
categories:
  - "minhbui"
coverImage: "/images/jefferson-santos-fCEJGBzAkrU-unsplash.jpg"
coverWidth: 16
coverHeight: 9
excerpt: Ấn vào để xem thêm ....
---

---
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

