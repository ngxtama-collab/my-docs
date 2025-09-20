**Proxmox Backup Server**

**Setup OS**

a\. Cài trên 1 server từ file ISO <https://www.proxmox.com/en/downloads>

b\. Cài trên Proxmox VE server

add deb deb <http://download.proxmox.com/debian/pbs> bullseye
pbs-no-subscription vào file /etc/apt/sources.list

*apt update  
apt install install proxmox-backup-server*

Sau khi cài đặt có thể truy cập bằng trình duyệt https://\<IP\>:8007

2\. Tạo User

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:6.5in;height:3.81319in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

nhập User/Pass

tích Enabled  và set Expire never

3\. Tạo Datastore

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:2.88681in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:6.32292in;height:2.4375in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image4.png"
style="width:6.35417in;height:2.33333in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Nhập số bản backup gần nhất cần giữ.

Set permission cho User nào được sử dụng Datastore này

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image5.png"
style="width:6.5in;height:2.90139in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

4\. Kết nối đến PVE server

Cấu hình network thông từ PVE server và PBS

Trên PBS chạy command proxmox-backup-manager cert info \| grep
Fingerprint

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image6.png"
style="width:6.5in;height:0.225in" />

Lưu thông tin Fringerint để add vào PVE

Vào Cluster PVE

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image7.png"
style="width:6.5in;height:2.30764in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image8.png"
style="width:6.32292in;height:3.02083in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image9.png"
style="width:6.5in;height:5.22014in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image10.png"
style="width:6.5in;height:1.85625in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

5\. Add Backup Job

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image11.png"
style="width:6.39583in;height:6.48958in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image12.png"
style="width:6.28125in;height:2.82292in"
alt="A screenshot of a note template AI-generated content may be incorrect." />
