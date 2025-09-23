# Ceph Storage

## 1. Cài Ceph package cho OS

![Ceph Install 1](../images/media/2.1/1.png)  
![Ceph Install 2](../images/media/2.1/2.png)

Chỉ cài đặt các packages, không cần configure thêm.

Copy `ceph.client.admin.keyring`, `ceph.conf` của cluster Ceph qua node Proxmox:

```bash
mkdir /etc/pve/priv/ceph
```

- `ceph.conf` → `/etc/pve/`  
- `ceph.client.admin.keyring` → `/etc/pve/priv/`

---

## 2. Tạo RBD storage

![Create RBD Storage](../images/media/2.1/3.png)
