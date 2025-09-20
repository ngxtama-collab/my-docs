**Tài liệu kỹ thuật: Migrate VM giữa hai host Proxmox không Cluster
(ZFS)**

**Phân loại mục:**  
📁 Virtualization  
  📁 Proxmox VE  
    📁 Setup  
      📄 Migrate VM giữa hai host không cluster (ZFS)

**🌟 Mục tiêu**

Di chuyển một máy ảo (VM) đang sử dụng ZFS storage từ một host Proxmox
(A) sang một host khác (B) **mà không cần join cluster**.

**📌 Yêu cầu**

- Cả hai host đều sử dụng ZFS.

- SSH giữa hai host hoạt động.

- VM cần migrate đang ở trạng thái **tắt (shutdown)**.

**🧪 Ví dụ thực tế**

- VM ID gốc: 110 (trên host A)

- VM ID mới: 100 (trên host B)

- ZFS pool: Datastore

- Disk: scsi0 (3000G), scsi1 (457344M)

**🛠️ Các bước thực hiện**

**1️⃣ Trên host A - tạo snapshot**

zfs snapshot Datastore/vm-110-disk-0@snap

zfs snapshot Datastore/vm-110-disk-1@snap

**2️⃣ Gửi ZFS snapshot sang host B và đổi tên volume theo VM mới**

zfs send Datastore/vm-110-disk-0@snap \| ssh root@hostB zfs receive
Datastore/vm-100-disk-0

zfs send Datastore/vm-110-disk-1@snap \| ssh root@hostB zfs receive
Datastore/vm-100-disk-1

**3️⃣ Trên host B - tạo VM mới (ID 100)**

qm create 100 --name TenVM --memory 4096 --cores 4 --net0
virtio,bridge=vmbr0

**4️⃣ Gắn disk ZFS vào VM 100**

qm set 100 --scsi0 Datastore:vm-100-disk-0

qm set 100 --scsi1 Datastore:vm-100-disk-1

**5️⃣ Khởi động và kiểm tra VM**

qm start 100

**🔁 Tuỳ chọn: Giữ nguyên ID VM (110)**

Nếu bạn muốn giữ nguyên VM ID 110, chỉ cần:

- Không đổi tên khi zfs receive, giữ nguyên vm-110-disk-0

- Tạo lại VM trên host B với ID 110

qm create 110 --name TenVM --memory 4096 --cores 4 --net0
virtio,bridge=vmbr0

qm set 110 --scsi0 Datastore:vm-110-disk-0

qm set 110 --scsi1 Datastore:vm-110-disk-1

**🔐 Lưu ý bảo mật và kỹ thuật**

- Luôn **shutdown** VM trước khi snapshot để tránh mất dữ liệu.

- Đảm bảo dung lượng ZFS pool trên host B đủ lớn.

- Sử dụng SSH key hoặc xác thực password để thực hiện ssh root@hostB.

- Các VM Windows có thể cần driver tương thích khi thay đổi host.

**✅ Kiểm tra sau khi migrate**

- VM khởi động bình thường trên host mới

- Disk nhận diện đúng dung lượng

- Không phát sinh lỗi từ Proxmox hoặc ZFS

**📚 Tham khảo thêm**

- [Proxmox ZFS Documentation](https://pve.proxmox.com/wiki/ZFS_on_Linux)

- [qm command reference](https://pve.proxmox.com/pve-docs/qm.1.html)
