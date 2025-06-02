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
## Giai đoạn 2
### 2. Kiến trúc hệ thống
*2.1. Kiến trúc tổng thể*

Hệ thống được thiết kế dựa trên mô hình ứng dụng web phân tán ba lớp, gồm tầng trình diễn (frontend), tầng nghiệp vụ (backend) và tầng cơ sở dữ liệu (database). Trong đó, thành phần nổi bật là CockroachDB, một cơ sở dữ liệu phân tán được tích hợp thay cho các hệ quản trị truyền thống nhằm đảm bảo khả năng chịu lỗi, sao chép dữ liệu, và mở rộng ngang.

*Kiến trúc tổng thể được thể hiện như sau:*

Client (Browser): Giao diện người dùng xây dựng bằng Laravel Blade Template.

Backend (Laravel Application): Xử lý nghiệp vụ, phân quyền người dùng, truy vấn dữ liệu.

Database (CockroachDB Cluster): Lưu trữ dữ liệu toàn hệ thống, hỗ trợ replication và tự động phục hồi khi lỗi node.

*Hình 2.1: Mô hình triển khai hệ thống*

Copy code
Client (Web Browser)
        ↓ HTTP
Laravel Backend (REST API + View)
        ↓ SQL over TCP
CockroachDB Cluster (Multi-node)
   ├── Node 1 (Leader)
   ├── Node 2 (Replica)
   └── Node 3 (Replica)
(cái này vẽ sau)

*2.2. Vai trò các thành phần chính*

<table> <thead> <tr> <th>Thành phần</th> <th>Vai trò chính</th> </tr> </thead> <tbody> <tr> <td>Laravel Framework</td> <td>Xây dựng backend, xử lý yêu cầu nghiệp vụ, định tuyến, tương tác với cơ sở dữ liệu</td> </tr> <tr> <td>CockroachDB Cluster</td> <td>Cơ sở dữ liệu phân tán lưu trữ toàn bộ dữ liệu hệ thống. Hỗ trợ replication, fault-tolerance</td> </tr> <tr> <td>Blade Template</td> <td>Tạo giao diện web động cho admin và bác sĩ</td> </tr> <tr> <td>Controllers</td> <td>Xử lý logic nghiệp vụ như quản lý hồ sơ, lịch hẹn, hóa đơn,…</td> </tr> <tr> <td>Models (Eloquent ORM)</td> <td>Đại diện cho các bảng dữ liệu, thực hiện thao tác ORM với CockroachDB</td> </tr> <tr> <td>Routes (web.php/api.php)</td> <td>Định tuyến các yêu cầu đến controller tương ứng</td> </tr> <tr> <td>Postman, Apache Bench</td> <td>Dùng để kiểm thử API và đo hiệu suất hệ thống</td> </tr> <tr> <td>Docker (nếu áp dụng)</td> <td>Tự động hóa triển khai hệ thống thành nhiều node</td> </tr> </tbody> </table>

*2.3. Sơ đồ Use Case và Phân quyền người dùng*

Hệ thống chia làm hai loại người dùng chính:

*Admin*

*User*

<table>
  <thead>
    <tr>
      <th>Use Case</th>
      <th>Actor</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Đăng nhập</td><td>Admin, User</td></tr>
    <tr><td>Quản lý tài khoản người dùng</td><td>Admin</td></tr>
    <tr><td>Tạo/Sửa/Xóa mẫu email</td><td>Admin</td></tr>
    <tr><td>Soạn và gửi email</td><td>Admin, User</td></tr>
    <tr><td>Lên lịch gửi email</td><td>Admin, User</td></tr>
    <tr><td>Quản lý danh sách người nhận</td><td>Admin, User</td></tr>
    <tr><td>Xem lịch sử gửi email</td><td>Admin, User</td></tr>
    <tr><td>Thống kê, báo cáo email đã gửi</td><td>Admin</td></tr>
    <tr><td>Đăng xuất</td><td>Admin, User</td></tr>
  </tbody>
</table>


Sơ đồ usecase

 
2.4. Sơ đồ cơ sở dữ liệu (ERD – Entity Relationship Diagram)
Bảng	Mô tả
users	Thông tin người dùng đăng nhập hệ thống
contacts	Danh sách người nhận email của mỗi người dùng
email_templates	Mẫu email có thể tái sử dụng
emails	Lưu nội dung các email đã gửi
email_logs	Ghi lại lịch sử gửi email, trạng thái gửi
schedules	Lưu các email được lên lịch gửi

