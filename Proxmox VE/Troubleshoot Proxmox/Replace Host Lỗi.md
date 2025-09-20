Nguyên nhân: Do host lỗi disk boot. không thể phục hồi

Xử lý:

1.  Cài lại OS mới với cùng IP và hostname

2.  Cấu hình lại mô hình network ở đây dùng OVS

Lưu ý: add  deb <http://download.proxmox.com/debian/pve> buster
pve-no-subscription vào /etc/apt/sources.list

*apt update*  
*apt install openvswitch-switch -y*  
*apt install ifupdown2 -y*

Bước 1: pvecm delnode namenode

Bước 2: Stop service corosync và bỏ node bị lỗi trong file
/etc/corosync/corosync.conf trên 1 host bất kỳ đang hoạt động bình
thường

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:6.5in;height:2.56111in"
alt="A computer screen with text on it AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:5.17708in;height:7.17708in"
alt="A screen shot of a computer AI-generated content may be incorrect." />

Bước 3: Start lại corosync service để cluster bỏ node lỗi trên GUI

Bước 4: Restart lại pve-cluster service để cluster bỏ host khỏi cấu hình
/etc/pve/.members

Bước 5: Rejoin lại host bằng GUI

Bước 6: Sau khi rejoin thì kiểm tra lại

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:3.0625in;height:1.38542in"
alt="A computer screen with white text AI-generated content may be incorrect." />

Bước 6: UP lại ceph storage

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image4.png"
style="width:6.5in;height:2.83958in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Chọn đúng version với cluster đang chạy

Copy file ceph.conf và ceph.client.admin.keyring vào host mới

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image5.png"
style="width:6.5in;height:0.79306in"
alt="A screen shot of a computer AI-generated content may be incorrect." />

**Lưu ý: Nếu Node lỗi là MON-MGR node trong ceph cluster thì không cần
copy 2 file**

**Với MON sẽ chạy chung 1 keyring ceph.mon.keyring trong thư mục
/etc/pve/priv**

Sau khi cài lại OS thì sẽ chưa có file này, nhưng sau khi join cluster
thì corosync sẽ đồng bộ các file config này. Nên sẽ phải tạo lại service
ceph-mon cho host.

Trường hợp tạo lại trên GUI có thể sẽ báo lỗi là mon đã tồn tại thì thực
hiện command sau để remove mon cũ:

*ceph mon remove {mon-id}*

Sau đó add lại mon service trên GUI

**\*\*\* Các trường hợp phát sinh khác chưa rõ thì phải báo lại cho quản
lý cấp trên**

Check thông tin OSD cũ

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image6.png"
style="width:5.98958in;height:1.60417in"
alt="A screen shot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image7.png"
style="width:6.5in;height:2.09236in"
alt="A black background with white text AI-generated content may be incorrect." />

Bước 7: Start lại Service OSD và KT đã OK chưa

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image8.png"
style="width:6.5in;height:1.06042in"
alt="A black screen with white text AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image9.png"
style="width:5.91667in;height:1.77083in"
alt="A screen shot of a computer AI-generated content may be incorrect." />
