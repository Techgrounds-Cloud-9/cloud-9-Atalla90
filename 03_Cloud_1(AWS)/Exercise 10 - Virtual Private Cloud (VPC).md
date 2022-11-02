# [Virtual Private Cloud (VPC)]

[Working with Amazon VPC.]

## Key terminology

[Internet Gateway: A VPC component that provides internet connection to the EC2 instances in public subnets within that VPC.

NAT Gateway: A VPC component that provides internet connection to the EC2 instances in private subnets within that VPC. A NAT Gateway has to have an Elastic IP address assigned to it.

Elastic IP Address: A static public IP address that you can allocate to your account and assign to resources like EC2 instances or network components, such as; NAT Gateways and Load Balancer nodes.]

## Exercise

1.  
A) Allocated Elastic IP address to my account.  
B) Launched a VPC with the provided requirements

2.  
A) Created two additional subnets (Public and private).  
B) Created an Internet Gateway.
C) Created a NAT Gateway using the Elastic IP address.  
D) Changed the name of the main route table to "Private Route Table" and registered the NAT Gateway in it.  
E) Associated the Private Route Table with both private subnets.  
F) Created a Public Route Table and registered the Internet Gateway in it.  
G) Associated both Public subnets with the Public Route Table.

3. Created a Security Group with the provided requirements.  

4.  
A) Created an EC2 instance with the provided requirements.  
B) Made an HTTP connection with the web server on the EC2 instance from my web browser.


### Sources

[1. https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html

2. https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html

3. https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html]

### Overcome challenges

[]

### Results

![Elastic_IP](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/e54a7246f086db4d583767767436c412bc5034be/00_includes/Cloud(AWS)/Elastic_IP.png)  
![Lab_VPC](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/493e3055774f4963f7fb69cde4087252ca597e75/00_includes/Cloud(AWS)/Lab_VPC.png)  
![Subnets](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/1392e9985670a9ab6c0ae8d7fe84722c2130333c/00_includes/Cloud(AWS)/Subnets.png)  
![NAT_Available](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/20d804ec3c895aa003b78947e6ab318529fee0d0/00_includes/Cloud(AWS)/NAT_Available.png)  
![Private_RT](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/f550c36a2196068f760e4f783c8ccc222449e3c7/00_includes/Cloud(AWS)/Private_RT.png)  
![Public_RT](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a11994870dd46d72b63efbc02be6cb9028c8a772/00_includes/Cloud(AWS)/Public_RT.png)  
![Web_SG](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/dfa39ec0f61705cafa899f8f718baa0813f16eb4/00_includes/Cloud(AWS)/Web_SG.png)  
![HTTP_Request](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/e75dffe15ab0edaf486884e450b670f34c113972/00_includes/Cloud(AWS)/HTTP_Request.png)