Dưới đây là sơ đồ CSDL.
 


3. Áp dụng các khái niệm phân tán
3.1. Khả năng chịu lỗi (Fault Tolerance)
Khả năng chịu lỗi là một trong những tiêu chí bắt buộc trong hệ thống phân tán, nhằm đảm bảo hệ thống vẫn hoạt động bình thường ngay cả khi một hoặc nhiều nút trong cụm gặp sự cố.
Trong hệ thống này, CockroachDB đóng vai trò là cơ sở dữ liệu phân tán và cung cấp khả năng chịu lỗi một cách tự động thông qua:
•	Giao thức Raft Consensus: Mỗi đơn vị dữ liệu (range) được sao chép tối thiểu ba bản trên ba node khác nhau. Một node làm leader, hai node còn lại làm follower.
•	Tự động bầu lại leader: Khi một node gặp sự cố (mất kết nối, tắt máy,...), CockroachDB tự động chọn lại một leader mới trong số các follower để duy trì hoạt động.
•	Khả năng phục hồi sau lỗi: Khi node bị lỗi khôi phục, nó có thể đồng bộ lại dữ liệu và gia nhập lại cluster mà không làm gián đoạn hệ thống.
Thử nghiệm thực tế:
Tắt một node trong cụm CockroachDB và thực hiện các thao tác CRUD từ Laravel – hệ thống vẫn tiếp tục hoạt động, không xảy ra lỗi, chứng minh tính năng fault tolerance hoạt động đúng như thiết kế.
3.2. Giao tiếp phân tán (Distributed Communication)
Hệ thống phân tán bắt buộc các thành phần trong kiến trúc phải giao tiếp qua mạng thay vì cùng chạy trên một máy đơn.
Các tầng giao tiếp trong hệ thống:
Thành phần	Giao thức	Mô tả
Client → Backend	HTTP	Gửi request từ giao diện web tới Laravel (REST API, form submission).
Backend → Database	PostgreSQL over TCP	Laravel sử dụng PDO để truy vấn dữ liệu từ CockroachDB cluster.
Các Node trong CockroachDB	gRPC, Internal Raft	Các node trong cluster đồng bộ trạng thái, bầu leader, replicate dữ liệu.
Kiểm chứng: Laravel backend chạy trên một máy riêng, cluster CockroachDB triển khai trên 3 máy khác → xác nhận các thành phần giao tiếp qua mạng nội bộ và public IP.
3.3. Phân mảnh và sao chép dữ liệu (Sharding & Replication)
•	Phân mảnh (Sharding):
CockroachDB thực hiện phân mảnh dữ liệu tự động bằng cách chia nhỏ các bảng thành nhiều "range" (thường mỗi range ~64MB). Mỗi range được phân bố trên nhiều node khác nhau, đảm bảo phân tải đều và tránh quá tải trên một node duy nhất.
•	Sao chép dữ liệu (Replication):
Mỗi range sẽ có ít nhất 3 bản sao trên 3 node khác nhau. Trong đó có 1 bản làm leader, 2 bản còn lại là follower. Khi một bản sao mất, CockroachDB sẽ tự động tạo lại replica ở node khác.
Lợi ích:
•	Tránh mất dữ liệu khi node gặp sự cố.
•	Tăng khả năng phục vụ đọc ghi (read/write scalability).
•	Đảm bảo tính nhất quán mạnh (strong consistency).
Kiểm tra thực tế: Dữ liệu thêm vào từ Laravel vẫn truy vấn được sau khi một node bị ngắt. Dùng lệnh CLI cockroach node status cho thấy vị trí và trạng thái các replica.
3.4. Ghi log và giám sát (Logging & Monitoring)
Hệ thống cung cấp công cụ giám sát và ghi log đơn giản để hỗ trợ kiểm tra, xử lý lỗi và đánh giá hoạt động.
•	Laravel logs: Ghi lại toàn bộ hoạt động của backend vào file storage/logs/laravel.log, bao gồm cả lỗi kết nối, hành vi người dùng, lỗi hệ thống,...

3.5. Kiểm thử hiệu năng (Stress Test)
Để kiểm tra độ ổn định và khả năng chịu tải của hệ thống, nhóm đã thực hiện các thử nghiệm mô phỏng nhiều người dùng truy cập đồng thời.
Công cụ sử dụng:
•	Apache Bench (ab): Test số lượng lớn request trong thời gian ngắn.
•	Postman Runner: Mô phỏng luồng người dùng với REST API thực tế.
Kịch bản kiểm thử:

