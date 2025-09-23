1 . Cài Ceph package cho OS

<img
src="../images/media/2.1/1.png"
style="width:6.5in;height:3.03472in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:4.60764in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Chỉ cài đặt các packages ko cần configure thêm

Copy ceph.client.admin.keyring, ceph.conf của cluster Ceph qua node
Proxmox

mkdir /etc/pve/priv/ceph

ceph.conf -\> /etc/pve/

ceph.client.admin.keyring -\> mkdir /etc/pve/priv/

Tạo RBD storage

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:6.5in;height:3.17708in"
alt="A screenshot of a computer AI-generated content may be incorrect." />
