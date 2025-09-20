Bước 1: Tìm chính xác ID của VM cần restore

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:6.5in;height:2.64861in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Bước 2: Cần restore VM lên host nào thì truy cập đúng host đó và chọn
storage BACKUP-STORE và tìm các bản restore của VMID

VD: restore VM lên host quanta2-n1

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:2.69375in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Bước 3: Chọn chính xác ngày cần restore và nhấn nút Restore

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:6.5in;height:2.62014in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Bước 4: Sau khi nhấn Restore sẽ hiện popup các thông tin

Source: thông tin bản Backup

Storage: Storage sẽ lưu disk của VM mới

VM ID: chọn 1 ID cho VM Restore, chắc chắn là ID duy nhất không trùng
với VM đã có, nếu trùng thì khung VM ID sẽ hiện đỏ

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image4.png"
style="width:4.78125in;height:2.54167in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

VM ID đã tồn tài

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image5.png"
style="width:4.78125in;height:2.54167in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Tiến hành Restore

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image6.png"
style="width:6.5in;height:4.09444in"
alt="A screenshot of a computer program AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image7.png"
style="width:6.5in;height:4.09028in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

**Bước 6: Sau khi restore process hoàn tất, sẽ tạo ra 1 VM mới, phải
thay đổi tên VM để tránh bị nhầm lẫn với VM cũ**

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image8.png"
style="width:6.5in;height:2.14653in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image9.png"
style="width:6.5in;height:2.29097in" />

Bước 7: Disable hoặc đổi cấu hình network VM trước khi ON lên, tránh bị
trùng IP với VM cũ đang chạy

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image10.png"
style="width:6.5in;height:2.26181in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image11.png"
style="width:5.88542in;height:2.69792in"
alt="A screenshot of a computer AI-generated content may be incorrect." />
