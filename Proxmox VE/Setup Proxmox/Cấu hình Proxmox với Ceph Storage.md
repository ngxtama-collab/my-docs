**Cấu hình Proxmox với Ceph Storage**

Trong bài hướng dẫn này, chúng ta sẽ tìm hiểu cách cấu hình Proxmox với
Ceph Storage để tạo một giải pháp lưu trữ phân tán, có tính sẵn sàng cao
cho môi trường ảo hóa của bạn.

**Giới thiệu về Proxmox và Ceph**

Proxmox VE (Virtual Environment) là một nền tảng ảo hóa mã nguồn mở dựa
trên Debian Linux, kết hợp KVM (Kernel-based Virtual Machine) và LXC
(Linux Containers) để quản lý máy ảo và container.

Ceph là một hệ thống lưu trữ phân tán, có khả năng tự quản lý và tự sửa
chữa, được thiết kế để cung cấp hiệu suất, độ tin cậy và khả năng mở
rộng vượt trội. Ceph cung cấp lưu trữ dạng đối tượng, khối và tệp tin
trong một nền tảng thống nhất.

**Yêu cầu hệ thống**

Để triển khai Proxmox với Ceph, bạn cần:

- Ít nhất 3 node Proxmox để đảm bảo tính sẵn sàng cao và dự phòng dữ
  liệu

- Mỗi node cần có ít nhất 16GB RAM

- CPU hỗ trợ ảo hóa (Intel VT-x/AMD-V)

- Ít nhất 2 card mạng trên mỗi node (1 cho mạng quản lý, 1 cho mạng
  Ceph)

- Ổ cứng SSD cho OSD journals (tùy chọn nhưng được khuyến nghị)

- Ổ cứng HDD hoặc SSD cho OSD data

**Cài đặt Proxmox VE**

Trước khi cấu hình Ceph, bạn cần cài đặt Proxmox VE trên tất cả các
node:

1.  Tải xuống ISO Proxmox VE từ trang web chính thức:
    <https://www.proxmox.com/downloads>

2.  Tạo USB boot và cài đặt Proxmox VE trên tất cả các node

3.  Cấu hình mạng cho mỗi node, đảm bảo chúng có thể giao tiếp với nhau

4.  Tạo Proxmox Cluster bằng cách chạy lệnh sau trên node đầu tiên:

pvecm create clustername

Sau đó, thêm các node còn lại vào cluster:

\# Trên node đầu tiên

pvecm nodes

pvecm updatecerts --force

\# Trên các node còn lại

pvecm add IP_NODE_DAU_TIEN

**Cấu hình mạng cho Ceph**

Ceph yêu cầu một mạng riêng biệt để đảm bảo hiệu suất và bảo mật. Chỉnh
sửa file /etc/network/interfaces trên mỗi node để thêm mạng Ceph:

auto eno2

iface eno2 inet static

address 10.10.10.X/24 \# X là số node

post-up echo 1 \> /proc/sys/net/ipv4/ip_forward

Khởi động lại dịch vụ mạng:

systemctl restart networking

**Cài đặt Ceph trên Proxmox**

Proxmox VE đã tích hợp sẵn các công cụ để cài đặt và quản lý Ceph. Thực
hiện các bước sau trên tất cả các node:

**1. Cài đặt gói Ceph**

apt update

apt install proxmox-ceph

**2. Tạo Ceph Monitor**

Trên node đầu tiên, tạo Ceph Monitor:

pveceph init --network 10.10.10.0/24

Trên các node còn lại, thêm Ceph Monitor:

pveceph mon create

**3. Tạo Ceph Manager**

Trên mỗi node, tạo Ceph Manager:

pveceph mgr create

**4. Tạo Ceph OSD**

Trên mỗi node, tạo Ceph OSD (Object Storage Daemon) cho mỗi ổ đĩa bạn
muốn sử dụng cho Ceph:

\# Liệt kê các ổ đĩa có sẵn

lsblk

\# Tạo OSD

pveceph osd create /dev/sdX

Nếu bạn muốn sử dụng SSD cho journal và HDD cho data:

pveceph osd create /dev/sdX --journal /dev/sdY

**5. Tạo Ceph Pool**

Tạo Ceph Pool để lưu trữ dữ liệu:

pveceph pool create poolname --pg_num 128 --pgp_num 128

**Cấu hình Ceph làm backend cho Proxmox**

Sau khi đã thiết lập Ceph, bạn có thể sử dụng nó làm backend lưu trữ cho
Proxmox:

**1. Tạo RBD Storage**

Trong giao diện web Proxmox, điều hướng đến Datacenter \> Storage \> Add
\> RBD và cấu hình như sau:

- ID: ceph-rbd

- Pool: poolname

- Content: Disk image, Container

**2. Tạo CephFS (tùy chọn)**

Nếu bạn muốn sử dụng CephFS cho lưu trữ tệp tin:

\# Tạo MDS (Metadata Server)

pveceph mds create

\# Tạo CephFS

pveceph fs create --name cephfs --pg_num 128 --add-storage

**Kiểm tra trạng thái Ceph**

Để kiểm tra trạng thái của cụm Ceph:

ceph status

ceph health detail

ceph osd tree

ceph df

**Bảo trì và khắc phục sự cố**

**Thay thế OSD bị lỗi**

\# Đánh dấu OSD là out

ceph osd out osd.X

\# Dừng OSD

systemctl stop ceph-osd@X

\# Xóa OSD khỏi CRUSH map

ceph osd crush remove osd.X

\# Xóa OSD

ceph auth del osd.X

ceph osd rm osd.X

\# Tạo OSD mới

pveceph osd create /dev/sdY

**Mở rộng cụm Ceph**

Để thêm node mới vào cụm Ceph:

1.  Thêm node mới vào Proxmox Cluster

2.  Cài đặt Ceph trên node mới

3.  Thêm Ceph Monitor và Manager

4.  Tạo OSD mới trên node

**Kết luận**

Bạn đã hoàn thành việc cấu hình Proxmox với Ceph Storage. Giải pháp này
cung cấp:

- Lưu trữ phân tán với khả năng mở rộng cao

- Tính sẵn sàng cao và dự phòng dữ liệu

- Hiệu suất tốt với khả năng tự cân bằng tải

- Khả năng tự sửa chữa khi có lỗi phần cứng

Với Proxmox và Ceph, bạn có một nền tảng ảo hóa mạnh mẽ, đáng tin cậy và
có khả năng mở rộng cao cho môi trường doanh nghiệp.
