Mục đích: dựng Proxy Server để expose VM Console VNC của Proxmox

Cấu hình: với  3 File trong thư mục /etc/nginx/conf.d

1\.  console.conf :  file mô tả location

*server {  
    listen 10521 ssl;  \#open port ứng với 2 octet cuối cuối IP node
proxmox  
    include   /etc/nginx/conf.d/websocket-proxy.conf;  \#đường dẫn đến
file option  
    include   /etc/nginx/conf.d/ssl.conf;  \#đường dẫn đến file SSL  
    server_name consolehcm-q2.longvan.net
www.consolehcm-q2.longvan.net;    
    error_log  /var/log/nginx/proxy-error.log warn;  
\#    location ~ pvemanagerlib { return 404;}  
        client_max_body_size 0;  
        rewrite_log on;  
    location / {  
                if (\$args ~ (.\*)(vmid=10521)(.\*)) { \#so sánh
argument từ URL   
                        set \$args \$1vmid=\$3; \#set giá trị với cho
argument  
                }  
                if (\$args ~ (.\*)(node=longvan-)(.\*)) {  
                        set \$args \$1node=\$3;  
                }  
                proxy_pass https://10.80.105.21:8006/?\$args;  
                location /pve/ {  
                        proxy_pass https://10.80.105.21:8006/pve/;  
                }  
                location /api2 {  
                        rewrite
/api2/(.\*)/nodes/longvan-(.\*)/qemu/10521(\w+)\\?.\*/status/current
/api2/\$1/nodes/\$2/qemu/\$3/status/current break;   
                        rewrite
/api2/(.\*)/nodes/longvan-(.\*)/qemu/10521(\w+)\\?.\*/vncproxy 
/api2/\$1/nodes/\$2/qemu/\$3/vncproxy break;  
                        rewrite
/api2/(.\*)/nodes/longvan-(.\*)/qemu/10521(\w+)\\?.\*/vncwebsocket 
/api2/\$1/nodes/\$2/qemu/\$3/vncwebsocket break;  
                        proxy_pass https://10.80.105.21:8006;  
                }  
                location /novnc/ {  
                        proxy_pass https://10.80.105.21:8006/novnc/;  
                }  
    }  
}*

Giải thích quy trình sử dụng:

Portal -\> Proxy Server -\> Proxmox Node

B1: Portal xác định VMID và host đang giữ VM đó

B2: thêm prefix và gửi request với URL đến Proxy server

<img
src="C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE\images/media/image1.png"
style="width:6.5in;height:1.83125in"
alt="A close-up of a computer code AI-generated content may be incorrect." />

B3: Nginx Proxy Server xử lý URL

*if (\$args ~ (.\*)(vmid=10521)(.\*)) {  
set \$args \$1vmid=\$3;  
}  
if (\$args ~ (.\*)(node=longvan-)(.\*)) {  
set \$args \$1node=\$3;  
}*

Sau khi so sánh và set \$args thì sẽ có thông tin sau:

*console=kvm&novnc=1&vmid=118&vmname=null&node=hp1-n1&resize=scale*

Sau đó rewrite lại URL để pass xuống Proxmox Node:

*rewrite
/api2/(.\*)/nodes/longvan-(.\*)/qemu/10521(\w+)\\?.\*/status/current
/api2/\$1/nodes/\$2/qemu/\$3/status/current break;*  
*rewrite /api2/(.\*)/nodes/longvan-(.\*)/qemu/10521(\w+)\\?.\*/vncproxy
 /api2/\$1/nodes/\$2/qemu/\$3/vncproxy break;*  
*rewrite
/api2/(.\*)/nodes/longvan-(.\*)/qemu/10521(\w+)\\?.\*/vncwebsocket
 /api2/\$1/nodes/\$2/qemu/\$3/vncwebsocket break;*

2\. ssl.conf: đường dẫn SSL file

*ssl_protocols TLSv1 TLSv1.1 TLSv1.2;  
ssl_certificate /etc/nginx/[longvan.net](http://longvan.net)-2023.crt; 
\#path to file cert  
ssl_certificate_key
/etc/nginx/[longvan.net](http://longvan.net)-2023.key; \#path to file
key  
ssl_verify_client off;  
ssl_session_cache  builtin:1000  shared:SSL:10m;  
ssl_ciphers  RC4:HIGH:!aNULL:!MD5;  
ssl_prefer_server_ciphers on;*

3\. websocket-proxy.conf : option cho proxy

*proxy_http_version 1.1;  
proxy_set_header Upgrade \$http_upgrade;  
proxy_set_header Connection "upgrade";  
proxy_redirect off;  
proxy_buffering off;  
proxy_connect_timeout  3600s;  
proxy_read_timeout  3600s;  
proxy_send_timeout  3600s;*
