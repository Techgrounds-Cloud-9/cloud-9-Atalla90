# [Security Groups]

[Studying Security Groups.]

## Key terminology

[Security Group: A virtual stateful firewall that controls the inbound and outbound traffic of an EC2 instance. AWS always automatically assigns a default security group to the instance if another(new) security group was not specified. When creating an EC2 instance within a VPC you have to assign a security group to it that's created for that network, afterwards you can change it. With the security group you can define rules to allow traffic from or to your AWS resource. Traffic that's not explicitly allowed is, by default, denied.

AWS PrivateLink: A private connection the user can make between an EC2 instance and a VPC to improve security even further. With PrivateLink you can access the outside EC2 instance as if it were part of your VPC without any need of another kind of connection to the internet.

Network Access Control List (NACL): A sort of a stateless firewall that works on the subnet level in the VPC. The default NACL of the VPC, that allows all traffic, gets assigned to the subnet if the user doesn't assign a custom NACL. It's a common practice to customize an NACL as an extra layer of VPC security by applying the same rules as the VPC's security groups.]

## Exercise

### Sources

[1. <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>

2. <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html>

3. <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html>]

### Overcome challenges

[]

### Results

[]
