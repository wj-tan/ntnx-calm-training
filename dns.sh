ip_dns_list="@@{DNS_SERVER}@@"

nic_device_name=$(nmcli -t -f Device,Type d | cut -d ':' -f 1 | head -n 1)
nic_connection_name=$(nmcli -t -f NAME,DEVICE con show --active | grep "$device_name" | cut -d ':' -f 1)

nmcli con mod "$nic_connection_name" ipv6.ignore-auto-dns yes
nmcli con mod "$nic_connection_name" ipv4.ignore-auto-dns yes
nmcli con mod "$nic_connection_name" ipv4.dns "$ip_dns_list"
nmcli con down "$nic_connection_name" && nmcli con up "$nic_connection_name"
