# Proxmox Backup Server
## Setup OS

a. Cài trên 1 server từ file ISO <https://www.proxmox.com/en/downloads>

b. Cài trên Proxmox VE server

add deb http://download.proxmox.com/debian/pbs


vào file `/etc/apt/sources.list`

apt update
apt install proxmox-backup-server

Sau khi cài đặt có thể truy cập bằng trình duyệt:  
`https://<IP>:8007`

---

## 2. Tạo User

![](images/media/image1.png)

Nhập User/Pass, tích **Enabled** và set **Expire never**

---

## 3. Tạo Datastore

![Datastore 1](./images/image2.png)  
![Datastore 2](./images/image3.png)  
![Datastore 3](./images/image4.png)

Nhập số bản backup gần nhất cần giữ.  
Set permission cho User nào được sử dụng Datastore này.

![](images/media/image5.png)

---

## 4. Kết nối đến PVE server

Cấu hình network thông từ PVE server và PBS.  

Trên PBS chạy command:

