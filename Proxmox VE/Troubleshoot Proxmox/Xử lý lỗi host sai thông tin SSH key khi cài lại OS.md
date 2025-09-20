**Xử lý lỗi host sai thông tin SSH key khi cài lại OS**

Nguyên nhân: sau khi cài lại OS, các thông tin public key cũ của host
trong cluster đã không còn chính xác

Truy cập Shell trên GUI

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:6.5in;height:2.63264in"
alt="A computer screen with white text AI-generated content may be incorrect." />

Migrate VM

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:4.06528in"
alt="A screenshot of a computer AI-generated content may be incorrect." />

Cách xử lý:

1\. Remove thông tin ssh

ssh-keygen -f "/etc/ssh/ssh_knows_hosts" -R "hostname or IP"

2\. Add lại thông tin key ssh

ssh -o 'HostKeyAlias=\<hostname\>' root@\<IP\>

Rồi nhập pass root
