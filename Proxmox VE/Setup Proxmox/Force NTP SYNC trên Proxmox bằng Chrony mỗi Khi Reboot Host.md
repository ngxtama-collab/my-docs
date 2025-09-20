**Force NTP SYNC trên Proxmox bằng Chrony mỗi Khi Reboot Host**

Có thể dùng 2 lệnh dưới đây để đồng bộ time,\
chronyc -a makestep   : dùng trong trường hợp server lệch time nhiều (
trên 1000s), đồng bộ ngay lập tức\
chronyd -q \'server [pool.ntp.org](http://pool.ntp.org) iburst\'   : 
mất khoảng 3p để đồng bộ

*touch /etc/rc.local\
chmod +x /etc/rc.local\
printf \'%s\\n\' \'#!/bin/bash\' \'\' \'sh /etc/init.d/chrony stop\'
\'chronyd -q \'pool
[2.debian.pool.ntp.org](http://2.debian.pool.ntp.org)\'\' \'sh
/etc/init.d/chrony start\' \'\' \'exit 0\' \| sudo tee -a /etc/rc.local\
cat /etc/rc.local*

#thêm 3 dòng dưới đây vào file

*sh /etc/init.d/chrony stop\
chronyd -q \'pool
[2.debian.pool.ntp.org](http://2.debian.pool.ntp.org)\'\
sh /etc/init.d/chrony start*

![A screen shot of a computer screen AI-generated content may be
incorrect.](media/image1.png){width="5.479166666666667in"
height="2.8020833333333335in"}

Tạo file system cho rc-local

nano /etc/systemd/system/rc-local.service

*\[Unit\]\
Description=/etc/rc.local Compatibility\
Documentation=man:systemd-rc-local-generator(8)\
ConditionFileIsExecutable=/etc/rc.local\
After=[network.target](http://network.target)*

*\[Service\]\
Type=forking\
ExecStart=/etc/rc.local start\
TimeoutSec=0\
RemainAfterExit=yes\
GuessMainPID=no*

*\[Unit\]\
After=[network-online.target](http://network-online.target)\
\[Service\]\
StandardOutput=journal+console\
StandardError=journal+console*

![A screen shot of a computer AI-generated content may be
incorrect.](media/image2.png){width="6.5in"
height="3.4902777777777776in"}

Enable rc.local

*systemctl enable rc-local\
systemctl start rc-local\
systemctl status rc-local*

Set lệch time để kiểm tra kết quả

![A black screen with white text AI-generated content may be
incorrect.](media/image3.png){width="6.5in"
height="0.9111111111111111in"}

Service chrony đang đồng bộ tự động nên không set được time, phải stop
chrony\
Hình dưới service rc-local đang chạy

![A computer screen with text on it AI-generated content may be
incorrect.](media/image4.png){width="6.5in"
height="1.6819444444444445in"}

Reboot

Sau khi reboot xong thì thời gian chưa đồng bộ ngay lập tức Service
chrony và rc-local ở trạng thái activiting

![A screenshot of a computer program AI-generated content may be
incorrect.](media/image5.png){width="6.5in"
height="3.9923611111111112in"}

Sau gần 3p thì thời gian mới được đồng bộ

Thay chronyd -q \'pool
[2.debian.pool.ntp.org](http://2.debian.pool.ntp.org)\' bằng chronyc -a
makestep thì thời gian được đồng bộ ngay

Sửa lại file cấu hình như sau

![A screenshot of a computer screen AI-generated content may be
incorrect.](media/image6.png){width="4.21875in" height="2.65625in"}
