# Proxmox Backup Server

## 1. Setup OS

a. Cai tren 1 server tu file ISO  
<https://www.proxmox.com/en/downloads>

b. Cai tren Proxmox VE server

Them dong sau vao file `/etc/apt/sources.list`:

```
deb http://download.proxmox.com/debian/pbs bullseye pbs-no-subscription
```

Cai dat:

```
apt update
apt install proxmox-backup-server
```

Sau khi cai dat co the truy cap bang trinh duyet:  
`https://<IP>:8007`

---

## 2. Tao User

![User](../images/media/image1.png)

Nhap User/Pass  
Tich **Enabled** va set **Expire never**

---

## 3. Tao Datastore

![Datastore 1](../images/media/image2.png)  
![Datastore 2](../images/media/image3.png)  
![Datastore 3](../images/media/image4.png)

Nhap so ban backup gan nhat can giu.  
Set permission cho User nao duoc su dung Datastore nay

![Permission](../images/media/image5.png)

---

## 4. Ket noi den PVE server

Cau hinh network thong tu PVE server va PBS.  

Tren PBS chay lenh:

```
proxmox-backup-manager cert info | grep Fingerprint
```

![Fingerprint](../images/media/image6.png)

Luu thong tin **Fingerprint** de add vao PVE.  

Vao **Cluster PVE**:

![Cluster 1](../images/media/image7.png)  
![Cluster 2](../images/media/image8.png)  
![Cluster 3](../images/media/image9.png)  
![Cluster 4](../images/media/image10.png)

---

## 5. Add Backup Job

![Backup Job 1](../images/media/image11.png)  
![Backup Job 2](../images/media/image12.png)
