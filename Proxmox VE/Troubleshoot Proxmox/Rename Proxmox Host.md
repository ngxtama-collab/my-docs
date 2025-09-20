Edit lại các file sau

/etc/hosts

*10.2.144.21 [prox1-s3.p1.site1.lv](http://prox1-s3.p1.site1.lv)
prox1-s3*

/etc/hostname

[prox1-s3.p1.site1.lv](http://prox1-s3.p1.site1.lv)

*hostnamectl set-hostname
[prox1-s3.p1.site1.lv](http://prox1-s3.p1.site1.lv)\
rm -f /var/lib/rrdcached/db/pve2-node/\<old pve\>\
rm -rf /var/lib/rrdcached/db/pve2-storage/\<old pve\>*

Reboot lại Server
