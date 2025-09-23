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
