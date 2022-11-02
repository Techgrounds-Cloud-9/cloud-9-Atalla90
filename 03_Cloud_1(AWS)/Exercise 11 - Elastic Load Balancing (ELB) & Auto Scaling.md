# [Elastic Load Balancing (ELB) & Auto Scaling]

[Working with ELBs and EC2 Auto scaling.]

## Key terminology

[Elastic Load Balancing (ELB): Distributing the incoming traffic across multiple targets using Load Balancers. The process also involves checking the health of the instances to avoid forwarding traffic to the unhealthy ones.

Application Load Balancer: A Load Balancer that works on Application Layer (layer 7) of OSI model. It distributes the incoming HTTP and HTTPS requests across a specific group of EC2 instances called Target group.

Network Load Balancer: A Load Balancer that works on Transport Layer (layer 4) of OSI model. It distributes the incoming TCP connection requests or UDP requests across a specific group of EC2 instances called Target group.

Gateway Load Balancer:  A Load Balancer that works on Network Layer (layer 3) of OSI model. It offers a single entry and exit point of all the traffic delivering the packets to a third-party appliance for inspection purposes and the distributes it across application instances.

Classic Load Balancer: A Load Balancer that works on Transport Layer (layer 4) of OSI model. This is the old generation of Load Balancers in AWS. It routes the traffic to the available instances based on IP addresses and protocols.

Load Balancer node: An endpoint that represents a Load Balancer in an AZ, where a Load Balancer routes the traffic to.

Internet-facing Load Balancer: A Load Balancer that routes traffic from clients over the internet to the servers in the VPC. That's because the nodes of this LB have public IP addresses and the DNS name of the LB is resolvable to those addresses.

Internal Load Balancer: A Load Balancer that routes traffic only from clients that have access to the VPC, to the servers in the VPC. That's because the nodes of this LB have private IP addresses and the DNS name of the LB is resolvable to those addresses.

Listener: A process that checks for connection requests from clients.

Auto Scaling: An EC2 feature that adapts the number of EC2 instances running an application to the size of the incoming traffic received by a Load Balancer.

Launch Configuration/ Launch Template: The saved configuration of the EC2 instances to be launched. Both Launch Configuration and Launch Template are the same thing, except that Launch templates have more features, such as; the ability to be edited and updated while maintaining all versions. Therefore, AWS recommends always using Launch Templates.

Auto Scaling Group: An EC2 fleet that gets upscaled or downscaled automatically and based on the traffic load. It uses a Launch Configuration or a Launch Template to create its EC2 instances. ASG has a defined minimum, maximum and desired capacities of the EC2 instances.]

## Exercise

1.  
A) Launched an EC2 instance with the provided requirements.  
B) Created an AMI with the name "Web server AMI" from the launched instance.

2. Created an Application Load Balancer with the name "Lab ELB" and all the provided requirements.

3.  
A) Created a Launch Configuration with "Web server AMI".  
B) Created an Auto Scaling Group with the name "Lab ASG", "Lab ELB" Load Balancer, the Launch Configuration that was created in the last step and all the provided requirements.

4. Accessed the web server using the DNS name of "Lab ELB", ran a load test and saw how the number of EC2 instances in the fleet increased (upscaled) automatically in response to the HTTP requests sent to the server via the application load balancer.

### Sources

[1. <https://docs.aws.amazon.com/AmazonECS/latest/userguide/create-application-load-balancer.html>

2. <https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html>

3. <https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html>

4. <https://docs.aws.amazon.com/AmazonECS/latest/userguide/service-auto-scaling.html>

5. <https://docs.aws.amazon.com/AmazonECS/latest/userguide/service-autoscaling-targettracking.html>]

### Overcome challenges

[]

### Results

![Lab_ELB](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/34d837ac4bce8df44f7c07a6ad9d7923e992de63/00_includes/Cloud(AWS)/Lab_ELB.png)  
![Lab_ASG(1)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/34d837ac4bce8df44f7c07a6ad9d7923e992de63/00_includes/Cloud(AWS)/Lab_ASG(1).png)  
![Lab_ASG(2)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/34d837ac4bce8df44f7c07a6ad9d7923e992de63/00_includes/Cloud(AWS)/Lab_ASG(2).png)  
![Launch_Configuration](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/34d837ac4bce8df44f7c07a6ad9d7923e992de63/00_includes/Cloud(AWS)/Launch_Configuration.png)  
![CloudWatch_Metrics](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/34d837ac4bce8df44f7c07a6ad9d7923e992de63/00_includes/Cloud(AWS)/CloudWatch_Metrics.png)  
![Load_LB](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/34d837ac4bce8df44f7c07a6ad9d7923e992de63/00_includes/Cloud(AWS)/Load_LB.png)  
![Instances_ASed](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/34d837ac4bce8df44f7c07a6ad9d7923e992de63/00_includes/Cloud(AWS)/Instances_ASed.png)
