# [Firewalls]
[Getting to know different kinds of firewalls and their functions.]

## Key terminology
[Firewall: A piece of software or hardware that monitors and filters the incoming and outgoing traffic on a certain host or on the network in general.

Stateful Firewall: A firewall that monitors and filters the traffic based on all its aspects, besides the nature of the data and channels of communication. It's considered as a more security efficient way to protect the host or the network from melicious attacks.

Stateless Firewall: A firewall that monitors and filters packets based on the basic parameters of each packet, like its source and its destination. It's considered a more time efficient way to protect the host or the network from melicious attacks.

Software Firewall: A program that works as a firewall and can be installed on a host individualy.

Hardware Firewall: A device that's installed between the hosts and and the gateway. It's provides more security to the network as it monitors the network traffic as a whole, but it's also more expensive and requires experience to be maintained.]

## Exercise
On my Linux machine, I configured the firewall to allow all outgoing traffic and deny all incoming traffic except for SSH connections. Afterwards, I wasn;t able to send an HTTP request to the web server on my Linux machine from my Windows machine.
### Sources
[1. https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-22-04

2. https://www.cdw.com/content/cdw/en/articles/security/stateful-versus-stateless-firewalls.html#:~:text=Stateful%20firewalls%20are%20capable%20of,preset%20rules%20to%20filter%20traffic.

3. https://www.geeksforgeeks.org/difference-between-hardware-firewall-and-software-firewall/

4. https://www.techtarget.com/searchsecurity/feature/The-five-different-types-of-firewalls]

### Overcome challenges
[]

### Results
![Apache_working](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/cc9dd57919f750bc17b0c58a11d6541444e77171/00_includes/Networking/Apache_working.png)
![Unable_to_reach_web_server](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/cc9dd57919f750bc17b0c58a11d6541444e77171/00_includes/Networking/Unable_to_reach_web_server.png)