# [Files, AppServices, CDN, DNS, Database]

[Learning about Elastic Beanstalk, CloudFront and Route 53, and working with EFS, RDS and Aurora.]

## Key terminology

[Environment: An environment in AWS Elastic Beanstalk is the collection of AWS resources running a web application.

Application Source Bundle: The bundle that combines the scripts of a Web Application.

CloudFront distribution: A configuration the customer makes to specify the origin servers from which Amazon CloudFront should get the requested content.

Point Of Presence(POP): An Edge Location or a Regional Edge Cache where content gets cached by Amazon CloudFront in order to be delivered faster.

Domain Name: The user-friendly name of a website, for example; www.website.com

Registrar: A company that receives domain name registration requests for certain Top-level domains, verifying them and forwards them to the registry.

Registry: A company that owns the right to sell certain top-level domains. It also set the requirements for domain name registration for those top-level domains, such as; residency constraints in the case of geographic TLDs.

Hosted Zone: A container where records are stored in Route 53.

Alias Record: A record in Route 53 that refers to endpoints in AWS resources.

CNAME Record: A record in Route 53 that refers to resouces outside of AWS.

Time To Live(TTL): The amount of time in seconds that a record values live in a DNS resolver before expiring.

Aurora Cluster: A unit consists of one or more Aurora database instances.]

## Studies

### AWS Elastic Beanstalk

1. AWS Elastic Beanstalk is a PaaS service that provides the customer with the ability to deploy web applications without worrying about provisioning the infrastructure themselves. You upload an Application Source Bundle in one of the supported languages (Go, Java, .NET, Node.js, PHP, Python, and Ruby) and Elastic Beanstalk takes care of provisioning the needed AWS resources and creates an environment that runs your application.  
2. A customer can apply hybrid solutions using AWS Elastic Beanstalk to deploy a web application that depends on components they have in their on-premise, such as a database server. To provide a secure connection between their AWS resources and their on-premise resources, a VPN connection, AWS Managed VPN or AWS Direct Connect can be used.  
Before Cloud-based platforms such as Elastic Beanstalk, conventional solutions were followed, where you had to provision and configure all the components required to deploy your application. Later on, independent PaaS providers came into the picture, with the first one being Zimki in London, 2006.
3. In order to provide the required environment for an app, AWS Elastic Beanstalk works with many other AWS services, such as; Amazon EC2 to create the servers, Amazon S3 to create storage units, Amazon CloudWatch to monitor, AWS CloudFormation to create the basic infrastructure.  
4. Beside AWS Elastic Beanstalk, AWS offers other PaaS services, such as AWS Lambda. The difference between AWS Lambda and AWS Elastic Beanstalk is that Lambda creates functions that run in an event-driven serverless way, without provisioning a dedicated server and a complete traditional infrastructure.  
Another PaaS service that has some similarity with Elastic Beanstalk is Amazon LightSail. LightSail provides an even more managed platform to host and run light applications. Therefore, you have even less control over the infrastructure than with Elastic Beanstalk.

### AWS CloudFront

1. Amazon CloudFront is an AWS web service that works as a CDN for the customer's web content, such as; HTML, CSS, JavaScript and image files. CloudFront gets the requested content from the origin servers and caches it in Points Of Presence (POPs) that are closer to the end-user in order to reduce latency. CloudFront allows the user to make a configuration called CloudFront Distribution in which they can specify where the object is originally located and how to track and manage the delivery process. Optionally, An expiration period of the object can also be configured by adding headers to the original file. An object expires and gets removed from the POP by default after 24 hours.  
2. Using a Custom Origin Server configuration, a customer can also use CloudFront to cache content that's originally located anywhere, in an on-premises hosted server or even in servers that are running in other clouds rather than AWS.  
CDNs have been used to cache content to be delivered faster since the late 90's. Amazon CloudFront is a modern, global CDN that offers you the ability to cache your content in a world-wide spreaded AWS POPs.  
3. Amazon CloudFront gets content that can be originally located in units of other AWS services, such as; EC2 instances and S3 buckets.  
4. CloudFront is the only CDN service that AWS offers.

### Amazon Route 53

