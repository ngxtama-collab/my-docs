**Tài liệu kỹ thuật: Hướng dẫn cấu hình Veeam Backup cho Server vật lý**

**Phân loại mục:**  
📁 Virtualization  
  📁 Backup & Restore  
    📄 Hướng Dẫn Cấu Hình Veeam Backup Cho Server Vật Lý

**🌟 Mục tiêu**

- Cài đặt và cấu hình phần mềm Veeam Backup & Replication.

- Thiết lập job sao lưu định kỳ cho các server vật lý chạy Windows.

- Tăng cường khả năng khôi phục dữ liệu trong trường hợp sự cố.

**🧩 Giới thiệu**

Veeam Backup là phần mềm sao lưu chuyên dụng cho cả môi trường vật lý và
ảo hóa như VMware, Hyper-V, Proxmox. Hỗ trợ backup tăng dần
(incremental), khôi phục linh hoạt, quản lý tập trung.

**🛠️ Các thành phần chính của hệ thống**

- **Veeam Backup Server:** Điều phối toàn bộ hoạt động backup/restore.

- **Backup Proxy:** Xử lý dữ liệu sao lưu (compress, dedup).

- **Backup Repository:** Nơi lưu trữ bản sao lưu.

- **Enterprise Manager:** Quản trị từ trình duyệt web.

- **Backup Search:** Tìm kiếm dữ liệu đã sao lưu.

**1️⃣ Cài đặt Veeam Backup Server**

**Bước 1: Tải phần mềm**

- Download file ISO VeeamBackup&Replication_12.2.0.334_20240926.iso từ
  trang chủ Veeam.

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:6.5in;height:0.72778in"
alt="A screen shot of a black screen AI-generated content may be incorrect." />

**Bước 2: Cài đặt**

- Giải nén file ISO và chạy Setup.exe

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:3.15139in"
alt="A screenshot of a computer program AI-generated content may be incorrect." />

- Chọn **Install Veeam Backup & Replication**

- Tiếp tục nhấn **Next** cho tới bước chọn tài khoản

**Bước 3: Thiết lập tài khoản dịch vụ**

- Dùng **Local System account** hoặc nhập tài khoản domain.

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:6.5in;height:5.05764in"
alt="A screenshot of a computer Description automatically generated" />

**Bước 4: Kết nối SQL Server**

- Nếu có SQL Server riêng → nhập thông tin kết nối.

- Nếu không, Veeam sẽ cài SQL Express mặc định.

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image4.png"
style="width:6.5in;height:5.05764in"
alt="A screenshot of a computer Description automatically generated" /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image5.png"
style="width:6.5in;height:5.05764in"
alt="A screenshot of a computer Description automatically generated" />

**Bước 5: Cài đặt hoàn tất**

- Nhấn **Install** để bắt đầu cài

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image6.png"
style="width:6.5in;height:5.05764in"
alt="A screenshot of a computer Description automatically generated" />

- Chọn **Finish** sau khi cài đặt xong

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image7.png"
style="width:6.5in;height:5.05764in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

- Khởi động ứng dụng và nhấn **Connect**

**2️⃣ Cấu hình Backup Repository**

- Truy cập tab **Backup Infrastructure** → Add Backup Repository

- Chọn loại repo: Windows, Linux, NAS...

- Chỉ định đường dẫn lưu trữ (ví dụ: D:\VeeamBackup) và xác nhận

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image8.png"
style="width:6.5in;height:4.18958in"
alt="A screenshot of a computer Description automatically generated" />

**3️⃣ Tạo Job Backup Cho Server**

- Vào **Home** → **Jobs** → **Backup Job**

- Chọn **Windows Computer** → đặt tên job

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image9.png"
style="width:6.5in;height:4.91667in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

- Thêm server vật lý cần sao lưu

- Chọn chế độ backup: Entire machine / Volume / File-level

- Cấu hình lịch trình chạy job (daily, weekly...)

- Chọn Repository đã tạo

- Xác nhận và chạy thử job lần đầu

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image10.png"
style="width:6.5in;height:1.64514in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

**4️⃣ Phục hồi Server (Restore)**

- Vào tab **Home** → **Restore**

- Chọn dạng phục hồi:

  - Entire machine

  - Volume

  - File/folder

- Làm theo wizard để chọn thời điểm phục hồi, đích đến...

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image11.png"
style="width:6.5in;height:4.55903in"
alt="A screenshot of a desktop Description automatically generated" />

**🔐 Lưu ý bảo mật**

- Phân quyền người dùng truy cập Veeam rõ ràng

- Đặt mật khẩu cho backup repository (nếu dùng ổ NAS)

- Luôn backup Veeam configuration định kỳ

**✅ Kiểm tra sau triển khai**

- Job backup hoàn tất không lỗi

- Có thể khôi phục file bất kỳ từ bản backup

- Kiểm tra dung lượng backup và retention phù hợp
