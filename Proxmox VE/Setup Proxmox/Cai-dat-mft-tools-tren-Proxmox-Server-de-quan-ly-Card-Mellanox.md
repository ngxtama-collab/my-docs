# Hướng dẫn cài đặt Mellanox MFT trên Proxmox

## 1. Kiểm tra header version

```bash
uname -r
```

![Header Version](../images/media/image1.png)

## 2. Cài đặt các package cần thiết

```bash
apt update && apt install gcc make dkms unzip pve-headers-6.2.16-3-pve -y
```

## 3. Tải file MFT

```bash
wget https://www.mellanox.com/downloads/MFT/mft-4.22.1-307-x86_64-deb.tgz
```

*Lưu ý: version có thể thay đổi*

## 4. Cài đặt MFT

```bash
tar xzvf mft-4.22.1-307-x86_64-deb.tgz
cd mft-4.22.1-307-x86_64-deb/
./install
```

![Install MFT](../images/media/image2.png)

### Start service

```bash
mst start
```

Kết quả:  

```
Starting MST (Mellanox Software Tools) driver set
Loading MST PCI module - Success
Loading MST PCI configuration module - Success
Create devices
Unloading MST PCI module (unused) - Success
```

### Show device

```bash
mst status
```

Kết quả:  

```
MST modules:
------------
    MST PCI module is not loaded
    MST PCI configuration module loaded

MST devices:
------------
/dev/mst/mt4117_pciconf0 - PCI configuration cycles access.
                           domain:bus:dev.fn=0000:05:00.0 addr.reg=88 data.reg=92 cr_bar.gw_offset=-1
                           Chip revision is: 00
```

### Kiểm tra Firmware

```bash
flint -d /dev/mst/mt4117_pciconf0 query
```

Kết quả:  

```
Image type:            FS3
FW Version:            14.24.1000
FW Release Date:       26.11.2018
Product Version:       14.24.1000
Rom Info:              type=UEFI version=14.17.11 cpu=AMD64
                       type=PXE version=3.5.603 cpu=IA32
Description:           UID                GuidsNumber
Base GUID:             b8599f0300b3d7dc        8
Base MAC:              b8599fb3d7dc            8
Image VSD:             N/A
Device VSD:            N/A
PSID:                  DEL0000000006
Security Attributes:   N/A
```
