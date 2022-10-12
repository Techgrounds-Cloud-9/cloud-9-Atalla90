# [Network devices]
[Getting to know different kinds of network devices, what they do and on which layer(s) they do it.]

## Key terminology
[Network device: A device that is used for communication purposes between computers on the network.

Access Point (AP): A network device that works on the data link layer of the OSI model. It performs as bridge or as a router. 

Router: A network device that routes the packets through the network. It works on the network layer of the OSI model.

Bridge: A network device that's used to link two hosts or two different LANs forming a larger LAN. It filters the data to addresses before transmission at the hand of dynamic bridge table. It functions on the physical and data link layers of OSI model.

Gateway: A network device that works on the session and transport layers of OSI model. It functions as an entry and an exit point of the data into and from the LAN in its communication with remote networks.

Hub: A network device that works on the physical layer of OSI model. It repeats a signal that it receives on one of its ports out all of its other ports, linking the components of the LAN together. A hub can be passive or active.

Passive hub: A hub that only connects devices by repeating and transmitting the signal from one of them to the others.

Active hub: Active hub is smarter than passive hub, as it can regenerate the signal and strengthen it. It also can monitor and process information. Active hub needs electericity to function and has its own adapter.

Switch: A network device that can be thought of as a multiport bridge. It works on the data link layer of OSI model, transfering packets from one device to the others. A switsh can also have routing funcitionality and therefore also be working on the network layer. In this case it's called a "Multilayer Switch".

Modem: A network device that transforms phone analog signals into digital signals and vice versa.

DHCP: Dynamic Host Configuration Protocol, is a protocol that determines how a DHCP-server automatically issues IP adresses and other configuration information, such as; the default gateway, to client systems.]

## Exercise
Logged in my router's configuration page. Checked the list of the connected devices to my home network and checked the configurations of the DHCP server.
### Sources
[1. https://www.educba.com/types-of-network-devices/

2. https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top

3. https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol]

### Overcome challenges
[]

### Results
![Connected_devices](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/9d5515758b4c2881e617be0515b5af4a53fe5602/00_includes/Networking/Connected_devices.png)
![DHCP_settings(1)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/9d5515758b4c2881e617be0515b5af4a53fe5602/00_includes/Networking/DHCP_settings(1).png)
![DHCP_settings(2)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/9d5515758b4c2881e617be0515b5af4a53fe5602/00_includes/Networking/DHCP_settings(2).png)
![DHCP_CLI](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/bcec479be5ff800ebe5d57bd493fc4992684d2e5/00_includes/Networking/DHCP_CLI.png)