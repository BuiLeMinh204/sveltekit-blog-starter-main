# Hệ thống phân tán là gì?
Hệ thống phân tán (Distributed System) là một hệ thống bao gồm nhiều thành phần (máy tính, thiết bị) độc lập, nhưng phối hợp làm việc với nhau để hoàn thành một nhiệm vụ chung. Các thành phần này có thể nằm ở các địa điểm khác nhau và giao tiếp với nhau qua mạng. Mặc dù các thành phần trong hệ thống phân tán có thể ở xa nhau, nhưng chúng hoạt động như một hệ thống duy nhất đối với người sử dụng.

## Các đặc điểm của hệ thống phân tán:
### Phân tán về địa lý: 
Các máy tính trong hệ thống không nhất thiết phải ở cùng một địa điểm mà có thể nằm ở nhiều nơi khác nhau.

### Giao tiếp qua mạng: 
Các thành phần trong hệ thống cần giao tiếp với nhau qua các kênh truyền thông như mạng LAN, WAN, internet, v.v.

### Độc lập: 
Các thành phần trong hệ thống có thể độc lập với nhau, mỗi máy tính có thể chạy các chương trình riêng biệt.

### Tính sẵn sàng cao: 
Hệ thống phân tán có thể đảm bảo tính khả dụng cao, nếu một phần của hệ thống gặp sự cố, các phần khác vẫn có thể tiếp tục hoạt động.

## Lợi ích của hệ thống phân tán:
### Tính mở rộng: 
Dễ dàng mở rộng hệ thống bằng cách thêm các nút mới mà không ảnh hưởng đến các thành phần hiện có.

### Tính chịu lỗi: 
Nếu một phần của hệ thống bị hỏng, các phần khác vẫn có thể tiếp tục hoạt động, giúp tăng tính ổn định và độ tin cậy.

### Tính chia sẻ tài nguyên: 
Các tài nguyên như máy chủ, cơ sở dữ liệu, phần mềm có thể được chia sẻ và sử dụng bởi nhiều người và hệ thống.

## Các ví dụ về hệ thống phân tán:
### Hệ thống máy chủ web: 
Các máy chủ web thường được phân tán để xử lý yêu cầu từ người dùng và đảm bảo tính sẵn sàng.

### Hệ thống lưu trữ đám mây: 
Các dịch vụ như Google Drive, Dropbox, AWS là các hệ thống phân tán, nơi dữ liệu được lưu trữ trên nhiều máy chủ ở các địa điểm khác nhau.

### Blockchain: 
Là một hệ thống phân tán, nơi mỗi nút trong mạng có thể kiểm tra và xác nhận các giao dịch mà không cần đến sự can thiệp của một bên trung gian.

# Các ứng dụng của hệ thống phân tán
Hệ thống phân tán có rất nhiều ứng dụng trong các lĩnh vực khác nhau nhờ vào khả năng phân tán tài nguyên, khả năng chịu lỗi, và tính mở rộng. Dưới đây là một số ứng dụng phổ biến của hệ thống phân tán:

### Lưu trữ đám mây (Cloud Storage)
Ví dụ: Google Drive, Dropbox, Amazon S3

Hệ thống phân tán được sử dụng để lưu trữ và đồng bộ hóa dữ liệu trên nhiều máy chủ ở nhiều vị trí địa lý khác nhau. Người dùng có thể truy cập dữ liệu từ bất kỳ đâu mà không phải lo ngại về việc mất dữ liệu vì hệ thống có khả năng chịu lỗi và sao lưu dữ liệu trên các máy chủ khác nhau.

### Dịch vụ Web và Mạng xã hội
Ví dụ: Facebook, Twitter, Instagram, YouTube

Các nền tảng mạng xã hội và dịch vụ web lớn sử dụng hệ thống phân tán để xử lý hàng triệu yêu cầu người dùng mỗi giây. Các máy chủ web và cơ sở dữ liệu phân tán giúp hệ thống mở rộng và chịu tải tốt hơn.

### Hệ thống thanh toán điện tử và Blockchain
Ví dụ: Bitcoin, Ethereum

Các mạng blockchain là hệ thống phân tán, trong đó dữ liệu giao dịch được phân tán trên nhiều nút mạng. Mỗi nút kiểm tra và xác nhận giao dịch mà không cần sự can thiệp của bên trung gian, giúp đảm bảo tính bảo mật và minh bạch.

### Dữ liệu lớn và phân tích (Big Data and Analytics)
Ví dụ: Hadoop, Apache Spark

