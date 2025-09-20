**Proxmox Backup Server**

**Setup OS**

a\. Cài trên 1 server từ file ISO <https://www.proxmox.com/en/downloads>

b\. Cài trên Proxmox VE server

add deb deb <http://download.proxmox.com/debian/pbs> bullseye
pbs-no-subscription vào file /etc/apt/sources.list

*apt update\
apt install install proxmox-backup-server*

Sau khi cài đặt có thể truy cập bằng trình duyệt https://\<IP\>:8007

2\. Tạo User

![A screenshot of a computer AI-generated content may be
incorrect.](media/image1.png){width="6.5in"
height="3.8131944444444446in"}

nhập User/Pass

tích Enabled  và set Expire never

3\. Tạo Datastore

![A screenshot of a computer AI-generated content may be
incorrect.](media/image2.png){width="6.5in"
height="2.8868055555555556in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image3.png){width="6.322916666666667in"
height="2.4375in"}![A screenshot of a computer AI-generated content may
be incorrect.](media/image4.png){width="6.354166666666667in"
height="2.3333333333333335in"}

Nhập số bản backup gần nhất cần giữ.

Set permission cho User nào được sử dụng Datastore này

![A screenshot of a computer AI-generated content may be
incorrect.](media/image5.png){width="6.5in"
height="2.901388888888889in"}

4\. Kết nối đến PVE server

Cấu hình network thông từ PVE server và PBS

Trên PBS chạy command proxmox-backup-manager cert info \| grep
Fingerprint

![](media/image6.png){width="6.5in" height="0.225in"}

Lưu thông tin Fringerint để add vào PVE

Vào Cluster PVE

![A screenshot of a computer AI-generated content may be
incorrect.](media/image7.png){width="6.5in"
height="2.307638888888889in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image8.png){width="6.322916666666667in"
height="3.0208333333333335in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image9.png){width="6.5in"
height="5.220138888888889in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image10.png){width="6.5in"
height="1.85625in"}

5\. Add Backup Job

![A screenshot of a computer AI-generated content may be
incorrect.](media/image11.png){width="6.395833333333333in"
height="6.489583333333333in"}![A screenshot of a note template
AI-generated content may be
incorrect.](media/image12.png){width="6.28125in"
height="2.8229166666666665in"}
