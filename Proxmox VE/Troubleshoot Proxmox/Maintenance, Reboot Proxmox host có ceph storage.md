Bước 1: Kiểm tra ceph storage

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:6.5in;height:3.82708in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Bước 2: Set maintenance ceph

noout,nobackfill,noscrube,nodeep-scrub,norebalance,norecover

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:3.94028in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:6.5in;height:3.62778in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Bước 3: Migrate các VM trên host qua node khác. Trường hợp VM đã được
add vào HA thì có thể reboot trực tiếp host

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image4.png"
style="width:4.10417in;height:3.625in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Bước 4: Kiểm tra lại các OSD đã up lại, bỏ maintenance ceph, trạng thái
đã OK thì mới làm tiếp host khác

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image5.png"
style="width:6.5in;height:2.68681in"
alt="A computer screen with white text AI-generated content may be incorrect." />
