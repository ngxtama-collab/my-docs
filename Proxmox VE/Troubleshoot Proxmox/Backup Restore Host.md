**BACKUP CONFIG**

Bước 1: Backup File

Backup /var/lib/pve-cluster/

*tar -czf /root/pve-cluster-backup.tar.gz /var/lib/pve-cluster*

Backup /root/.ssh/ , there are two symlinks here to the shared pve
config authorized_keys and authorized_keys.orig, don't worry about these
two yet as they're stored in /var/lib/pve-cluster/

*tar -czf /root/ssh-backup.tar.gz /root/.ssh*

Backup /etc/corosync/

*tar -czf /root/corosync-backup.tar.gz /etc/corosync*

Backup /etc/hosts/

*cp /etc/hosts /root/*

Backup /etc/network/interfaces

*cp /etc/network/interfaces /root/*

Bước 2: Lưu lại các file config này bằng SCP

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:5.98958in;height:1.38542in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

**RESTORE CONFIG**

Bước 1: Cài lại OS, cấu hình Physical network cho đúng với thông tin
trong file networks

Bước 2: Restore

Restore /etc/hosts/

*cp /root/hosts /etc/hosts*

Restore /etc/network/interfaces

*cp /root/interfaces /etc/network/interfaces*

Reboot Server và Kiểm tra service network đã chính xác

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:1.44861in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

*systemctl stop pvestatd.service  
systemctl stop pvedaemon.service  
systemctl stop pve-cluster.service*

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:4.47917in;height:0.80208in"
alt="A screenshot of a computer screen AI-generated content may be incorrect." />

Restore the files in /root/.ssh/

*cd / ; tar -xzf /root/ssh-backup.tar.gz*

Replace /var/lib/pve-cluster/ with your backup copy

*rm -rf /var/lib/pve-cluster*  
*cd / ; tar -xzf /root/pve-cluster-backup.tar.gz*

Replace /etc/corosync/ with your backup copy

*rm -rf /etc/corosync*  
*cd / ; tar -xzf /root/corosync-backup.tar.gz*

Start pve-cluster

*systemctl start pve-cluster.service*

Restore the two ssh symlinks:

*ln -sf /etc/pve/priv/authorized_keys /root/.ssh/authorized_keys*  
*ln -sf /etc/pve/priv/authorized_keys /root/.ssh/authorized_keys.orig*

Start the rest of the services:

*systemctl start pvestatd.service  
systemctl start pvedaemon.service*

Bước 3: Host sử dụng CEPH thì kiểm tra, cài đặt lại như hướng dẫn ở phần
replace host lỗi
