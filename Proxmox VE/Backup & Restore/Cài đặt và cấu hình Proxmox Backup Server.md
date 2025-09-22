# Proxmox Backup Server

## 1.Setup OS

a. Cài trên 1 server từ file ISO  
<https://www.proxmox.com/en/downloads>

b. Cài trên Proxmox VE server

Thêm dòng sau vào file `/etc/apt/sources.list`:

```
deb http://download.proxmox.com/debian/pbs bullseye pbs-no-subscription
```

Cài đặt:

```
apt update
apt install proxmox-backup-server
```

Sau khi cài đặt có thể truy cập bằng trình duyệt:  
`https://<IP>:8007`

---

## 2. Tạo User

![User](../images/media/image1.png)

Nhập User/Pass  
Tích **Enabled** và set **Expire never**

---

## 3. Tạo Datastore

![Datastore 1](../images/media/image2.png)  
![Datastore 2](../images/media/image3.png)  
![Datastore 3](../images/media/image4.png)

Nhập số bản backup gần nhất cần giữ.  
Set permission cho User nào được sử dụng Datastore này

![Permission](../images/media/image5.png)

---

## 4. Kết nối đến PVE server

Cấu hình network thông từ PVE server và PBS.  

Trên PBS chạy lệnh:

```
proxmox-backup-manager cert info | grep Fingerprint
```

![Fingerprint](../images/media/image6.png)

Lưu thông tin **Fingerprint** để add vào PVE.  

Vào **Cluster PVE**:

![Cluster 1](../images/media/image7.png)  
![Cluster 2](../images/media/image8.png)  
![Cluster 3](../images/media/image9.png)  
![Cluster 4](../images/media/image10.png)

---

## 5. Add Backup Job

![Backup Job 1](../images/media/image11.png)  
![Backup Job 2](../images/media/image12.png)
