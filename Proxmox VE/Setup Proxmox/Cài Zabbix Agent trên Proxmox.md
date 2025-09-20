**Hướng dẫn cài Zabbix Agent trên Proxmox**

1.  **Cài đặt Zabbix-agnet.**

Cài sẵn proxmox trên node

Bắt đầu bằng cách cập nhật danh sách gói trên máy chủ từ xa: *sudo apt
update*

Sau đó tải xuống tệp Debian của kho lưu trữ Zabbix bằng lệnh như sau :
*wget* [*https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+focal_all.deb*](https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+focal_all.deb)

Sau đó kích hoạt nó bằng lệnh dpkg như sau: *sudo dpkg -i
zabbix-release_5.0-1+focal_all.deb*

![A screen shot of a computer program AI-generated content may be
incorrect.](media/image1.png){width="6.239583333333333in"
height="1.4895833333333333in"}

Khi đã có kho lưu trữ, hãy cài đặt tác nhân Zabbix: *sudo apt install
zabbix-agent*

![A screenshot of a computer program AI-generated content may be
incorrect.](media/image2.png){width="6.5in"
height="3.3715277777777777in"}

Khi quá trình cài đặt hoàn tất, hãy kiểm tra xem daemon Zabbix-agent có
đang chạy hay không như sau: *sudo systemctl status zabbix-agent*

![A computer screen with white text AI-generated content may be
incorrect.](media/image3.png){width="6.5in"
height="2.563888888888889in"}

Thay đổi đối với tệp cấu hình tại /etc/zabbix/zabbix_agentd.conf: *sudo
vim /etc/zabbix/zabbix_agentd.conf*

![](media/image4.png){width="6.5in" height="0.43819444444444444in"}

Thay đổi cấu hình trong file ở một số chỗ như sau:

![A black background with white numbers AI-generated content may be
incorrect.](media/image5.png){width="3.3541666666666665in"
height="0.7291666666666666in"}

Lưu các thay đổi và thoát khỏi tệp. Sau đó, khởi động lại dịch vụ đại lý
Zabbix để các thay đổi được thực hiện: *sudo systemctl restart
zabbix-agent*

*Cài tool lm-sensors:*

![A screen shot of a computer AI-generated content may be
incorrect.](media/image6.png){width="6.5in"
height="2.423611111111111in"}![A black screen with white text
AI-generated content may be incorrect.](media/image7.png){width="6.5in"
height="1.2416666666666667in"}![A screenshot of a computer program
AI-generated content may be
incorrect.](media/image8.png){width="5.416666666666667in"
height="6.354166666666667in"}

***2.*** **Add host Zabbix server**

Truy cập địa chỉ ip Zabbix server qua tài khoản Admin/zabbix.

![A screenshot of a computer AI-generated content may be
incorrect.](media/image9.png){width="6.5in"
height="2.767361111111111in"}![A screenshot of a computer program
AI-generated content may be incorrect.](media/image10.png){width="6.5in"
height="6.020833333333333in"}![A screenshot of a computer AI-generated
content may be incorrect.](media/image11.png){width="6.5in"
height="3.125in"}

3\. Check nhiệt độ CPU

Tạo file userparameter_cputemp.conf theo đường dẫn sau
/etc/zabbix/zabbix_agentd.d/

Copy đoạn code sau vào file vừa tạo được:

*UserParameter=basicCPUTemp.min,sensors \| grep Core \| awk
-F\'\[:+°\]\' \'{if(min==\"\"){min=\$3}; if(\$3\<min) {min=\$3};} END
{print min}\'*\
*UserParameter=basicCPUTemp.max,sensors \| grep Core \| awk
-F\'\[:+°\]\' \'{if(max==\"\"){max=\$3}; if(max\<\$3) {max=\$3};} END
{print max}\'*\
*UserParameter=basicCPUTemp.avg,sensors \| grep Core \| awk
-F\'\[:+°\]\' \'{avg+=\$3}END{print avg/NR}\'*

*sudo systemctl restart zabbix-agent*

![A screenshot of a web page AI-generated content may be
incorrect.](media/image12.png){width="5.9375in"
height="4.239583333333333in"}![A graph with lines and numbers
AI-generated content may be incorrect.](media/image13.png){width="6.5in"
height="1.9847222222222223in"}
