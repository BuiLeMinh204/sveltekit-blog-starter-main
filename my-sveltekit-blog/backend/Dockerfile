
# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Cài đặt gói phụ thuộc hệ thống
RUN apt-get update && apt-get install -y build-essential

# Tạo thư mục làm việc
WORKDIR /app

# Sao chép mã nguồn vào container
COPY . .

# Cài đặt thư viện Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Mở cổng Flask
EXPOSE 5000

# Lệnh khởi động ứng dụng Flask bằng Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
