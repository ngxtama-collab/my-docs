Bước 1: Tìm chính xác ID của VM cần restore

![A screenshot of a computer AI-generated content may be
incorrect.](media/image1.png){width="6.5in"
height="2.6486111111111112in"}

Bước 2: Cần restore VM lên host nào thì truy cập đúng host đó và chọn
storage BACKUP-STORE và tìm các bản restore của VMID

VD: restore VM lên host quanta2-n1

![A screenshot of a computer AI-generated content may be
incorrect.](media/image2.png){width="6.5in" height="2.69375in"}

Bước 3: Chọn chính xác ngày cần restore và nhấn nút Restore

![A screenshot of a computer AI-generated content may be
incorrect.](media/image3.png){width="6.5in"
height="2.620138888888889in"}

Bước 4: Sau khi nhấn Restore sẽ hiện popup các thông tin

Source: thông tin bản Backup

Storage: Storage sẽ lưu disk của VM mới

VM ID: chọn 1 ID cho VM Restore, chắc chắn là ID duy nhất không trùng
với VM đã có, nếu trùng thì khung VM ID sẽ hiện đỏ

![A screenshot of a computer AI-generated content may be
incorrect.](media/image4.png){width="4.78125in"
height="2.5416666666666665in"}

VM ID đã tồn tài

![A screenshot of a computer AI-generated content may be
incorrect.](media/image5.png){width="4.78125in"
height="2.5416666666666665in"}

Tiến hành Restore

![A screenshot of a computer program AI-generated content may be
incorrect.](media/image6.png){width="6.5in"
height="4.094444444444444in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image7.png){width="6.5in"
height="4.090277777777778in"}

**Bước 6: Sau khi restore process hoàn tất, sẽ tạo ra 1 VM mới, phải
thay đổi tên VM để tránh bị nhầm lẫn với VM cũ**

![A screenshot of a computer AI-generated content may be
incorrect.](media/image8.png){width="6.5in"
height="2.1465277777777776in"}![](media/image9.png){width="6.5in"
height="2.2909722222222224in"}

Bước 7: Disable hoặc đổi cấu hình network VM trước khi ON lên, tránh bị
trùng IP với VM cũ đang chạy

![A screenshot of a computer AI-generated content may be
incorrect.](media/image10.png){width="6.5in"
height="2.2618055555555556in"}![A screenshot of a computer AI-generated
content may be
incorrect.](media/image11.png){width="5.885416666666667in"
height="2.6979166666666665in"}
