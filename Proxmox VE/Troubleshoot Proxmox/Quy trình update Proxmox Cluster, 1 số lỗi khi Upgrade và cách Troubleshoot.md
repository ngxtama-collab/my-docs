**Quy trình update Proxmox Cluster, 1 số lỗi khi Upgrade và cách
Troubleshoot**

Mô tả: Do Proxmox sẽ thường xuyên update fix bug và thêm tính năng, nên
cluster production cũng phải thường xuyên update lên version mới nhất

Yêu cầu và Quy trình thực hiện:

B1. Kiểm tra Cluster

- Ceph cluster health phải OK, hoặc các pg \"active\"

- Các nodes trong cluster hoạt động bình thường

B2. Thực hiện Backup config

- Thực hiện backup các file config của Node theo hướng dẫn
  <https://projects.longvan.net/projects/lvss/wiki/5-backup-slash-restore-host>

B3. Migrate VM ra khỏi node trước khi thực hiện chạy update

B4. Thực hiện tắt HA service

- Cách 1: Stop service pve-ha-lrm lần lượt trên các node trong cluster.
  Sau đó lần lượt stop service pve-ha-crm trên các node trong cluster

- Cách 2: Remove toàn bộ VM khỏi HAGroup

**\*Lý do: Theo cơ chế self fencing của Proxmox nếu Cluster enable HA
service, trong 1 khoảng thời gian không nhận health check từ các node
khác sẽ tự đồng reboot lần lượt các node trong cluster.**

B5. Maintenance Ceph storage

B6. Update lần lượt từng server

- Thực hiện kiểm tra đã có repo Non-subcription đã add hay chưa

- Chạy Update trên giao diện (tương ứng command \"apt update\")

![A screenshot of a computer AI-generated content may be
incorrect.](media/image1.png){width="6.5in"
height="3.4319444444444445in"}

- Sau đó thực hiện tiếp Upgrade: ở bước này sẽ hiện 1 console VNC của
  node hiện lên -\> Nhấn \"Y\" -\> Enter để thực hiện upgrade

**\*Lưu ý: ở bước này có thể xảy ra tình trạng khi update OVS thì
service openvswitch-switch sẽ bị down làm cho service networking bị lỗi
như sau khi check**

***systemctl status networking***

**\"ovs-vsctl: unix:/usr/local/var/run/openvswitch/db.sock: database
connection failed\"**

**Biểu hiện là không thể ping từ trong server ra ngoài**

Cách xử lý: truy cập vào server thực hiện command sau

*/etc/init.d/openvswitch-switch restart*\
*ifreload -a*

**\*\*Lưu ý: Trong quá trình update, trên console VNC sẽ đến 1 bước xác
nhận có ghi đè lên file config trước đó. Ở bước này mặc định default=N
nên có thể nhất Enter bỏ qua, tuyệt đối ko chọn Y**

**\-\-\--**

**Lỗi một số package cài đặt không chính xác khi update**

**Biêu hiện: do package pve-cluster chưa update hoàn tất nên khi truy
cập GUI sẽ chập chờn, các thông tin cluster khi xem trên GUI sẽ không
hiện đầy đủ**

![A screenshot of a computer AI-generated content may be
incorrect.](media/image2.png){width="6.5in"
height="5.352777777777778in"}

Cách xử lý là chạy command

*dpkg \--configure -a*

Nhưng có thể sẽ hiện lỗi như hình do process dpkg đã bị lock khi update,
fix bằng cách kill process đó

*lsof /var/lib/dkpg/lock #để check process PID*\
*kill \<PID\>*

![](media/image3.png){width="6.5in" height="1.3715277777777777in"}

**Sau đó tiến hành chạy tiếp**

*dpkg \--configure -a*

B7. Kiểm tra cluster

Sau khi quá trình upgrade hoàn tất thì kiểm tra lại các service

- pve-ha-lrm và pve-ha-crm có thể sẽ tự Start nên phải Stop ngay

- Các service ceph sẽ restart lại, nên phải đảm bảo service ceph-osd
  trên node đó đã Start, quá trình recovery hoàn tất thì mới thực hiện
  tiếp

- Kiểm tra service corosync đã Start, các node trong cluster đã joined
  hết

- Kiểm tra giao diện có hiện đầy đủ các nodes

**\*\*\*Lưu ý: trường hợp upgrade xong nhưng có thể sẽ xảy ra tình trạng
corosync member ko joined, thì thực hiện reboot lại node đó**

![A screenshot of a computer AI-generated content may be
incorrect.](media/image4.png){width="3.8020833333333335in"
height="3.2604166666666665in"}
