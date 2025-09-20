Bước 1: Kiểm tra ceph storage

![A screenshot of a computer AI-generated content may be
incorrect.](media/image1.png){width="6.5in"
height="3.8270833333333334in"}

Bước 2: Set maintenance ceph

noout,nobackfill,noscrube,nodeep-scrub,norebalance,norecover

![A screenshot of a computer AI-generated content may be
incorrect.](media/image2.png){width="6.5in"
height="3.9402777777777778in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image3.png){width="6.5in"
height="3.6277777777777778in"}

Bước 3: Migrate các VM trên host qua node khác. Trường hợp VM đã được
add vào HA thì có thể reboot trực tiếp host

![A screenshot of a computer AI-generated content may be
incorrect.](media/image4.png){width="4.104166666666667in"
height="3.625in"}

Bước 4: Kiểm tra lại các OSD đã up lại, bỏ maintenance ceph, trạng thái
đã OK thì mới làm tiếp host khác

![A computer screen with white text AI-generated content may be
incorrect.](media/image5.png){width="6.5in"
height="2.6868055555555554in"}
