# [ECS, AWS Support Plans, Trusted Advisor, AWS Config, AWS Cloud Trail]

[Gaining more knowledge about the AWS services mentioned in the title.]

## Key terminology

[Amazon Elastic Container Service(ECS): An AWS service for managing containers.

AWS Fargate: An AWS service that provides serverless management for containers in AWS ECS.

ECS Cluster: A group of ECS tasks and services.

ECS Task: One or more (up to ten) containers that run within a cluster.

Task Definition: A text file in JSON format where the container(s) that are used to run (part of) an application are described.

ECS Service: A group of tasks which run simultaneously within a cluster.

Container: A standard unit of software development that contains all what a specific application needs to run, including; relevant code, runtime, system tools and system libraries.

Container Image: A read-only template that is used to create a container. Images are usually built from Dockerfiles and then pushed to a registry like Docker Hub or Amazon Elastic Container Registry to be stored.

Dockerfile: A plaintext file where all the components included in a container are specified.

Container agent: A process that connects AWS ECS with containers in a cluster. It sends information about the running tasks and receives requests to run or stop tasks.

CI/CD: Continuous Integration/Continuous Deployment, is the process of automating application development by employing a CI/CD Pipeline. It makes it possible to integrate new versions of the code and re-deploy the application continuously.

Microservice: A way of developing an application as a group of small independent services that communicate with each other and that are owned by a small team.

Configuration Item: A point-in-time view of the configuration of a certain AWS resource that's supported by AWS Config. It includes; metadata, attributes, relationships, current configuration, and related events.

Configuration Snapshot: A collection of the configuration items for the resources supported by AWS Config. It gives a whole picture of the resources and their configuration.

Configuration Stream: An updated list of configuration Items.

AWS Config Rules: Rules that define the customer's desired configurations of an AWS resource in their account or of the entire account. Config Rules can be managed or customized.

AWS Config Aggregator: A process that collects configurations and compliance data from multiple source accounts and/or multiple regions.

AWS CloudTrail Event: An activity in an AWS account that's logged by CloudTrail.

AWS CloudTrail Trail: The process of CloudTrail sending event logs to Amazon S3 Buckets, CloudWatch Events and CloudWatch Logs.]

## Exercise

### Amazon Elastic Container Service(ECS)  

1. Amazon ECS enables developers to manage the containers that run their application. Amazon ECS is a fully managed service that comes with AWS configuration and operational best practices built-in. ECS is integrated with other AWS and third-parties tools, such as AWS Elastic Container Registry and Docker.  
2. Using Amazon ECS Anywhere, a customer can run and manage their container workloads on their own on-premise infrastructure by obtaining an activation key through AWS Management Console or AWS CLI to register their servers, and then installing AWS Systems Manager Agent and Amazon ECS Agent.  
3. Amazon ECS works together with other AWS services, such as; AWS IAM to manage access to the containers, Amazon EC2 to manage the infrastructure where containers run on, and where you can use Load Balancing and Auto Scaling for your containers, AWS Fargate to run serverless containers, AWS CloudWatch where you can choose to send the logs for your containers to view it conveniently and AWS CloudFormation to define clusters, tasks and services.  
4. Another AWS service that is used to manage containers is Amazon Elastic Kubernetes Service (EKS), which is used to manage containers specifically with Kubernetes.

### AWS Support Plans

1. Using AWS Support, a Support Case can be created about one of three topics; Billing and Account, Service Limit increase, or Technical Support according to the customer's Support Plan. In the Support Case, Service, Category and Severity can be specified. The level of severity a case can be created at depends also on the Support Plan.  
Available AWS Support Plans are:  
A) Basic: The standard Support Plan any AWS customer gets by default. It includes support for Account and Billing and for Service Limit increase. It offers 24/7 access to; One-on-one responses to account and billing questions, Support forums, Service health checks, and Documentation, technical papers, and best practice guides. With the Basic Support, severity of the case can not be selected.  
B) Developer: The first grade of paid AWS Support Plan. It offers, in addition to the basic features, Best practice guidance, Client-side diagnostic tools, Building-block architecture support, An unlimited number of support cases that can be opened by the Root User. With the Developer Support Plan you get to choose between 2 grades of case severity; General guidance (Low), which has 24 hours as First-response time, and System impaired (Normal), which has 12 hours as First-response time.  
C) Business: This Support Plan offers, in addition to Basic and Developer features, Use-case guidance – What AWS products, features, and services to use, AWS Trusted Advisor, AWS Support API, Third-party software support, an unlimited number of AWS IAM users. In addition to the 2 severity grades supported in Developer Support Plan, you also get to choose between 2 more severity grades, which are; Production system impaired (High), which has 4 hours as First-response time, and Production system down (Urgent), which has 1 hour as First-response time.  
D) Enterprise On-Ramp: his Support Plan offers, in addition to Basic, Developer and Business features, Application architecture guidance, Infrastructure event management, Technical account manager, White-glove case routing, and Management business reviews. In addition to the 4 severity grades supported in Developer and Business Support Plans, you also get to choose 1 more severity grade, which is; Business-critical system down (Critical), which has in this plan 30 minutes as First-response time. This plan also offers access to the Concierge Support Team.  
E) Enterprise: This plan offers the same features supported in Enterprise On-Ramp plan plus; access to AWS Incident Detection and Response, Access to online self-paced labs, and a First-time response of 15 minutes for Critical support cases.

