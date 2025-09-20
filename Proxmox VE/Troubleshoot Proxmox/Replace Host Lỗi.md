Nguyên nhân: Do host lỗi disk boot. không thể phục hồi

Xử lý:

1.  Cài lại OS mới với cùng IP và hostname

2.  Cấu hình lại mô hình network ở đây dùng OVS

Lưu ý: add  deb <http://download.proxmox.com/debian/pve> buster
pve-no-subscription vào /etc/apt/sources.list

*apt update*\
*apt install openvswitch-switch -y*\
*apt install ifupdown2 -y*

Bước 1: pvecm delnode namenode

Bước 2: Stop service corosync và bỏ node bị lỗi trong file
/etc/corosync/corosync.conf trên 1 host bất kỳ đang hoạt động bình
thường

![A computer screen with text on it AI-generated content may be
incorrect.](media/image1.png){width="6.5in"
height="2.561111111111111in"}![A screen shot of a computer AI-generated
content may be incorrect.](media/image2.png){width="5.177083333333333in"
height="7.177083333333333in"}

Bước 3: Start lại corosync service để cluster bỏ node lỗi trên GUI

Bước 4: Restart lại pve-cluster service để cluster bỏ host khỏi cấu hình
/etc/pve/.members

Bước 5: Rejoin lại host bằng GUI

Bước 6: Sau khi rejoin thì kiểm tra lại

![A computer screen with white text AI-generated content may be
incorrect.](media/image3.png){width="3.0625in"
height="1.3854166666666667in"}

Bước 6: UP lại ceph storage

![A screenshot of a computer AI-generated content may be
incorrect.](media/image4.png){width="6.5in"
height="2.839583333333333in"}

Chọn đúng version với cluster đang chạy

Copy file ceph.conf và ceph.client.admin.keyring vào host mới

![A screen shot of a computer AI-generated content may be
incorrect.](media/image5.png){width="6.5in"
height="0.7930555555555555in"}

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

![A screen shot of a computer AI-generated content may be
incorrect.](media/image6.png){width="5.989583333333333in"
height="1.6041666666666667in"}![A black background with white text
AI-generated content may be incorrect.](media/image7.png){width="6.5in"
height="2.092361111111111in"}

Bước 7: Start lại Service OSD và KT đã OK chưa

![A black screen with white text AI-generated content may be
incorrect.](media/image8.png){width="6.5in"
height="1.0604166666666666in"}![A screen shot of a computer AI-generated
content may be incorrect.](media/image9.png){width="5.916666666666667in"
height="1.7708333333333333in"}
