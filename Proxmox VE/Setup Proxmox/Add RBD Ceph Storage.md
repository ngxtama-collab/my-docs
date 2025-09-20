1 . Cài Ceph package cho OS

![A screenshot of a computer AI-generated content may be
incorrect.](media/image1.png){width="6.5in"
height="3.0347222222222223in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image2.png){width="6.5in"
height="4.607638888888889in"}

Chỉ cài đặt các packages ko cần configure thêm

Copy ceph.client.admin.keyring, ceph.conf của cluster Ceph qua node
Proxmox

mkdir /etc/pve/priv/ceph

ceph.conf -\> /etc/pve/

ceph.client.admin.keyring -\> mkdir /etc/pve/priv/

Tạo RBD storage

![A screenshot of a computer AI-generated content may be
incorrect.](media/image3.png){width="6.5in"
height="3.1770833333333335in"}
