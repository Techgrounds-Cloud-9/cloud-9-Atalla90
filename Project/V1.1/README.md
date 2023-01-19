
## Welcome to Atalla-Techgrounds project V1.1

-This is an IaC project using AWS CDK in Python.  
-This app deploys an AWS infrastructure consisting of:  
A) 2 VPC's in region eu-central-1(Frankfurt), as the AZ's where the subnets would reside are AZ's of that region. To change the region you'll have to change the AZ's in the code accordingly. CIDR-blocks used for the VPC's are 10.10.10.0/24 and 10.20.20.0/24.  
B) The VPC where the admin server resides spans two AZ's (eu-central-1a, eu-central-1b) with one public subnet in each AZ. The subnets have the CIDR Mask /25.  
C) The VPC where the web server instances resides spans three AZ's (eu-central-1a, eu-central-1b, eu-central-1c) with one public subnet and one private subnet in each AZ. The public subnents have the CIDR Mask /28, and the private subnets have the CIDR Mask /26. The private subnets are connected to the internet through a NAT Gateway.  
D) An EC2 autoscaling group that launches an Apache Web Server on Amazon Linux instances to the private subnets.  
E) An EC2 instance that works as a management server and runs Windows Server 2022 and resides in the other VPC in AZ eu-central-1b. The server is initially used as a jump-host for the web server.  
F) A key-pair that's used for SSH and RDP connections and that gets generated and stored in Systems Manager's Parameter Store.  
G) Each subnet where one of the servers resides is protected with a NACL that allows only the inbound and outbound traffic needed for the respective server to perform its function.  
H) A VPC peering connects both VPC's with each other, with the CIDR-blocks of only the two subnets where the servers reside registered in each other's route tables.  
I) Each server is protected with a security group that allows only the needed inbound traffic and all the outbound traffic.  
J) An S3 bucket where a Bash script contains the post-deployment script needed to download, install and configure Apache web server on the web server EC2 instances. The buckets in versioned to provide a cost-efficient backup solution for the user data.
K) KMS encryption keys that encrypt the EBS Volumes for the admin server's EBS volume and the bucket. While the EBS volumes of the web server instances are encrypted with keys that are AWS managed.  
L) An application load balancer that works as proxy in front of the web server instances and that has nodes in the public subnets of the web VPC.  
M) A self-signed TLS certificate that is used by the load balancer to provide HTTPS connection.  
N) Only the IP addresses of home and office are allowed to make an RDP connection with the management server, and only the management server is allowed to make an SSH connection with the webserver.  
O) Most of the IAM roles and policies that are required for the resources to function get generated automatically with exactly enough permissions for their functions.

## To use the app

### Prerequisites

- Before attempting to deploy the app, make sure you have the following requirements satisfied:  
- Install AWS CLI on your system, by downloading the installer for your OS from: [AWS CLI installation page.](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html)  
- Assuming you already have an AWS account where you want to create the environment for the app, you should obtain an Access Key ID and a Secret Access Key for your AWS user. Note that it's not recommended to obtain such credentials for the root user. Therefore, make sure you have an IAM user with Adminstrator's permissions.  
When you're all set you can run the following command to log into your AWS environment:  

```
aws configure
```  

- Install Node.js (>= 10.13.0, except for versions 13.0.0 - 13.6.0). You can downlaod the installer from: [The official Node.Js download page.](https://nodejs.org/en/)  
- Install AWS CDK Toolkit by running:  

```
npm install -g aws-cdk
```

- Install Python and make sure you have it in your PATH environment variable. You can download the installer from: [The official Python download page](https://www.python.org/downloads/)  

### Using the app

1- First you should create your Python Virtual Environment for the app by running the command:

```
python -m venv .venv
```

2- Then you activate your virtualenv. by running one of the following commands depending on the OS you're using.  
For UNIX-based systems:

```
source .venv/bin/activate
```

For Microsoft Windows:

```
% .venv\Scripts\activate.bat
```

Or:

```
% .venv\Scripts\activate.ps1
```

3- When the virtualenv. is activated you can install the requirements by running:

```
pip install -r requirements.txt
```

4- Now is a good time for synthesising the CloudFormation template for the app by running:

```
cdk synth
```  
5- Then bootstrapping the environment, which uploads the assets CloudFormation will use to deploy our infrastructure, by running:  
```
cdk bootstrap
```  
6- To make sure everything is in the right order, code wise, you can run:  
```
cdk ls
```  
which will list the available stacks to be deployed in this app. You should be able to see the following in your terminal:  
```
ProjectAtallaCertStack
ProjectAtallaKmsStack
ProjectAtallaS3Stack
ProjectAtallaVpcStack
```  
7- Then you can deploy each stack separately by running:  
```
cdk deploy <Stack Name>
```
Or deploy the whole app by running:  
```
cdk deploy --all
```


To add additional dependencies, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

### Useful commands

- `cdk diff`        compare deployed stack with current state
- `cdk docs`        open CDK documentation

Enjoy!