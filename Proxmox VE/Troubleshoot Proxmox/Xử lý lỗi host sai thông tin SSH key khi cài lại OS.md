**Xử lý lỗi host sai thông tin SSH key khi cài lại OS**

Nguyên nhân: sau khi cài lại OS, các thông tin public key cũ của host
trong cluster đã không còn chính xác

Truy cập Shell trên GUI

![A computer screen with white text AI-generated content may be
incorrect.](media/image1.png){width="6.5in"
height="2.6326388888888888in"}

Migrate VM

![A screenshot of a computer AI-generated content may be
incorrect.](media/image2.png){width="6.5in"
height="4.065277777777778in"}

Cách xử lý:

1\. Remove thông tin ssh

ssh-keygen -f \"/etc/ssh/ssh_knows_hosts\" -R \"hostname or IP\"

2\. Add lại thông tin key ssh

ssh -o \'HostKeyAlias=\<hostname\>\' root@\<IP\>

Rồi nhập pass root
