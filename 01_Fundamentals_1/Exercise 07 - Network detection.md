# [Network detection]
[Analyzing the network traffic using Nmap and Wireshark.]

## Key terminology
[Port: The end point of a connection. This is where a packet arrives at its destination.

Network latency: The time it takes the packet to arrive from its source to its destination.

Keepalive: Is an instruction attached to a signal to keep the connection between two ends open.]

## Exercise
A) Scanned the host's traffic of my Linux machine using Nmap, and the output was:

1- The date and time when the mapping started.

2- The scanned host IP address.

3- The state of the host and the network latency.

4- The number of closed ports.

5- The ports open for traffic.

B) Analyzed the network's traffic on my Windows machine with Wireshark when opening a web browser and found that there are a lot of packets being exchanged between my host system and other remote addresses. Packets are numbered with source, destination, packet length, protocol and information like instructions of the packet and ports of both source and destination provided. Most of the packets are exchanged under TCP protocol.

### Sources
[1. https://www.cyberciti.biz/security/nmap-command-examples-tutorials/

2. https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/

3. https://en.wikipedia.org/wiki/Keepalive]

### Overcome challenges
[]

### Results
![Nmap_report](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ea3eec65660866d98290958da22217b1b55680b2/00_includes/Networking/Nmap_report.png)
![Wireshark_Windows](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ea3eec65660866d98290958da22217b1b55680b2/00_includes/Networking/Wireshark_Windows(2).png)