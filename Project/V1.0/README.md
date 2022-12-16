
## Welcome to Atalla-Techgrounds project V1.0

This app deploys an AWS infrastructure consisting of:  
A) 2 VPC's in region eu-central-1(Frankfurt), as the AZ's where the subnets would reside are AZ's of that region. To change the region you'll have to change the AZ's in the code accordingly. CIDR-blocks used for the VPC's are 10.10.10.0/24 and 10.20.20.0/24.  
B) Each VPC spans two AZ's (eu-central-1a, eu-central-1b) with one public subnet in each AZ. The subnets have the CIDR Mask /25.  
C) An EC2 instance that runs an Apache Web Server on Amazon Linux and resides in one of the VPC's in AZ eu-central-1a.  
D) An EC2 instance that works as a management server and runs Windows Server 2022 and resides in the other VPC in AZ eu-central-1b. The server is used as a jump-host for the web server.  
E) A key-pair for each server that gets generated and stored in Systems Manager's Parameter Store.  
F) Each subnet where one of the servers resides is protected with a NACL that allows only the inbound and outbound traffic needed for the respective server to perform its function.  
G) A VPC peering connects both VPC's with each other, with the CIDR-blocks of only the two subnets where the servers reside registered in each other's route tables.  
H) Each server is protected with a security group that allows only the needed inbound traffic and all the outbound traffic.  
I) A Bash script contains the post-deployment script needed to download, install and configure Apache web server on the web server EC2 instance. The script is uploaded as an asset to the CDK assets S3 Buckets. The web server then reads the Bash script and executes it when the app is deployed. The assets Bucket is encrypted (AWS managed) and is not publicly accessible.  
J) An AWS Backup Plan and Vault for daily backing up the webserver at 00:00. Each backup gets retained for 7 days.  
K) KMS encryption keys that encrypt the EBS Volumes for both servers and the Backup Vault.  
L) Only the IP addresses of home and office are allowed to make an RDP connection with the management server, and only the management server is allowed to make an SSH connection with the webserver.  
M) Most of the IAM roles and policies that are required for the resources to function get generated automatically with exactly enough permissions for their functions.

## To use the app

```
python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk docs`        open CDK documentation

Enjoy!
