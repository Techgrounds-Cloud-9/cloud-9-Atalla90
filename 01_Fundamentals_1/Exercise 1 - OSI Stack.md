# [OSI Stack]
[Understanding both OSI and TCP/IP models, their use cases and the differences between them.]

## Key terminology
[OSI: Open Systems Interconnection model, a standard model that was developed between the late 1790s and the early 1980s and released in 1983. It illustrates the framework in which systems can communicate with each other over the network. It consists of 7 layers; phisical layer, data link layer, network layer, transport layer, session layer, presentation layer and application layer. OSI model is mainly used for troubleshooting purposes, due to its ability to isolate the problem.

Physical layer: The first and lowermost layer of the OSI model. It handels the connection between different nodes on the network, defining the kind of connection (wired/wireless) and its physical elements. It takes care of transmitting raw binary data and also of bit rate control.

Data link layer: The second layer of the OSI model. It takes care of transfering data between nodes on the same LAN, by breaking up the packets into frames. It performs only within the same LAN. It consists of two sublayers; LLC and MAC. Data link layer performs flow control and error control in communication between nodes on the same LAN.

LLC: Logical Link Control, is the upper sublayer of the data link layer in OSI model. It enabels different network protocols to coexist in the same network by multiplexing (uniting) them. It can optionally provide flow-control and error management too.

MAC: Media Access Control, is the bottom sublayer of the data link layer in OSI model. It uses MAC addresses to organize the access to the media.

MAC Address: An address consists of 12 hexadecimal digits divided into six groups of two's. It serves as a unique identifier for a network interface controller (NIC) in a LAN.

NIC: Network Interface Controller, is the unit in the hardware of a computer that's responsible for connecting the computer with networks.

LAN: Local Area Network, is a computer network where nodes in the same local area are interconnected.

Segment: A piece of data that's a part of the original data after being broken up in the trasport layer and with a header added to it. The header contains information about the data, the source port and the destination port.

Packet: A segment from the session layer after adding IP headers to it in the network layer.

Network layer: The third layer of the OSI model. It has on the sending end two functions, one is breaking up the segments into packets, preparing them to be transfered through the data link layer, and the other is using IP addresses to route the packet through the best path for it across the network. On the receiving end it reassembles the packets rebuilding the segments.

Transport layer: The fourth layer of the OSI model. On the sending end it receives a chunk of data from the session layer and breaks it into segments to facilitate the transfer. On the receiving end it reassembles the segments back into data that can be used in the session layer. Transport layer performs flow control and error control in communication between end hosts.

Node: Any device on the network, including hosts and network devices.

Host: Any system on the network. It can perform as a server, a client or both.

Server: A system on the network that offers services upon client's request.

Client: A system on the network that uses the services available on a server.

Flow Control: Controling the flow of data between a sender and a receiver, making sure it's suitable for the receiver's capacity.

Error Control: Making sure the data has been transmitted correctly, and requesting it again if not.

Session layer: The fifth layer of the OSI model. It establishes and maintains channels of communication between hosts. It receives and manipulates the data between the transport layer and the presentation layer. It performs many functions, with making checkpoints for recovery as the most important one.

Presentation layer: The sixth layer of the OSI model. It works between the session layer and application layer, defining and performing encoding and encrypting as well as decoding and decrypting to transform the data into transmittable form on the sending end, or into presentable form on the receiving end.

Application layer: The seventh and uppermost layer of the OSI model. It enables the basic functions of the communication between a host and a client by providing several protocols, such as; HTTP, FTP and DNS.

TCP/IP model: Transmission Control Protocol/Internet Protocol, a standard model that was developed by the US daprtment of defence in 1960s. It illustrates the framework in which systems can communicate with each other over the network. It consists of 4 layers; Process/Application layer, Host-to-Host/Transport layer, Internet layer and Network Access/Link layer. It is considered simpeler and more reliable than OSI model. That's beacause of the fact that it was designed to be a functional model that addresses and solves specific communication problems based on standard protocols.

Network Access/Link layer: The first and lowermost layer of TCP/IP model. It takes care of the physical transmission of data. It corresponds to the combination of the physical layer and the data link layer in OSI model.

Internet layer: The second layer of TCP/IP model. It takes care of transmitting the data through the whole network, by defining some crucial protocols. It corresponds to the network layer in OSI model.

Host-to-Host/Transport layer: The fourth layer of TCP/IP model. It is responsible for the flawless trassmision of data between two ends based on two main protocols; TCP and UDP. It corrsponds to the trasport layer in OSI model.

Application layer: The fourth and uppermost layer of TCP/IP model. It does the job of the top three layers in OSI model; appliction layer, presentation layer and session layer. It's responsible for node-to-node communication.]

## Exercise
Studied OSI and TCP/IP models, their use cases and the differences between them.

### Sources
[1. https://www.imperva.com/learn/application-security/osi-model/

2. https://en.wikipedia.org/wiki/OSI_model

3. https://en.wikipedia.org/wiki/Data_link_layer

4. https://en.wikipedia.org/wiki/Network_packet

5. https://www.geeksforgeeks.org/application-layer-in-osi-model/

6. https://www.geeksforgeeks.org/presentation-layer-in-osi-model/

7. https://www.geeksforgeeks.org/session-layer-in-osi-model/

8. https://www.geeksforgeeks.org/difference-between-segments-packets-and-frames/

9. https://www.geeksforgeeks.org/tcp-ip-model/

10. https://www.geeksforgeeks.org/tcp-ip-model/]

### Overcome challenges
[]

### Results
[]
