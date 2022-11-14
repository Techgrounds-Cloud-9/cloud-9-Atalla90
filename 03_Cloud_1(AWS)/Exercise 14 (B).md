# [IAM, AWS Cloudwatch, DynamoDB, AWS Lambda, SNS, SQS, Event Bridge]

[Working with the AWS services mentioned in the title.]

## Key terminology

[IAM Entity: IAM object that AWS uses for authentication. It includes users and roles.

IAM Identity: General IAM objects which you can assign policies to. It includes users, groups and roles.

Principal: A person or an application that uses an IAM user or an IAM role to make requests to AWS resources.

Attribute-based access control (ABAC): An authorization strategy that bases the permissions an entity has on attributes (Tags) assigned to that entity.

CloudWatch Metric: A time-ordered set of data points that are published to CloudWatch.

CloudWatch Namespace: An isolated container for metrics that are related to each other. You must specify a namespace when you publish metrics to CloudWatch.

Metric Dimension: A name/value pair that defines a part of the metric's characteristics. A metric can have up to 30 dimensions.

Alarm: A signal that CloudWatch issues for an action to be taken on the customer's behalf based on exceeding a certain threshold according to a metric.

NoSQL: Nonrelational database system that's highly available and highly scalable. It's an alternative for relational databases (SQL).

Lambda Function: An AWS resource that runs the customer's code when invoked by a trigger event.

Lambda Runtime: An environment of a programming language that's in the execution environment of a Lambda function.

LAmbda Layer: A .zip file that can contain custom runtime, libraries or data to run the code in a function.

Lambda Extension: A way to augment a Lambda function in order for it to be integrated with monitoring, security or governance tools.

SNS Topic: A communication channel in Amazon SNS where a publisher publishes message to subscriber(s).

Fanout: When a message in an SNS Topic gets published to many subscribers.

FIFO: First In First Out, is a technique for ordering the exit of messages from a topic, a queue or a bus in the same order they entered.

SQS Queue: A communication channel in Amazon SQS where producers produce messages to be consumed by consumers.

Dead-letter Queue: An SQS Queue where messages that have failed to be consumed get sent.

Event Bus: The communication channel in Amazon EventBridge. It has the same functionality as An SQS Queue.]

## Exercise

### AWS Identity and Access Management (IAM)

1. Created a new IAM user as administrator.  
2. Created a new group for administrators and put the new user in it.  
3. Assigned administration policies to the group.

### AWS CloudWatch

1. Viewed the metrics of the Lambda Function.  
2. Viewed the metrics of "Students" DynamoDB table.  

### AWS DynamoDB

1. Created a "Students" table and added one item to it with 3 attributes; a string, a number and a boolean value.
2. Added a new item to the table with the same attributes.  

### AWS Lambda

1. Created a function from a blueprint that processes data from "Students" table in DynamoDB and publishes to an SNS topic.
2. Assigned an IAM role with the needed permissions.  
3. Ran a successful test on the function

### Amazon SNS

1. Created a Topic where the Lambda function publishes messages to my email address.
2. Published an email to my email address

### Sources

[1. <https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html>

2. <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html>

3. <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html>

4. <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html>

5. <https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html>

6. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html>

7. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html>

8. <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html>

9. <https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html>

10. <https://docs.aws.amazon.com/sns/latest/dg/welcome.html>

11. <https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html>

12. <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-architecture.html>

13. <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-difference-from-amazon-mq-sns.html>

14. <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/step-create-queue.html>

15. <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html>

16. <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-event-bus.html>]

### Overcome challenges

[]

### Results

![IAM_Console](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/be61f3e13fe87aed0331c99c606badb002da117b/00_includes/Cloud(AWS)/IAM_Console.png)  
![New_User](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/be61f3e13fe87aed0331c99c606badb002da117b/00_includes/Cloud(AWS)/New_User.png)  
![Created_User](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/be61f3e13fe87aed0331c99c606badb002da117b/00_includes/Cloud(AWS)/Created_User.png)  
![Admin_Group](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/be61f3e13fe87aed0331c99c606badb002da117b/00_includes/Cloud(AWS)/Admin_Group.png)  
![IAMuser_Access](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/be61f3e13fe87aed0331c99c606badb002da117b/00_includes/Cloud(AWS)/IAMuser_Access.png)  
![IAM_Billing](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/be61f3e13fe87aed0331c99c606badb002da117b/00_includes/Cloud(AWS)/IAM_Billing.png)  
![CloudWatch_Dashboard](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/9629d6e61491e5001b0687fa62a085a5cda3aca7/00_includes/Cloud(AWS)/CloudWatch_Dashboard.png)  
![Students_Table](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/d7d7036687b2af26d92391db8d54cf61c9ca8b80/00_includes/Cloud(AWS)/Students_Table.png)  
![Lambda_Scheme](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a2d936c63bc4a35ae7cedde766ea42fb14f69221/00_includes/Cloud(AWS)/Lambda_Scheme.png)  
![New_Item](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a2d936c63bc4a35ae7cedde766ea42fb14f69221/00_includes/Cloud(AWS)/New_Item.png)  
![Func_Test](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a2d936c63bc4a35ae7cedde766ea42fb14f69221/00_includes/Cloud(AWS)/Func_Test.png)  
![SNS_Email](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a2d936c63bc4a35ae7cedde766ea42fb14f69221/00_includes/Cloud(AWS)/SNS_Email.png)  
![SNS_Topic](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a2d936c63bc4a35ae7cedde766ea42fb14f69221/00_includes/Cloud(AWS)/SNS_Topic.png)  
![Table_Metrics](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/a2d936c63bc4a35ae7cedde766ea42fb14f69221/00_includes/Cloud(AWS)/Table_Metrics.png)  