Hệ thống phân tán được sử dụng trong các ứng dụng phân tích dữ liệu lớn, nơi dữ liệu được chia nhỏ và xử lý song song trên nhiều máy chủ. Điều này giúp xử lý và phân tích dữ liệu khổng lồ một cách nhanh chóng và hiệu quả.

### Hệ thống chia sẻ tài nguyên
Ví dụ: Hệ thống chia sẻ tài nguyên tính toán (Grid Computing), máy chủ ảo (Virtualization)

Các hệ thống phân tán cho phép chia sẻ tài nguyên tính toán, bộ nhớ, hoặc băng thông trên nhiều máy tính trong mạng. Ví dụ, hệ thống Grid Computing có thể cho phép các nhà nghiên cứu chia sẻ sức mạnh tính toán từ các máy tính khác nhau trên toàn cầu để giải quyết các bài toán phức tạp.

### Hệ thống phân tán thời gian thực
Ví dụ: Hệ thống điều khiển giao thông, mạng điện, hệ thống điều khiển công nghiệp

Các hệ thống phân tán thời gian thực giúp giám sát và điều khiển các quá trình trong thời gian thực. Ví dụ, trong các hệ thống giao thông thông minh, dữ liệu từ các cảm biến giao thông được thu thập và phân tích để tối ưu hóa đèn tín hiệu và luồng giao thông.

### Hệ thống tìm kiếm
Ví dụ: Google Search, Bing

Các công cụ tìm kiếm sử dụng hệ thống phân tán để thu thập, lưu trữ và xử lý lượng lớn dữ liệu từ web. Quá trình tìm kiếm và xếp hạng các trang web được phân tán trên nhiều máy chủ để tối ưu hóa tốc độ và khả năng mở rộng.

### Ứng dụng di động và IoT (Internet of Things)
Ví dụ: Các ứng dụng thông minh (smart home), các hệ thống giám sát từ xa

Các hệ thống phân tán được sử dụng trong các ứng dụng IoT để thu thập và xử lý dữ liệu từ nhiều thiết bị kết nối (như cảm biến, thiết bị gia đình thông minh, hoặc xe tự lái). Dữ liệu được phân phối và xử lý trên các máy chủ hoặc trong đám mây, giúp tối ưu hóa việc giám sát và ra quyết định.

### Hệ thống trò chơi trực tuyến
Ví dụ: World of Warcraft, Fortnite

Các trò chơi trực tuyến yêu cầu hệ thống phân tán để xử lý và đồng bộ hóa các hành động của người chơi trên toàn thế giới. Điều này giúp duy trì kết nối và trạng thái của trò chơi một cách chính xác cho mọi người chơi trong thời gian thực.

### Hệ thống viễn thông
Ví dụ: Mạng 5G, các hệ thống chuyển mạch viễn thông

Các hệ thống phân tán được sử dụng để xử lý lưu lượng mạng và truyền tải dữ liệu trong các mạng viễn thông, giúp tối ưu hóa băng thông, giảm độ trễ và đảm bảo kết nối ổn định cho hàng triệu người dùng.

### Hệ thống quản lý cơ sở dữ liệu phân tán
Ví dụ: Google Spanner, Amazon DynamoDB

Hệ thống cơ sở dữ liệu phân tán giúp duy trì dữ liệu nhất quán và khả năng truy cập từ nhiều máy chủ khác nhau. Chúng cho phép quản lý lượng dữ liệu lớn và hỗ trợ các ứng dụng có yêu cầu cao về tính sẵn sàng và hiệu suất.

### Hệ thống phát hiện và phòng chống tấn công mạng (IDS/IPS)
Ví dụ: Hệ thống phân tán phòng chống xâm nhập (Intrusion Detection Systems)

Các hệ thống phân tán giúp giám sát và phát hiện các mối đe dọa trên mạng từ nhiều điểm khác nhau, bảo vệ mạng khỏi các cuộc tấn công phân tán.

# Các khái niệm chính của hệ thống phân tán

### Scalability

**Khả năng mở rộng** là khả năng của một hệ thống hoặc ứng dụng để xử lý được một lượng công việc lớn hơn khi tăng thêm tài nguyên (như máy chủ, bộ nhớ, băng thông, v.v.). Một hệ thống có khả năng mở rộng tốt có thể duy trì hiệu suất và tính ổn định khi tải của hệ thống tăng lên.

**Mở rộng theo chiều ngang (horizontal scalability)** và **mở rộng theo chiều dọc (vertical scalability)** là hai cách chính để mở rộng hệ thống.
### Fault Tolerance

