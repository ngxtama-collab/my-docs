Cấu hình để reboot server thì sẽ tự migrate VM qua server khác:

Datacenter -\> Options -\> HA settings

Đổi shutdown_policy về Migrate

![A screenshot of a computer AI-generated content may be
incorrect.](media/image1.png){width="6.5in"
height="1.8881944444444445in"}

HA group Sẽ có 2 mode:

Restricted : tương tự Vmware host rules bắt buộc các VM chỉ được ON trên
các host chỉ định.

Nofailback: được quyền chạy trên tất cả các node, nhưng sẽ ưu tiên được
ON trên host có priority lớn nhất

![A screenshot of a computer AI-generated content may be
incorrect.](media/image2.png){width="6.333333333333333in"
height="5.239583333333333in"}

3.  Troubleshoot

Nếu VM bị Error thì có thể set disable trên GUI

![A screenshot of a virtual machine AI-generated content may be
incorrect.](media/image3.png){width="6.260416666666667in"
height="2.3333333333333335in"}

Hoặc dùng command:

ha-manager set vm:\<id\> \--state disabled
