# Tài liệu kỹ thuật: Migrate VM giữa hai host Proxmox không Cluster (ZFS)

Di chuyển một máy ảo (VM) đang sử dụng **ZFS storage** từ một host Proxmox (A) sang một host khác (B) **mà không cần join cluster**.

---

## 📌 Yêu cầu

- Cả hai host đều sử dụng ZFS.  
- SSH giữa hai host hoạt động.  
- VM cần migrate đang ở trạng thái **tắt (shutdown)**.  

---

## 🧪 Ví dụ thực tế

- VM ID gốc: **110** (trên host A)  
- VM ID mới: **100** (trên host B)  
- ZFS pool: **Datastore**  
- Disk:  
  - scsi0 (3000G)  
  - scsi1 (457344M)  

---

## 🛠️ Các bước thực hiện

### 1️⃣ Trên host A - tạo snapshot

```bash
zfs snapshot Datastore/vm-110-disk-0@snap
zfs snapshot Datastore/vm-110-disk-1@snap

---

###2️⃣ Gửi ZFS snapshot sang host B và đổi tên volume theo VM mới

```bash
qm create 100 --name TenVM --memory 4096 --cores 4 --net0 virtio,bridge=vmbr0

---

###3️⃣ Trên host B - tạo VM mới (ID 100)

```bash
qm create 100 --name TenVM --memory 4096 --cores 4 --net0 virtio,bridge=vmbr0

---

###4️⃣ Gắn disk ZFS vào VM 100

```bash
qm set 100 --scsi0 Datastore:vm-100-disk-0
qm set 100 --scsi1 Datastore:vm-100-disk-1

---

###5️⃣ Khởi động và kiểm tra VM

```bash
qm start 100

---

##🔁 Tuỳ chọn: Giữ nguyên ID VM (110)

```bash
qm create 110 --name TenVM --memory 4096 --cores 4 --net0 virtio,bridge=vmbr0
qm set 110 --scsi0 Datastore:vm-110-disk-0
qm set 110 --scsi1 Datastore:vm-110-disk-1