**Khả năng chịu lỗi** là khả năng của một hệ thống tiếp tục hoạt động bình thường ngay cả khi có sự cố hoặc lỗi xảy ra ở một hoặc nhiều thành phần trong hệ thống. Các hệ thống chịu lỗi cao có thể khôi phục sau sự cố mà không ảnh hưởng đến trải nghiệm người dùng hoặc hoạt động chung của hệ thống.
### Availability

**Tính sẵn sàng** đề cập đến khả năng của một hệ thống hoặc dịch vụ có sẵn và có thể sử dụng được vào bất kỳ thời điểm nào. Tính sẵn sàng cao có nghĩa là hệ thống có thể duy trì hoạt động liên tục mà không có thời gian chết (downtime) đáng kể. Hệ thống có tính sẵn sàng cao có thể phục hồi nhanh chóng từ các sự cố và luôn có thể truy cập.
### Transparency

**Tính minh bạch** trong hệ thống phân tán có nghĩa là việc người dùng hoặc các ứng dụng không cần phải biết về cách thức hệ thống phân tán hoạt động phía sau. Điều này bao gồm việc ẩn đi các chi tiết như sự phân tán về địa lý, phân chia dữ liệu, hoặc các cơ chế đồng bộ hóa, giúp người dùng chỉ tập trung vào các tính năng và chức năng của hệ thống mà không cần quan tâm đến các vấn đề kỹ thuật phức tạp.
### Concurrency

**Concurrency** là khả năng của hệ thống để xử lý nhiều tác vụ (tasks) trong cùng một thời điểm, dù các tác vụ này có thể không thực sự được thực thi cùng một lúc. Điều này giúp tối ưu hóa hiệu suất hệ thống, đặc biệt trong môi trường đa người dùng hoặc đa tiến trình. Các hệ thống đồng thời sử dụng cơ chế chia sẻ tài nguyên và đồng bộ hóa để đảm bảo các tác vụ không gây xung đột.
### Parallelism

**Parallelism** là khả năng của hệ thống để thực hiện nhiều tác vụ cùng một lúc (thực sự cùng thời gian). Ví dụ, một hệ thống có thể chạy nhiều tiến trình hoặc luồng (threads) đồng thời trên nhiều lõi CPU khác nhau. Điều này giúp cải thiện tốc độ và hiệu suất của các tác vụ tính toán phức tạp hoặc xử lý dữ liệu lớn.
### Openness

**Openness** đề cập đến việc hệ thống sử dụng các tiêu chuẩn mở hoặc các giao thức dễ dàng tiếp cận và sử dụng bởi cộng đồng phát triển phần mềm hoặc các tổ chức khác. Một hệ thống mở thường hỗ trợ tích hợp dễ dàng với các hệ thống khác và cho phép người dùng hoặc nhà phát triển tùy chỉnh hoặc thay đổi phần mềm.
### Vertical Scaling

**Vertical Scaling** là việc nâng cấp một máy chủ hoặc thiết bị phần cứng để tăng công suất xử lý (tăng bộ xử lý, bộ nhớ, hoặc ổ cứng). Việc mở rộng theo chiều dọc giúp hệ thống xử lý nhiều yêu cầu hơn nhưng giới hạn bởi khả năng tối đa của phần cứng. Ví dụ, nâng cấp RAM hoặc CPU của một máy chủ.
### Horizontal Scaling

**Horizontal Scaling** là việc thêm nhiều máy chủ vào hệ thống để phân chia tải công việc giữa các máy chủ. Mở rộng theo chiều ngang giúp hệ thống có khả năng xử lý nhiều yêu cầu hơn và có thể dễ dàng mở rộng bằng cách thêm vào các máy chủ hoặc tài nguyên tính toán bổ sung.
### Load Balancer

**Load Balancer** là một thành phần hệ thống giúp phân phối tải công việc (như yêu cầu từ người dùng) đến nhiều máy chủ hoặc dịch vụ trong một hệ thống phân tán. Mục đích là để đảm bảo rằng không một máy chủ nào bị quá tải, giúp cải thiện hiệu suất và độ sẵn sàng của hệ thống.
### Replication

**Replication** là quá trình sao chép dữ liệu hoặc các thành phần của hệ thống từ một máy chủ hoặc địa điểm này sang máy chủ hoặc địa điểm khác trong hệ thống phân tán. Điều này giúp tăng tính sẵn sàng và khả năng chịu lỗi của hệ thống. Nếu một bản sao của dữ liệu bị lỗi, các bản sao khác có thể được sử dụng để thay thế, đảm bảo rằng dữ liệu luôn có sẵn.