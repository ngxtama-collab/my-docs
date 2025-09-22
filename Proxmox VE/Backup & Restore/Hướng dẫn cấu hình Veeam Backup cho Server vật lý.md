Tài liệu kỹ thuật: Hướng dẫn cấu hình Veeam Backup cho Server vật lý

Phân loại mục:\
📁 Virtualization\
  📁 Backup & Restore\
    📄 Hướng Dẫn Cấu Hình Veeam Backup Cho Server Vật Lý

🌟 Mục tiêu

-   Cài đặt và cấu hình phần mềm Veeam Backup & Replication.

-   Thiết lập job sao lưu định kỳ cho các server vật lý chạy Windows.

-   Tăng cường khả năng khôi phục dữ liệu trong trường hợp sự cố.

🧩 Giới thiệu

Veeam Backup là phần mềm sao lưu chuyên dụng cho cả môi trường vật lý và
ảo hóa như VMware, Hyper-V, Proxmox. Hỗ trợ backup tăng dần
(incremental), khôi phục linh hoạt, quản lý tập trung.

🛠️ Các thành phần chính của hệ thống

-   **Veeam Backup Server:** Điều phối toàn bộ hoạt động backup/restore.

-   **Backup Proxy:** Xử lý dữ liệu sao lưu (compress, dedup).

-   **Backup Repository:** Nơi lưu trữ bản sao lưu.

-   **Enterprise Manager:** Quản trị từ trình duyệt web.

-   **Backup Search:** Tìm kiếm dữ liệu đã sao lưu.

**1️⃣ Cài đặt Veeam Backup Server**

**Bước 1: Tải phần mềm**

-   Download file ISO VeeamBackup&Replication_12.2.0.334_20240926.iso từ
    trang chủ Veeam.

![A screen shot of a black screen AI-generated content may be
incorrect.](../images/media/image1.png){width="6.5in"
height="0.7277777777777777in"}

**Bước 2: Cài đặt**

-   Giải nén file ISO và chạy Setup.exe

![A screenshot of a computer program AI-generated content may be
incorrect.](media/image2.png){width="6.5in"
height="3.151388888888889in"}

-   Chọn **Install Veeam Backup & Replication**

-   Tiếp tục nhấn **Next** cho tới bước chọn tài khoản

**Bước 3: Thiết lập tài khoản dịch vụ**

-   Dùng **Local System account** hoặc nhập tài khoản domain.

![A screenshot of a computer Description automatically
generated](media/image3.png){width="6.5in" height="5.057638888888889in"}

**Bước 4: Kết nối SQL Server**

-   Nếu có SQL Server riêng → nhập thông tin kết nối.

-   Nếu không, Veeam sẽ cài SQL Express mặc định.

![A screenshot of a computer Description automatically
generated](media/image4.png){width="6.5in"
height="5.057638888888889in"}![A screenshot of a computer Description
automatically generated](media/image5.png){width="6.5in"
height="5.057638888888889in"}

**Bước 5: Cài đặt hoàn tất**

-   Nhấn **Install** để bắt đầu cài

![A screenshot of a computer Description automatically
generated](media/image6.png){width="6.5in" height="5.057638888888889in"}

-   Chọn **Finish** sau khi cài đặt xong

![A screenshot of a computer AI-generated content may be
incorrect.](media/image7.png){width="6.5in"
height="5.057638888888889in"}

-   Khởi động ứng dụng và nhấn **Connect**

**2️⃣ Cấu hình Backup Repository**

-   Truy cập tab **Backup Infrastructure** → Add Backup Repository

-   Chọn loại repo: Windows, Linux, NAS\...

-   Chỉ định đường dẫn lưu trữ (ví dụ: D:\\VeeamBackup) và xác nhận

![A screenshot of a computer Description automatically
generated](media/image8.png){width="6.5in" height="4.189583333333333in"}

**3️⃣ Tạo Job Backup Cho Server**

-   Vào **Home** → **Jobs** → **Backup Job**

-   Chọn **Windows Computer** → đặt tên job

![A screenshot of a computer AI-generated content may be
incorrect.](media/image9.png){width="6.5in"
height="4.916666666666667in"}

-   Thêm server vật lý cần sao lưu

-   Chọn chế độ backup: Entire machine / Volume / File-level

-   Cấu hình lịch trình chạy job (daily, weekly\...)

-   Chọn Repository đã tạo

-   Xác nhận và chạy thử job lần đầu

![A screenshot of a computer AI-generated content may be
incorrect.](media/image10.png){width="6.5in"
height="1.645138888888889in"}

**4️⃣ Phục hồi Server (Restore)**

-   Vào tab **Home** → **Restore**

-   Chọn dạng phục hồi:

    -   Entire machine

    -   Volume

    -   File/folder

-   Làm theo wizard để chọn thời điểm phục hồi, đích đến\...

![A screenshot of a desktop Description automatically
generated](media/image11.png){width="6.5in"
height="4.559027777777778in"}

**🔐 Lưu ý bảo mật**

-   Phân quyền người dùng truy cập Veeam rõ ràng

-   Đặt mật khẩu cho backup repository (nếu dùng ổ NAS)

-   Luôn backup Veeam configuration định kỳ

**✅ Kiểm tra sau triển khai**

-   Job backup hoàn tất không lỗi

-   Có thể khôi phục file bất kỳ từ bản backup

-   Kiểm tra dung lượng backup và retention phù hợp
