# [IP addresses]
[Understanding the nature of IP addresses.]

## Key terminology
[IP address: Internet Protocol address, a number identifing a device and used for communications between that device and other devices on the network.

Public IP address: The IP address assigned to the LAN and is used for its communications with the internet.

Private IP address: The IP address assigned to a host on the LAN and is used for internal communications within the LAN.

IPv4: The fourth version of IP addresses. IPv4 address is a 32-bits address represented as 4 octets containing decimal digits and seperated with dots.

IPv6: The sixth version of IP addresses. IPv6 address is a 128-bits address respresented as 8 colon(:) seperated groups, with each group containing 4 hexadecimal digits. IPv6 has many advantages over IPv4, most importantly, its so much larger addresses space.

NAT: Network Address Translation, is the process that happens on the router or the firewall to translate between public (global) and private (local) IP addresses according to a NAT table. It also does port number masking and translation.

Static IP address: An IP address that's assigned by a service provider. It can't be changed or modified.

Dynamic IP address: An IP address that's assigned by a DHCP server. It can be changed any time. It's also more secure than static IP address.]

## Exercise
Looked up my public and private IP addresses and learned the following:

A) The public IP addresses of both my laptop and my mobile are the same address. That's because this is the IP address of my local network assigned to the router by the service provider.

B) The private IP addresses of my laptop and my mobile are however different from each other. That's bacause these are their IP addresses within my laocal network as assigned by the DHCP server.
When tried to change my mobile's private IP address to be the same as my laptop's private IP address, the DHCP server accepted that and then gave my laptop another private IP address when restarted the router, because two different devices can not have the same identifing number on the same local network.
When tried to change my mobile's private IP address to an address outside of my network, the DHCP server denied the operation, as the assigned private IP address of a device has to be within the ranges specified on the DHCP server.

### Sources
[1. https://www.networkworld.com/article/3588315/what-is-an-ip-address-and-what-is-your-ip-address.html

2. https://www.lifewire.com/what-is-a-public-ip-address-2625974

3. https://www.geeksforgeeks.org/differences-between-ipv4-and-ipv6/

4. https://www.geeksforgeeks.org/network-address-translation-nat/

5. https://www.geeksforgeeks.org/difference-between-static-and-dynamic-ip-address/]

### Overcome challenges
[]

### Results
![Public_IP_laptop](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/fb870f02f39c7183cde0dc654b5bcd339371973b/00_includes/Networking/Public_IP_laptop.png)
![Public_IP_mobile](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/fb870f02f39c7183cde0dc654b5bcd339371973b/00_includes/Networking/Public_IP_mobile.png)
![Pirvate_IP_laptop&mobile](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/fb870f02f39c7183cde0dc654b5bcd339371973b/00_includes/Networking/Private_IP_laptop&mobile.png)
![Mobile_IP_changed_to_laptop](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/fb870f02f39c7183cde0dc654b5bcd339371973b/00_includes/Networking/Mobile_IP_changed_to_laptop.png)
![Mobile_IP_change_outside_trial](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/fb870f02f39c7183cde0dc654b5bcd339371973b/00_includes/Networking/Mobile_IP_change_outside_trial.png)