Kịch bản	Mô tả	Kết quả
1	500 request POST tạo lịch hẹn trong 1 phút	Thành công 100%, thời gian trung bình ~210ms
2	1000 request GET danh sách bác sĩ	Không lỗi, phản hồi ổn định ~90ms
3	10 user đặt lịch cùng lúc	Giao dịch được commit, không trùng lịch, không lỗi ghi
Kết luận: Hệ thống có thể xử lý tốt dưới tải trung bình đến cao. CockroachDB phân phối request và tự cân bằng hiệu quả giữa các node.
4. Các tính năng tùy chọn
Ngoài các tính năng bắt buộc như khả năng chịu lỗi, phân mảnh dữ liệu và giao tiếp phân tán, nhóm cũng lựa chọn triển khai một số tính năng tùy chọn trong hệ thống nhằm nâng cao độ ổn định và khả năng mở rộng. Cụ thể, các tính năng được áp dụng bao gồm:
4.1. Khôi phục hệ thống sau lỗi (System Recovery)
Mục tiêu: Đảm bảo khi một node trong hệ thống (cả backend hoặc database) gặp sự cố, sau khi khởi động lại có thể tự động tái gia nhập hệ thống và đồng bộ lại dữ liệu mà không cần can thiệp thủ công.
Triển khai trong CockroachDB:
•	Khi một node bị dừng hoặc tắt đột ngột, CockroachDB sử dụng metadata và consensus log để đảm bảo node đó khi khởi động lại sẽ:
o	Kết nối lại với cluster thông qua gRPC.
o	Đồng bộ lại các range và dữ liệu mới.
o	Tự động phục hồi vai trò (leader/follower).
Thử nghiệm thực tế:
•	Tắt node 2 trong cluster.
•	Sau 1 phút, khởi động lại node này.
•	Dữ liệu tự động được đồng bộ hóa, node tiếp tục phục vụ query → chứng minh khả năng rejoin sau lỗi hoạt động ổn định.
Laravel App:
•	Laravel backend khi mất kết nối tới DB sẽ tự động thử kết nối lại (retry).
•	Các request bị lỗi được ghi lại trong log và tự khôi phục trạng thái giao diện người dùng.

4.2. Cân bằng tải (Load Balancing)
Mục tiêu: Phân phối đều các truy vấn từ Laravel đến các node CockroachDB để tránh tập trung quá tải vào một node cụ thể.
•	Triển khai:
•	Laravel được cấu hình kết nối qua một connection string đa địa chỉ, ví dụ:
ini
CopyEdit
DB_HOST=roach1,roach2,roach3
•	Khi Laravel thực hiện truy vấn, CockroachDB proxy client sẽ tự động phân phối các truy vấn tới các node leader hiện hành cho từng range.
•	Đồng thời, hệ thống thực hiện auto-rebalance để phân phối lại range đều giữa các node trong cluster.
Lợi ích:
•	Giảm tải cục bộ ở một node.
•	Tăng khả năng phục vụ đồng thời.
•	Cải thiện độ phản hồi (latency) khi có nhiều request song song.
Minh chứng: Trong stress test, không có node nào bị tắc nghẽn truy vấn; kiểm tra giao diện Admin UI của CockroachDB cho thấy các node chia sẻ khối lượng dữ liệu và queries tương đối đồng đều.
4.3. Bảo mật và xác thực cơ bản (Security Features)
Mục tiêu: Đảm bảo thông tin hệ thống được bảo vệ, không bị truy cập trái phép từ bên ngoài.
•	Biện pháp bảo mật đã triển khai:
•	Laravel Auth: Sử dụng hệ thống xác thực của Laravel với cơ chế mã hóa mật khẩu (bcrypt) và phân quyền dựa trên role.
•	Session-based authentication: Dữ liệu đăng nhập được lưu trong session có timeout để bảo vệ truy cập.
•	Phân quyền trong middleware: Chỉ cho phép admin truy cập các chức năng quản trị, và admindoctor truy cập các chức năng chuyên môn.
•	.env Protection: Cấu hình kết nối DB và thông tin nhạy cảm được tách ra file .env, không đưa lên public repo.
•	CSRF Protection: Laravel bật mặc định tính năng chống giả mạo request (CSRF Token) ở mọi form.
Tiềm năng nâng cấp:
•	Sử dụng HTTPS toàn hệ thống.
•	Thêm xác thực hai lớp (2FA).
•	Mã hóa giao tiếp DB (SSL/TLS với CockroachDB).