1. Amazon Route 53 is an AWS service that offers a Domain Name System (DNS).  
Route 53 can be used for 3 purposes:  
A) Amazon Route 53 can be used to register domain names. When a new domain name is registered, Route 53 creates a hosted zone with the same name, Assigns a set of 4 name servers to the hosted zone and adds those name servers to the domain. Route 53 then sends the registeration's information to Amazon Registrar or Amazon registrar associate Gandi. The registrar forwards the information to the registry and the registry saves a copy of it in its database and saves another copy in the WHOIS database.  
B) After registering the domain name, you can route the traffic to your resources by creating Alias Records or CNAME Records In the hosted zone. When a request is made to the domain name, it's first sent from the client to the resolver of the Internet Service Provider. The resolver forwards the request to a DNS root name server, then to the TLD name server for the provided top-level domain and once again to the four assigned Route 53 name servers. The resolver then caches the four Route 53 name servers, typically for 2 days, it also caches the IP address of the resource for the Time To Live you specify.  
C) Amazon Route 53 can be used to send regular requests to the resources for health checking purposes. When you create a health check, you specify; IP address or domain name of the resource, The protocol to be used in the check, how often the request should be sent, the failure threshold and optionally, a notification you receive when a resource becomes unhealthy. You can also configure the health check to check the health of more health checks. That way you get notified when a specific number of resources gets unhealthy.  
2. Route 53 can be used for one of the three purposes solely or in combination with other purposes. Meaning that you can (for example) use Route 53 to route the traffic to resources that are registered with a domain name in another DNS service. Another example is that you can use Route 53 to check the health of resources that are registered with a domain name in another DNS service and don't use Route 53 to route their traffic.  
A lot of other DNS services other than Route 53 are there, though Route 53 stands out with its scalability and its high availability.
3. Route 53 works with a lot of other AWS services. It can route the traffic to endpoints in EC2, S3, VPC and many other services. Also, by using the health check notification of Route 53 you set a CloudWatch Alarm.  
4. Route 53 is the only DNS service in AWS.

## Exercise

### Amazon Elastic File System (Amazon EFS)

1. Created a File System using Amazon EFS.  
2. Mounted the File System in an EC2 instance during the launch of the instance.

### Amazon RDS & AWS Aurora

1. Created a PostgreSQL database instance on RDS and connected it to an EC2 instance.  
2. Created an Aurora database cluster on RDS, which created a reader instance and a writer instance and connected it to an EC2 instance

### Sources

[1. <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html>

2. <https://stackoverflow.com/questions/49201162/can-application-running-on-aws-elastic-beanstalk-make-a-call-to-on-premises-db>

3. <https://en.wikipedia.org/wiki/Platform_as_a_service#Providers>

4. <https://www.justaftermidnight247.com/insights/cloudformation-vs-elastic-beanstalk-aws-paas-and-iac-services/#:~:text=The%20essential%20difference%20between%20these,low%20control%2C%20and%20vice%20versa>.

5. <https://medium.com/@kyawzinlatt/aws-elastic-beanstalk-or-aws-lightsail-when-to-use-which-f448e4a49147>

6. <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html>

7. <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-domain-registration.html>

8. <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html>

9. <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html>

10. <https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html>

11. <https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html>

12. <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html>

13. <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.html>

14. <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html>

15. <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html>]

### Overcome challenges

[]

### Results

![Lab_EFS](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ddf1d2c6f06d60cd2534f8a08bedb921719273a5/00_includes/Cloud(AWS)/Lab_EFS.png)  
![Mounting_EFS](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ddf1d2c6f06d60cd2534f8a08bedb921719273a5/00_includes/Cloud(AWS)/Mounting_EFS.png)  
![Extra_SGs](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ddf1d2c6f06d60cd2534f8a08bedb921719273a5/00_includes/Cloud(AWS)/Extra_SGs.png)  
![RDS(1)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ddf1d2c6f06d60cd2534f8a08bedb921719273a5/00_includes/Cloud(AWS)/RDS(1).png)  
![RDS(2)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ddf1d2c6f06d60cd2534f8a08bedb921719273a5/00_includes/Cloud(AWS)/RDS(2).png)  
![RDS(3)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ddf1d2c6f06d60cd2534f8a08bedb921719273a5/00_includes/Cloud(AWS)/RDS(3).png)  
![Aurora_RDS(1)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/f85e6c9cac7d0733b0408c9399cfcb93dcdb0102/00_includes/Cloud(AWS)/Aurora_RDS(1).png)  
![Aurora_RDS(2)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/f85e6c9cac7d0733b0408c9399cfcb93dcdb0102/00_includes/Cloud(AWS)/Aurora_RDS(2).png)

