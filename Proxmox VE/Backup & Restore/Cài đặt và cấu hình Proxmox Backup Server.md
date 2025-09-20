# Proxmox Backup Server

## 1. Setup OS

a. Cài trên 1 server từ file ISO  
<https://www.proxmox.com/en/downloads>

b. Cài trên Proxmox VE server

```bash
add deb http://download.proxmox.com/debian/pbs bullseye pbs-no-subscription \
    >> /etc/apt/sources.list

apt update
apt install proxmox-backup-server
Sau khi cài đặt có thể truy cập bằng trình duyệt:
<https://<IP>:8007>

2. Tạo User
<img src="images/media/image1.png" width="700" />
Nhập User/Pass → tích Enabled và set Expire never.

3. Tạo Datastore
<img src="images/media/image2.png" width="700" /> <img src="images/media/image3.png" width="700" /> <img src="images/media/image4.png" width="700" />
Nhập số bản backup gần nhất cần giữ.
Set permission cho User nào được sử dụng Datastore này.

<img src="images/media/image5.png" width="700" />
4. Kết nối đến PVE server
Cấu hình network thông từ PVE server và PBS.

Trên PBS chạy:

proxmox-backup-manager cert info | grep Fingerprint
<img src="images/media/image6.png" width="700" />
Lưu thông tin Fingerprint để add vào PVE.

Vào Cluster PVE:

<img src="images/media/image7.png" width="700" /> <img src="images/media/image8.png" width="700" /> <img src="images/media/image9.png" width="700" /> <img src="images/media/image10.png" width="700" />
5. Add Backup Job
<img src="images/media/image11.png" width="700" /> <img src="images/media/image12.png" width="700" /> ``