### AWS Trusted Advisor

1. If a customer has Business, Enterprise On-Ramp or Enterprise Support Plan, they can enable AWS Trusted Advisor. With Enterprise Support Plan and an AWS Organizations account a customer can also have access to Trusted Advisor Priority, which enables members of the AWS Organization account to prioritize recommendations for the root user.  
AWS Trusted Advisor performs checks based on 5 criterias:  
A) Cost Optimization: Identifies cost-saving opportunities and gives recommendations to seize them. It checks, for example, for unused resources.  
B) Performance: Gives recommendations to improve the performance of an application.  
C) Security: Identifies security shortfalls and gives recommendations to fix them.  
D) Fault Tolerance: Gives recommendations to increase the resiliency on an application. It checks, for example, for redundancy shortfalls and current service limits.  
E) Service Limits: Checks the usage of AWS service and resources for an account to see when it approaches or exceeds those limits.  
Checks of Trusted Advisor are divided into 3 categories:  
A) Action Recommended (Red): Check results that require an urgent action to be taken by the customer.  
B) Investigation Recommended (Yellow): Check results that require some attention from the customer, as they might represent potential risks.  
C) Excluded Items (Gray): Items that have been excluded from the check by the customer.  
AWS Trusted Advisor operations can be called in the application's code by creating an instance of AWS Support Client.

### AWS Config

1. AWS Config is a service that enabels the customer to track configuration changes of their (supported) AWS resources and to set rules for their desired configuration of a resource or of an entire account.  
2. AWS Config offers a convenient environment to track configuration changes for your AWS resources as well as other non-AWS or non-cloud resources that you may have.  
3. AWS Config uses Amazon S3 Buckets to store configuration history, and it can also open an Amazon SNS topic to notify about changes in configuration or in compliance status based on a Config rule.  
AWS Config also track configuration changes of resources from various AWS services.  
4. Other AWS services that might be having similarities with AWS Config are; Trusted advisor, which runs checks on AWS resources and recommends actions to be taken to improve security, performance and optimize costs, and AWS CloudTrail, which offers an overview of the actions taken by users, roles and services in an account over time.

### AWS CloudTrail

1. AWS CloudTrail is a service that records activities in an AWS account as Events. CloudTrail is activated once an account is created. Optionally, a Trail can be created to archive, analyze and respond to changes in AWS resources. A Trail can track changes in all regions or in a specific region. A Trail is by default all-regions when it's created. A single-region Trail can only be created using AWS CLI.  
CloudTrail Events can be divided in 3 main categories:  
A) Management Events: Provide information about management operations, known as "Control Plane Operations", performed on AWS resources. management operations can be like; configuring security, registering devices, configuring routing rules and setting up logging.  
B) Data Events: Provide information about operations done on or in AWS resources, known as "Data Plane Operations". These are not logged by default when a Trail is created, and they cause extra charges. This includes; Amazon S3 object-level API activity, AWS Lambda function execution activity, Amazon DynamoDB object-level API activity on tables, Amazon S3 Object Lambda access points API activity, Amazon Elastic Block Store (EBS) direct APIs, Amazon S3 API activity on access points, Amazon DynamoDB API activity on streams, AWS Glue API activity on tables.  
C) Insights Events: Provide information about unusual API call rate or error rate activities in an AWS account so that a proper reaction on the unusual activity can be taken in time. Insights Events are logged to a different folder in the same destination Bucket where the Trail is saved. These are not logged by default when a Trail is created, and they cause extra charges.  
2. NA  
3. AWS CloudTrail uses Amazon S3 to store Trails. It also uses AWS CloudWatch to log events to CloudWatch Events and CloudWatch logs. Cloud Trail also provides information on activities on or in different AWS resources.  
4. CloudTrail has similarities with other AWS services, such as; AWS CloudWatch, which logs application specific reports and AWS Config, which logs reports about configuration changes of AWS resources.

### Sources

[1. <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html>

2. <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/welcome-features.html>

3. <https://www.redhat.com/en/topics/devops/what-is-ci-cd>

4. <https://aws.amazon.com/microservices/>

5. <https://aws.amazon.com/ecs/anywhere/>

6. <https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html>

7. <https://aws.amazon.com/premiumsupport/plans/>

8. <https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html>

9. <https://docs.aws.amazon.com/awssupport/latest/user/trustedadvisor.html>

10. <https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html>

11. <https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html>

12. <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html>

13. <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html>]

### Overcome challenges

[]

### Results

[]
