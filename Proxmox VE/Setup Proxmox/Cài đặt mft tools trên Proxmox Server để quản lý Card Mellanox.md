1\. Kiểm tra header version

uname -r

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:3.07292in;height:0.375in" />

2\. Cài đặt các package cần thiết

apt update && apt install gcc make dkms unzip pve-headers-6.2.16-3-pve
-y

3\. Tải file mft

wget
<https://www.mellanox.com/downloads/MFT/mft-4.22.1-307-x86_64-deb.tgz>

Lưu ý: version có thể thay đổi

4\. Cài đặt mft

*tar xzvf mft-4.22.1-307-x86_64-deb.tgz*  
*cd mft-4.22.1-307-x86_64-deb/*  
*./install*  
*language-text*

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image2.png"
style="width:6.5in;height:1.39653in"
alt="A screen shot of a computer AI-generated content may be incorrect." />

Start service

root@prox7-s3:~/mft-4.22.1-307-x86_64-deb# mst start

Starting MST (Mellanox Software Tools) driver set  
Loading MST PCI module - Success  
Loading MST PCI configuration module - Success  
Create devices  
Unloading MST PCI module (unused) - Success  
language-text  
Show device

root@prox7-s3:~/mft-4.22.1-307-x86_64-deb# mst status

MST modules:  
------------  
    MST PCI module is not loaded  
    MST PCI configuration module loaded  
MST devices:  
------------  
/dev/mst/mt4117_pciconf0         - PCI configuration cycles access.  
                                   domain:bus:dev.fn=0000:05:00.0
addr.reg=88 data.reg=92 cr\_[bar.gw](http://bar.gw)\_offset=-1  
                                   Chip revision is: 00  
language-text  
flint -d /dev/mst/mt4117_pciconf0 query  
Image type:            FS3  
FW Version:            14.24.1000  
FW Release Date:       26.11.2018  
Product Version:       14.24.1000  
Rom Info:              type=UEFI version=14.17.11 cpu=AMD64  
                       type=PXE version=3.5.603 cpu=IA32  
Description:           UID                GuidsNumber  
Base GUID:             b8599f0300b3d7dc        8  
Base MAC:              b8599fb3d7dc            8  
Image VSD:             N/A  
Device VSD:            N/A  
PSID:                  DEL0000000006  
Security Attributes:   N/A  
language-text 
