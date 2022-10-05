# [Protocols]
[Getting to know more about network protocols and how they function.]

## Key terminology
[Network Protocol: A set of rules and standards that organizes the way communications in a network happen.

UDP: User Datagram Protocol, is one of the two main network protocols that works on the transport layer of OSI model. It uses a technique that's called "Fire and forget", because it allows sending the data without delivery verification. That makes UDP faster and requiers more resources, but in the same time less reliable than TCP. Therefore, UDP is best used in broadcasting and live communications.

TCP: Transmission Control Protocol, is the other one of the two main network protocols that works on the transport layer of OSI model. It's described as a connection-oriented protocol, meaning it establishes a connection first and then starts communication. In order to do that, TCP relies on a "Threeway handshake" technique. That three-way handshake starts with a synchronization signal from a client to a server, then the server responds to that sending an acknowledgment/synchronization signal, and ending with the client sending a final acknowledgment signal to the server. Through maintaining the connection between the two hosts, TCP enabels delivery verification and data recovery, which makes it more reliable but also more resource demanding and slower than UDP.

Address Resolution Protocol (ARP): A network protocol that works between the data link and network layers of OSI model. It enabels translating IP adresses into physical adresses (MAC adresses).

Spanning Tree Protocol (STP): A network protocol on the data link layer of OSI model. Its function is to avoid network loops from happening when there are redundant paths in the network, by defining one path between the two nodes.

Hypertext Transfer Protocol (HTTP): A network protocol on the application layer. It organizes transmitting hypermedia, such as; HTML documents through the network. The server usually listens to HTTP requests on port 80.

Hypertext Transfer Protocol Secure (HTTPS): Exactly like HTTP, except that the communication in HTTPS is encrypted using TLS. The server listens to HTTPS requests on port 443.

Transport Layer Security (TLS): A network protocol on the application layer of OSI model. TLS takes care of encrypting the data being tansfered providing secure communication between hosts.

Internet Group Management Protocol (IGMP): A network protocol that works on the network layer of OSI model. It allows sharing the same IP between several devices in order for them to get the same packets. It is used for multicasting in for example; gaming, streaming and video conferencing.

Digital Subscriber Line (DSL): A network protocol related to DSL technology that works on the physical layer of OSI model and allows the translation between digital and analoug signals.

Password Authentication Protocol (PAP): A network protocol on the session layer of OSI model and works as an authentication protocol based on passwords.

Independent Computing Architecture (ICA): A network protocol on the presentation layer of OSI model. It provides specifications of the communication between clients and servers in way that's independent of platforms.

Internet Engineering Task Force (IETF): The organization that's responsible for making up the standards of internet protocols.]

## Exercise
1. In order for your protocol to be acknowleged by IETF it has to meet the following requirements:
A) It should determine message encoding. 
B) It should determine message sizing. 
C) It should handle message formatting. 
D) It should determine message timing. 
E) It should take message delivery options in consideration. 

2. Installed Wireshark on both my own Windows system and my Ubuntu VM and captured traffic on both. On th GIU of Wireshark on my Windows I noticed that some traffic was depending on UDP protocol, which was apparently traffic from the Zoom session as it was open back then (See attached photos in "Results" section).

### Sources
[1. https://www.spiceworks.com/tech/networking/articles/tcp-vs-udp/#:~:text=Transmission%20control%20protocol%20(TCP)%20and,UDP%20prioritizes%20speed%20and%20efficiency.

2. https://www.cbtnuggets.com/blog/technology/networking/12-most-important-protocols-to-learn-for-networking

3. https://www.geeksforgeeks.org/how-address-resolution-protocol-arp-works/

4. https://en.wikipedia.org/wiki/Spanning_Tree_Protocol

5. https://nl.wikipedia.org/wiki/Transport_Layer_Security

6. https://www.geeksforgeeks.org/what-is-igmpinternet-group-management-protocol/

7. https://www.cloudflare.com/learning/network-layer/what-is-igmp/

8. https://en.wikipedia.org/wiki/Digital_subscriber_line

9. https://en.wikipedia.org/wiki/Independent_Computing_Architecture

10. https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force#Operations

11. https://www.geeksforgeeks.org/elements-of-network-protocol/]

### Overcome challenges
[]

### Results
![Default_gateway](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/c49592b5e799e589c45c8354fd31c3c8dd26d33c/00_includes/Networking/Default_gateway.png)
![Wireshark_Linux](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/c49592b5e799e589c45c8354fd31c3c8dd26d33c/00_includes/Networking/Wireshark_Linux.png)
![Wireshark_Windows](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/c49592b5e799e589c45c8354fd31c3c8dd26d33c/00_includes/Networking/Wireshark_Windows.png)