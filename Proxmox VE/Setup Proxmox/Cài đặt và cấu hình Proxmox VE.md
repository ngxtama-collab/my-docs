1\. Hướng Dẫn Cài Đặt Proxmox VE:

Chọn Install Proxmox VE

<img
src="../images/1.1/1.png"
style="width:6.5in;height:4.75in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:4.89097in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Chọn disk boot

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:6.5in;height:4.88819in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image4.png"
style="width:6.5in;height:4.89236in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image5.png"
style="width:6.5in;height:4.89097in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image6.png"
style="width:6.5in;height:4.88819in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image7.png"
style="width:6.5in;height:1.95347in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

2\. Hướng dẫn cấu hình network trên Proxmox VE

**Cấu hình cơ bản sử dụng Bridge**

Bridge sẽ tạo ra một card mạng vmbr0 kết nối với card enp94s0f0np0 được
cấu hình trên: /etc/network/interfaces

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image8.png"
style="width:4.23958in;height:3.52083in"
alt="A computer screen with white text AI-generated content may be incorrect." />

Trên giao diện web của Proxmox vào phần network

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image9.png"
style="width:6.5in;height:1.36528in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

**Cấu hình sử dụng Linux Bond:**

Khi bạn có nhiều NIC trên máy chủ, Bond sẽ gộp các NIC này lại để tăng
tốc độ xử lý cũng như khả năng chịu lỗi.

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image10.png"
style="width:5.27083in;height:4.54167in"
alt="A computer screen shot of white text AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image11.png"
style="width:6.5in;height:1.45764in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Cấu hình sử dụng OVS Bond:

Để cấu hình sử dụng OVS bond cần cài gói openvswitch-switch

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image12.png"
style="width:6.21875in;height:2.61458in"
alt="A screenshot of a computer error message AI-generated content may be incorrect." />

*root@pve-1:~# apt install openvswitch-switch*

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image13.png"
style="width:5.16667in;height:4.61458in"
alt="A computer screen with white text AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image14.png"
style="width:6.5in;height:1.39931in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

3\. Join Cluster cho 3 node Proxmox

Trước tiên cần tạo vlan riêng cho 1 số đường để tránh bị nghẽn

vlan70 dùng cho MGT - vlan71 dùng cho Cluster - vlan72 dùng cho Ceph

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image15.png"
style="width:6.1875in;height:7.20833in"
alt="A computer screen shot of a black screen AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image16.png"
style="width:6.5in;height:1.84514in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Trước khi join cluster phải đảm bảo network giữa các vlan đã thông

Vào phần Datacenter - Cluster - Create Cluster

Cluster name: LVS

Cluster Network chọn vlan71

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image17.png"
style="width:6.5in;height:1.92639in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Sau khi tạo xong cluster sẽ hiển thị phần **Join Information** copy toàn
bộ

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image18.png"
style="width:5.20833in;height:1.91667in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image19.png"
style="width:6.5in;height:2.00972in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Ở node 2 click  **Join Cluster** dán đoạn vừa copy vào phần Cluster
Network chọn vlan71 và điền pass của Proxmox

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image20.png"
style="width:5.75in;height:2.19792in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image21.png"
style="width:6.5in;height:2.94236in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image22.png"
style="width:6.5in;height:3.31458in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

4\. CEPH STORAGE

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image23.png"
style="width:6.5in;height:3.15208in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image24.png"
style="width:2.38542in;height:1.15625in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image25.png"
style="width:6.5in;height:4.60556in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Chọn vlan72 cho Ceph

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image26.png"
style="width:6.5in;height:4.61458in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Tạo Ceph OSD

Tạo Ceph OSD cho 10 node vào "Ceph - OSD - Create: OSD"

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image27.png"
style="width:6.26042in;height:2.86458in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Tạo xong OSD cho 10 node sẽ hiển thị như trên hình

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image28.png"
style="width:6.5in;height:1.75625in"
alt="A group of numbers on a white background AI-generated content may be incorrect." />

Tạo Pool cho 10 OSD vừa tạo "Ceph - Pools - Create"

Mặc định ở đây sẽ là Size 3 - Min 2

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image29.png"
style="width:6.27083in;height:2.95833in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Sau khi tạo xong sẽ có 1 Storage mới là HDD-STORAGE

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image30.png"
style="width:2.92708in;height:1.65625in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Tạo VM trên Proxmox

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image31.png"
style="width:6.02083in;height:0.92708in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image32.png"
style="width:6.5in;height:4.59514in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image33.png"
style="width:6.5in;height:4.60139in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image34.png"
style="width:6.5in;height:4.61667in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image35.png"
style="width:6.5in;height:4.61319in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image36.png"
style="width:6.5in;height:4.57986in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image37.png"
style="width:6.5in;height:4.59375in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image38.png"
style="width:6.5in;height:4.59514in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image39.png"
style="width:6.5in;height:4.59514in"
alt="A screenshot of a computer AI-generated content may be incorrect." />
