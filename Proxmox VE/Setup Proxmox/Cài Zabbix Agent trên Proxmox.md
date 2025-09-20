**Hướng dẫn cài Zabbix Agent trên Proxmox**

1.  **Cài đặt Zabbix-agnet.**

Cài sẵn proxmox trên node

Bắt đầu bằng cách cập nhật danh sách gói trên máy chủ từ xa: *sudo apt
update*

Sau đó tải xuống tệp Debian của kho lưu trữ Zabbix bằng lệnh như sau :
*wget* [*https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+focal_all.deb*](https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+focal_all.deb)

Sau đó kích hoạt nó bằng lệnh dpkg như sau: *sudo dpkg -i
zabbix-release_5.0-1+focal_all.deb*

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:6.23958in;height:1.48958in"
alt="A screen shot of a computer program AI-generated content may be incorrect." />

Khi đã có kho lưu trữ, hãy cài đặt tác nhân Zabbix: *sudo apt install
zabbix-agent*

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:3.37153in"
alt="A screenshot of a computer program AI-generated content may be incorrect." />

Khi quá trình cài đặt hoàn tất, hãy kiểm tra xem daemon Zabbix-agent có
đang chạy hay không như sau: *sudo systemctl status zabbix-agent*

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image3.png"
style="width:6.5in;height:2.56389in"
alt="A computer screen with white text AI-generated content may be incorrect." />

Thay đổi đối với tệp cấu hình tại /etc/zabbix/zabbix_agentd.conf: *sudo
vim /etc/zabbix/zabbix_agentd.conf*

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image4.png"
style="width:6.5in;height:0.43819in" />

Thay đổi cấu hình trong file ở một số chỗ như sau:

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image5.png"
style="width:3.35417in;height:0.72917in"
alt="A black background with white numbers AI-generated content may be incorrect." />

Lưu các thay đổi và thoát khỏi tệp. Sau đó, khởi động lại dịch vụ đại lý
Zabbix để các thay đổi được thực hiện: *sudo systemctl restart
zabbix-agent*

*Cài tool lm-sensors:*

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image6.png"
style="width:6.5in;height:2.42361in"
alt="A screen shot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image7.png"
style="width:6.5in;height:1.24167in"
alt="A black screen with white text AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image8.png"
style="width:5.41667in;height:6.35417in"
alt="A screenshot of a computer program AI-generated content may be incorrect." />

***2.*** **Add host Zabbix server**

Truy cập địa chỉ ip Zabbix server qua tài khoản Admin/zabbix.

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image9.png"
style="width:6.5in;height:2.76736in"
alt="A screenshot of a computer AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image10.png"
style="width:6.5in;height:6.02083in"
alt="A screenshot of a computer program AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image11.png"
style="width:6.5in;height:3.125in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

3\. Check nhiệt độ CPU

Tạo file userparameter_cputemp.conf theo đường dẫn sau
/etc/zabbix/zabbix_agentd.d/

Copy đoạn code sau vào file vừa tạo được:

*UserParameter=basicCPUTemp.min,sensors \| grep Core \| awk -F'\[:+°\]'
'{if(min==""){min=\$3}; if(\$3\<min) {min=\$3};} END {print min}'*  
*UserParameter=basicCPUTemp.max,sensors \| grep Core \| awk -F'\[:+°\]'
'{if(max==""){max=\$3}; if(max\<\$3) {max=\$3};} END {print max}'*  
*UserParameter=basicCPUTemp.avg,sensors \| grep Core \| awk -F'\[:+°\]'
'{avg+=\$3}END{print avg/NR}'*

*sudo systemctl restart zabbix-agent*

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image12.png"
style="width:5.9375in;height:4.23958in"
alt="A screenshot of a web page AI-generated content may be incorrect." /><img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image13.png"
style="width:6.5in;height:1.98472in"
alt="A graph with lines and numbers AI-generated content may be incorrect." />
