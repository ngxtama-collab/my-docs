Cấu hình để reboot server thì sẽ tự migrate VM qua server khác:

Datacenter -\> Options -\> HA settings

Đổi shutdown_policy về Migrate

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:6.5in;height:1.88819in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

HA group Sẽ có 2 mode:

Restricted : tương tự Vmware host rules bắt buộc các VM chỉ được ON trên
các host chỉ định.

Nofailback: được quyền chạy trên tất cả các node, nhưng sẽ ưu tiên được
ON trên host có priority lớn nhất

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.33333in;height:5.23958in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

3.  Troubleshoot

Nếu VM bị Error thì có thể set disable trên GUI

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:6.26042in;height:2.33333in"
alt="A screenshot of a virtual machine AI-generated content may be incorrect." />

Hoặc dùng command:

ha-manager set vm:\<id\> --state disabled
