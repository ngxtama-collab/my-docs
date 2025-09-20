1\. Hướng Dẫn Cài Đặt Proxmox VE:

Chọn Install Proxmox VE

![A screenshot of a computer AI-generated content may be
incorrect.](media/image1.png){width="6.5in" height="4.75in"}

![A screenshot of a computer AI-generated content may be
incorrect.](media/image2.png){width="6.5in"
height="4.8909722222222225in"}

Chọn disk boot

![A screenshot of a computer AI-generated content may be
incorrect.](media/image3.png){width="6.5in"
height="4.888194444444444in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image4.png){width="6.5in"
height="4.892361111111111in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image5.png){width="6.5in"
height="4.8909722222222225in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image6.png){width="6.5in"
height="4.888194444444444in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image7.png){width="6.5in"
height="1.9534722222222223in"}

2\. Hướng dẫn cấu hình network trên Proxmox VE

**Cấu hình cơ bản sử dụng Bridge**

Bridge sẽ tạo ra một card mạng vmbr0 kết nối với card enp94s0f0np0 được
cấu hình trên: /etc/network/interfaces

![A computer screen with white text AI-generated content may be
incorrect.](media/image8.png){width="4.239583333333333in"
height="3.5208333333333335in"}

Trên giao diện web của Proxmox vào phần network

![A screenshot of a computer AI-generated content may be
incorrect.](media/image9.png){width="6.5in"
height="1.3652777777777778in"}

**Cấu hình sử dụng Linux Bond:**

Khi bạn có nhiều NIC trên máy chủ, Bond sẽ gộp các NIC này lại để tăng
tốc độ xử lý cũng như khả năng chịu lỗi.

![A computer screen shot of white text AI-generated content may be
incorrect.](media/image10.png){width="5.270833333333333in"
height="4.541666666666667in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image11.png){width="6.5in"
height="1.457638888888889in"}

Cấu hình sử dụng OVS Bond:

Để cấu hình sử dụng OVS bond cần cài gói openvswitch-switch

![A screenshot of a computer error message AI-generated content may be
incorrect.](media/image12.png){width="6.21875in"
height="2.6145833333333335in"}

*root@pve-1:\~# apt install openvswitch-switch*

![A computer screen with white text AI-generated content may be
incorrect.](media/image13.png){width="5.166666666666667in"
height="4.614583333333333in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image14.png){width="6.5in"
height="1.3993055555555556in"}

3\. Join Cluster cho 3 node Proxmox

Trước tiên cần tạo vlan riêng cho 1 số đường để tránh bị nghẽn

vlan70 dùng cho MGT - vlan71 dùng cho Cluster - vlan72 dùng cho Ceph

![A computer screen shot of a black screen AI-generated content may be
incorrect.](media/image15.png){width="6.1875in"
height="7.208333333333333in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image16.png){width="6.5in"
height="1.8451388888888889in"}

Trước khi join cluster phải đảm bảo network giữa các vlan đã thông

Vào phần Datacenter - Cluster - Create Cluster

Cluster name: LVS

Cluster Network chọn vlan71

![A screenshot of a computer AI-generated content may be
incorrect.](media/image17.png){width="6.5in"
height="1.926388888888889in"}

Sau khi tạo xong cluster sẽ hiển thị phần **Join Information** copy toàn
bộ

![A screenshot of a computer AI-generated content may be
incorrect.](media/image18.png){width="5.208333333333333in"
height="1.9166666666666667in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image19.png){width="6.5in"
height="2.0097222222222224in"}

Ở node 2 click  **Join Cluster** dán đoạn vừa copy vào phần Cluster
Network chọn vlan71 và điền pass của Proxmox

![A screenshot of a computer AI-generated content may be
incorrect.](media/image20.png){width="5.75in"
height="2.1979166666666665in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image21.png){width="6.5in"
height="2.942361111111111in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image22.png){width="6.5in"
height="3.314583333333333in"}

4\. CEPH STORAGE

![A screenshot of a computer AI-generated content may be
incorrect.](media/image23.png){width="6.5in"
height="3.152083333333333in"}![A screenshot of a computer AI-generated
content may be
incorrect.](media/image24.png){width="2.3854166666666665in"
height="1.15625in"}![A screenshot of a computer AI-generated content may
be incorrect.](media/image25.png){width="6.5in"
height="4.605555555555555in"}

Chọn vlan72 cho Ceph

![A screenshot of a computer AI-generated content may be
incorrect.](media/image26.png){width="6.5in"
height="4.614583333333333in"}

Tạo Ceph OSD

Tạo Ceph OSD cho 10 node vào \"Ceph - OSD - Create: OSD\"

![A screenshot of a computer AI-generated content may be
incorrect.](media/image27.png){width="6.260416666666667in"
height="2.8645833333333335in"}

Tạo xong OSD cho 10 node sẽ hiển thị như trên hình

![A group of numbers on a white background AI-generated content may be
incorrect.](media/image28.png){width="6.5in" height="1.75625in"}

Tạo Pool cho 10 OSD vừa tạo \"Ceph - Pools - Create\"

Mặc định ở đây sẽ là Size 3 - Min 2

![A screenshot of a computer AI-generated content may be
incorrect.](media/image29.png){width="6.270833333333333in"
height="2.9583333333333335in"}

Sau khi tạo xong sẽ có 1 Storage mới là HDD-STORAGE

![A screenshot of a computer AI-generated content may be
incorrect.](media/image30.png){width="2.9270833333333335in"
height="1.65625in"}

Tạo VM trên Proxmox

![A screenshot of a computer AI-generated content may be
incorrect.](media/image31.png){width="6.020833333333333in"
height="0.9270833333333334in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image32.png){width="6.5in"
height="4.595138888888889in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image33.png){width="6.5in"
height="4.601388888888889in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image34.png){width="6.5in"
height="4.616666666666666in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image35.png){width="6.5in"
height="4.613194444444445in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image36.png){width="6.5in"
height="4.579861111111111in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image37.png){width="6.5in"
height="4.59375in"}![A screenshot of a computer AI-generated content may
be incorrect.](media/image38.png){width="6.5in"
height="4.595138888888889in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image39.png){width="6.5in"
height="4.595138888888889in"}
