# [OSI Stack]
[Understanding both OSI and TCP/IP models, their use cases and the differences between them.]

## Key terminology
[OSI: Open Systems Interconnection model, a standard model that was developed between the late 1790s and the early 1980s and released in 1983. It illustrates the framework in which systems can communicate with each other over the network. It consists of 7 layers: phisical layer, data link layer, network layer, transport layer, session layer, presentation layer and application layer. OSI model is mainly used for troubleshooting purposes, due to its ability to isolate the problem.

Physical layer: The first layer of the OSI model. It handels the connection between different nodes on the network, defining the kind of connection (wired/wireless) and its physical elements. It takes care of transmitting raw binary data and also of bit rate control.

Data link layer: The second layer of the OSI model. It takes care of transfering data between hosts on the same LAN, by breaking up the packets into frames. It performs only within the same LAN. It consists of two sublayers: LLC and MAC.

LLC: Logical Link Control, is the upper sublayer of the data link layer in OSI model. It enabels different network protocols to coexist in the same network by multiplexing (uniting) them. It can optionally provide flow-control and error management too.

MAC: Media Access Control, is the bottom sublayer of the data link layer in OSI model. It uses MAC addresses to organize the access to the media.

MAC Address: An address consists of 12 hexadecimal digits divided into six groups of two's. It serves as a unique identifier for a network interface controller (NIC) in a LAN.

NIC: Network Interface Controller, is the unit in the hardware of a computer that's responsible for connecting the computer with networks.

LAN: Local Area Network, is a computer network where nodes in the same local area are interconnected.

Packet: Is a segment of the broken up message that is sent through the network. A packet contains a part of the message as well as control information to enable the delivery.

Network layer: The third layer of the OSI model. It has on the sending end two functions, one is breaking up the message into packets to facilitate the transfer, and the other is using IP addresses to route the packet through the best path for it across the network. On the receiving end it reassembles the packets to rebuild the message.

]

## Exercise
### Sources
[1. https://www.imperva.com/learn/application-security/osi-model/
2. https://en.wikipedia.org/wiki/OSI_model
3. https://en.wikipedia.org/wiki/Data_link_layer
4. https://en.wikipedia.org/wiki/Network_packet
5. ]

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

### Results
[Describe the result of the exercise. An image can speak more than a thousand words, include one when this wisdom applies.]
