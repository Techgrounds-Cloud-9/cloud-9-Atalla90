import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
    Duration,
    RemovalPolicy,
    CfnOutput,
    App,
    Tags,
    aws_iam as iam,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_backup as backup,
    aws_events as event,
    aws_kms as kms,
    aws_ssm as ssm,
    aws_elasticloadbalancingv2 as elbv2,
    aws_autoscaling as autoscaling,
)

import os.path

from constructs import Construct
from urllib import response
from aws_cdk.aws_s3_assets import Asset
from constructs import Construct

dirname= os.path.dirname(__file__)

class CustomVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_ip = "83.81.114.11/32"

        # The code that defines your stack goes here
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/Vpc.html
        WebVPC = ec2.Vpc(
                self, "Webserver VPC",
                cidr="10.10.10.0/24",
                availability_zones=["eu-central-1a", "eu-central-1b"],
                nat_gateways=0,
                subnet_configuration=[
                    ec2.SubnetConfiguration(name="public", cidr_mask=25, subnet_type=ec2.SubnetType.PUBLIC)
                    # ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE)
                ]
            )

        AdminVPC = ec2.Vpc(
                self, "Admin VPC",
                cidr="10.20.20.0/24",
                availability_zones=["eu-central-1a", "eu-central-1b"],
                nat_gateways=0,
                subnet_configuration=[
                    ec2.SubnetConfiguration(name="public", cidr_mask=25, subnet_type=ec2.SubnetType.PUBLIC)
                    # ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE)
                ]
            )
        
        # Tag all VPC Resources
        # core.Tag.add(vpc,key="Owner",value="Dominic",include_resource_types=[])

        self.cfn_VPCPeering_connection =ec2.CfnVPCPeeringConnection(self, "VPC peering connection",
            peer_vpc_id = AdminVPC.vpc_id,
            vpc_id = WebVPC.vpc_id,

            # the properties below are optional
            peer_region='eu-central-1',
            )

        # Update Route Tables for Peering Connection
        route_table_web_entry = ec2.CfnRoute(
            self, 'VPC-Web Peer Route100',
            route_table_id=WebVPC.public_subnets[0].route_table.route_table_id,
            destination_cidr_block='10.20.20.0/24',
            vpc_peering_connection_id=self.cfn_VPCPeering_connection.attr_id,
        )

        route_table_admin_entry = ec2.CfnRoute(
            self, 'VPC-admin Peer Route100',
            route_table_id=WebVPC.public_subnets[1].route_table.route_table_id,
            destination_cidr_block='10.10.10.0/24',
            vpc_peering_connection_id=self.cfn_VPCPeering_connection.attr_id,
        )


        #create and configure the Application Load Balancer
        APPlb = elbv2.ApplicationLoadBalancer(
            self, "Application Load Balancer",
            vpc=WebVPC,
            internet_facing=True,
        )

        # redirect HTTP traffic to HTTPS, from port 80 to port 443
        APPlb.add_redirect()

        # adding the listeners for HTTP and HTTPS port 80 and 443
        listener80 = APPlb.add_listener("listener80", port = 80)
        # listener443 = APPlb.addlistener("listener443", port = 443)

        target80 = listener80.add_targets("target 80", port = 80, targets= [])
        # target443 = listener443.addtargets("target 443", port = 443, targets = [asg])

# this is the Webserver ACL which needs to be Public, accessible from the Admin server only through SSH and RDP
        web_network_acl = ec2.NetworkAcl(
            self, "Webserver-ACL",
            vpc= WebVPC,

            # the properties below are optional
            network_acl_name="Webserver ACL",
            subnet_selection=ec2.SubnetSelection(
                # availability_zones=["eu-west-2a", "eu-west-2b"],
                # one_per_az=False,
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )
        # these are the entries that specify the rules on what is allowed like, inbound and outbound traffic
        # Outgoing Webserver ACL rules
#         network_acl_entry = ec2.NetworkAclEntry(self, "Allow Ephemeral Egress",
#             # the CIDR range to allow or deny the subnet access
#             cidr= ec2.AclCidr.any_ipv4(),
#             network_acl= web_network_acl,
#             # rule number represents the protocol rule number
#             rule_number=100,
#             # What kind of traffic
#             traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),

#             # the properties below are optional
#             # Inbound or outbound traffic direction
#             direction=ec2.TrafficDirection.EGRESS,
#             # key-value with acl rule name
#             network_acl_entry_name="Allow Ephemeral Egress",
#             # whether the rule allows or denies the access that is specified above
#             rule_action=ec2.Action.ALLOW
#         )

#         network_acl_entry = ec2.NetworkAclEntry(self, "Allow HTTP Egress",
#             cidr= ec2.AclCidr.any_ipv4(),
#             network_acl= web_network_acl,
#             rule_number= 190,
#             traffic= ec2.AclTraffic.tcp_port(80),
#             direction= ec2.TrafficDirection.EGRESS,
#             network_acl_entry_name= "Allow HTTP Egress",
#             rule_action= ec2.Action.ALLOW
#             ) 

#         network_acl_entry = ec2.NetworkAclEntry(self, "Allow HTTPS Egress",
#             cidr= ec2.AclCidr.any_ipv4(),
#             network_acl= web_network_acl,
#             rule_number= 110,
#             traffic= ec2.AclTraffic.tcp_port(443),
#             direction= ec2.TrafficDirection.EGRESS,
#             network_acl_entry_name= "Allow HTTPS",
#             rule_action= ec2.Action.ALLOW
#             )

#         network_acl_entry = ec2.NetworkAclEntry(self, "Allow Admin SSH Egress",
#             cidr= ec2.AclCidr.any_ipv4(),
#             network_acl= web_network_acl,
#             rule_number= 120,
#             traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),
#             direction= ec2.TrafficDirection.EGRESS,
#             network_acl_entry_name= "Allow Admin SSH",
#             rule_action= ec2.Action.ALLOW
#             )

        network_acl_entry= ec2.NetworkAclEntry(self, "Allow_All_Egress",
            cidr=ec2.AclCidr.any_ipv4(),
            network_acl= web_network_acl,
            rule_number=250,
            traffic= ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS, 
            rule_action=ec2.Action.ALLOW,
        )

            # The Webserver Incoming ACL rules

        network_acl_entry = ec2.NetworkAclEntry(self, "Allow Ephemeral Ingress",
            cidr= ec2.AclCidr.any_ipv4(),
            network_acl= web_network_acl,
            rule_number=100,
            traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),

            # the properties below are optional
            direction=ec2.TrafficDirection.INGRESS,
            network_acl_entry_name="Allow Ephemeral Ingress",
            rule_action=ec2.Action.ALLOW
            
        )

        network_acl_entry = ec2.NetworkAclEntry(self, "Allow HTTP Ingress",
            cidr= ec2.AclCidr.any_ipv4(),
            network_acl= web_network_acl,
            rule_number=190,
            traffic= ec2.AclTraffic.tcp_port(80),
            direction= ec2.TrafficDirection.INGRESS,
            network_acl_entry_name= "Allow HTTP Ingress",
            rule_action= ec2.Action.ALLOW
        )

        network_acl_entry = ec2.NetworkAclEntry(self, "Allow Admin SSH Ingress",
            cidr= ec2.AclCidr.ipv4("10.20.20.128/25"),
            network_acl= web_network_acl,
            rule_number=120,
            traffic= ec2.AclTraffic.tcp_port(22),
            direction= ec2.TrafficDirection.INGRESS,
            network_acl_entry_name= "Allow Admin SSH",
            rule_action= ec2.Action.ALLOW
        )

        network_acl_entry = ec2.NetworkAclEntry(self, "Allow HTTPS Ingress",
            cidr= ec2.AclCidr.any_ipv4(),
            network_acl= web_network_acl,
            rule_number=110,
            traffic= ec2.AclTraffic.tcp_port(443),
            direction= ec2.TrafficDirection.INGRESS,
            network_acl_entry_name= "Allow HTTPS",
            rule_action= ec2.Action.ALLOW
        )

        network_acl_entry= ec2.NetworkAclEntry(self, "Allow_All_Ingress_Ephemeral",
            cidr=ec2.AclCidr.ipv4("10.10.10.0/25"),
            network_acl= web_network_acl,
            rule_number=220,
            traffic= ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.INGRESS, 
            rule_action=ec2.Action.ALLOW,
        )
# this is the part of the Admin server ACL which needs to be only accessible with a trusted IP address. 
# from the Admin server access can be established to the Webserver only through SSH and RDP
        AdminACL = ec2.NetworkAcl(
            self, "Admin-server-ACL",
            vpc= AdminVPC,

            # the properties below are optional
            network_acl_name="Admin server ACL",
            subnet_selection=ec2.SubnetSelection(
                # availability_zones=["eu-west-2a", "eu-west-2b"],
                # one_per_az=False,
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        # Admin Incoming traffic rules

        Acl_Admin_Entry = ec2.NetworkAclEntry(self, "Allow SSH Web Incoming",
            # Got to insert your own IP address and change any_ipv4 to just ipv4 for all trusted location connections from the Admin server
            cidr= ec2.AclCidr.ipv4("10.10.10.0/24"),
            network_acl= AdminACL,
            rule_number= 120,
            traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction= ec2.TrafficDirection.INGRESS,
            network_acl_entry_name= "Allow SSH Web Incoming",
            rule_action= ec2.Action.ALLOW
            )

        Acl_Admin_Entry = ec2.NetworkAclEntry(self, "Allow HTTP Incoming",
            cidr= ec2.AclCidr.any_ipv4(),
            network_acl= AdminACL,
            rule_number= 180,
            traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction= ec2.TrafficDirection.INGRESS,
            network_acl_entry_name= "Allow HTTP Incoming",
            rule_action= ec2.Action.ALLOW
            )

        # Trusted IP address needs to be input in the cidr variable
        Acl_Admin_Entry = ec2.NetworkAclEntry(self, "Allow Trusted IP incoming",
            cidr= ec2.AclCidr.ipv4(my_ip),
            network_acl= AdminACL,
            rule_number= 100,
            traffic= ec2.AclTraffic.tcp_port(22),
            direction= ec2.TrafficDirection.INGRESS,
            network_acl_entry_name= "Allow Trusted IP SSH incoming",
            rule_action= ec2.Action.ALLOW
            )

        Acl_Admin_Entry = ec2.NetworkAclEntry(self, "Allow Admin RDP office Incoming",
            cidr= ec2.AclCidr.ipv4(my_ip),
            network_acl= AdminACL,
            rule_number= 130,
            traffic= ec2.AclTraffic.tcp_port(3389),
            direction= ec2.TrafficDirection.INGRESS,
            network_acl_entry_name= "Allow Admin RDP Incoming",
            rule_action= ec2.Action.ALLOW
            )

        Acl_Admin_Entry = ec2.NetworkAclEntry(self, "Allow Web server RDP Incoming",
            cidr= ec2.AclCidr.ipv4("10.10.10.0/24"),
            network_acl= AdminACL,
            rule_number= 170,
            traffic= ec2.AclTraffic.tcp_port(3389),
            direction= ec2.TrafficDirection.INGRESS,
            network_acl_entry_name= "Allow Web server RDP Incoming",
            rule_action= ec2.Action.ALLOW
            )

        # Admin Outgoing traffic rules

        # Acl_Admin_Entry = ec2.NetworkAclEntry(self, "Allow Trusted IP SSH Outgoing",
        #     cidr= ec2.AclCidr.ipv4(my_ip),
        #     network_acl= AdminACL,
        #     rule_number= 100,
        #     traffic= ec2.AclTraffic.tcp_port_range(1024, 65535),
        #     direction= ec2.TrafficDirection.EGRESS,
        #     network_acl_entry_name= "Allow Trusted IP SSH Outgoing",
        #     rule_action= ec2.Action.ALLOW
        #     )

        # Acl_Admin_Entry = ec2.NetworkAclEntry(self, "Allow SSH Web Outgoing",
        #     cidr= ec2.AclCidr.ipv4("10.10.10.0/24"),
        #     network_acl= AdminACL,
        #     rule_number= 120,
        #     traffic= ec2.AclTraffic.tcp_port(22),
        #     direction= ec2.TrafficDirection.EGRESS,
        #     network_acl_entry_name= "Allow SSH Web Outgoing",
        #     rule_action= ec2.Action.ALLOW
        #     )

        # Acl_Admin_Entry = ec2.NetworkAclEntry(self, "Allow HTTP Outgoing",
        #     cidr= ec2.AclCidr.any_ipv4(),
        #     network_acl= AdminACL,
        #     rule_number= 180,
        #     traffic= ec2.AclTraffic.tcp_port(80),
        #     direction= ec2.TrafficDirection.EGRESS,
        #     network_acl_entry_name= "Allow HTTP Outgoing",
        #     rule_action= ec2.Action.ALLOW
        #     )


        # Acl_Admin_Entry = ec2.NetworkAclEntry(self, "Allow Admin RDP Outgoing",
        #     cidr= ec2.AclCidr.any_ipv4(),
        #     network_acl= AdminACL,
        #     rule_number= 130,
        #     traffic= ec2.AclTraffic.tcp_port(3389),
        #     direction= ec2.TrafficDirection.EGRESS,
        #     network_acl_entry_name= "Allow Admin RDP Outgoing",
        #     rule_action= ec2.Action.ALLOW
        #     )

        Acl_Admin_Entry = ec2.NetworkAclEntry(self, 'Allow all Egress',
        cidr = ec2.AclCidr.any_ipv4(),
        network_acl= AdminACL,
        rule_number= 200,
        traffic= ec2.AclTraffic.all_traffic(),
        direction=ec2.TrafficDirection.EGRESS, 
        rule_action=ec2.Action.ALLOW,)

        # Security groups for the VPC on the Instance Level

        WebSG = ec2.SecurityGroup(self, 'alb', 
            vpc= WebVPC,
            allow_all_outbound = True,
            description = 'webserver security group'
            )

        WebSG.add_ingress_rule(
                peer=ec2.Peer.ipv4("10.20.20.0/24"),
                connection=ec2.Port.tcp(22),
                description='Allow SSH access from the world'
            )
        
        WebSG.add_ingress_rule(
                peer=ec2.Peer.any_ipv4(),
                connection=ec2.Port.tcp(80),
                description='HTTP'
            )
            
        WebSG.add_ingress_rule(
                peer=ec2.Peer.any_ipv4(),
                connection=ec2.Port.tcp(443),
                description='HTTPS'
            )

        WebSG.add_ingress_rule(
                peer=ec2.Peer.ipv4("10.20.20.128/25"),
                connection=ec2.Port.tcp(3389),
                description='Allow RDP access from the world'
            )

        AdminSG = ec2.SecurityGroup(self, 'Admin SG',
            vpc= AdminVPC,
            allow_all_outbound = True,
            description = 'AdminSecurityGroup'
            )

        AdminSG.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            connection=ec2.Port.tcp(22),
            description='SSH'
        )    

        AdminSG.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            connection=ec2.Port.tcp(3389),
            description='RDP'
        )

        WebSG.add_ingress_rule(
            ec2.Peer.security_group_id(AdminSG.security_group_id),
            ec2.Port.tcp(22),
            'Allow SSH access from the Admin SG'
        )
        
        #AMI for the instance
        amazon_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
            )

        windows_server = ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE
            )

        #WebServer Role for S3 read access
        Web_iam_role = iam.Role(
            self, 'webserver-role',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
                ],
        )

        # Instances for the servers
        Instance_Webserver = ec2.Instance(self, 'Webserver',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=amazon_linux,
            vpc = WebVPC,
            role= Web_iam_role,
            security_group=WebSG,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC,),
            key_name='ec2-key-pair',
            block_devices=[ec2.BlockDevice(
                device_name='/dev/xvda',
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,
                    encrypted=True
                ))])

        Instance_Admin_server = ec2.Instance(self, 'Admin Server',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=windows_server,
            vpc = AdminVPC,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC,),
            security_group=AdminSG,
            key_name='ec2-key-pair',
            block_devices=[ec2.BlockDevice(
                device_name='/dev/xvda',
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,
                    encrypted=True
            ))])

        # Instance role and SSM Managed policy
        role = iam.Role(self, 'InstanceSSM', assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AmazonSSMManagedInstanceCore'))
        
        # S3 Bucket creation

        self.script_bucket = s3.Bucket(
            self, construct_id,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            enforce_ssl=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        # Sending the file to the bucket from the Bucket folder
        self.deployment = s3deploy.BucketDeployment(
            self, 'Script Bucket Deployment',
            destination_bucket=self.script_bucket,
            sources=[s3deploy.Source.asset(os.path.join("./project_atalla"))]
        )

        #Assigning roles to the EC2 instances to access files from the bucket
        self.script_bucket.add_to_resource_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                principals=[iam.ServicePrincipal('ec2.amazonaws.com')],
                actions=['s3:GetObject'],
                resources=[f'{self.script_bucket.bucket_arn}/*'])
        )

        # download webserver script
        script_path = Instance_Webserver.user_data.add_s3_download_command(
            bucket= self.script_bucket,
            bucket_key='userdata1.sh',
        )

        Instance_Webserver.user_data.add_execute_file_command(file_path=script_path)

        # Backup Vault creation seperately from the Backup Plan
        Web_backup_vault = backup.BackupVault(self, 'Web-backup-vault',
            backup_vault_name='Web_backup_vault',
            # encryption_key='ec2-key-pair',
            removal_policy=cdk.RemovalPolicy.DESTROY)

        # Plan creates a backup vault by default, plan_Web is for the Webserver
        plan_Web = backup.BackupPlan(self,'Backup_Plan',
        backup_vault=Web_backup_vault)  

        # plan: backup.BackupPlan , adding the Webserver EC2 instance to be saved as a backup daily
        plan_Web.add_selection('Selection',
            resources=[backup.BackupResource.from_ec2_instance(Instance_Webserver)],
            allow_restores=True
    )  

        # backup_vault: backup.BackupVault, adding rule of backup
        
        plan_Web.add_rule(backup.BackupPlanRule(
            completion_window=Duration.minutes(120),
            start_window=Duration.minutes(60),
            schedule_expression=event.Schedule.cron(
                week_day='*',
                hour='17',
                minute='0'),
                enable_continuous_backup=True,
                delete_after=Duration.days(7),
            )
        )

        # Backup vault for the admin created seperately
        Admin_backup_vault = backup.BackupVault(self, 'Admin-backup-vault',
            backup_vault_name='Admin_backup_vault',
            # encryption_key='ec2-key-pair',
            removal_policy=cdk.RemovalPolicy.DESTROY)

        # Saving the backups for 7 days from the Admin server
        plan_Admin = backup.BackupPlan(self, 'Plan_Admin',
        backup_vault=Admin_backup_vault)  

        # plan: backup.BackupPlan, adding the required resources
        plan_Admin.add_selection('Admin_backupplan',
            resources=[backup.BackupResource.from_ec2_instance(Instance_Admin_server)],
        )   
        
        plan_Admin.add_rule(backup.BackupPlanRule(
            completion_window=Duration.minutes(120),
            start_window=Duration.minutes(60),
            schedule_expression=event.Schedule.cron(
                week_day='1',
                hour='17',
                minute='0'),
                enable_continuous_backup=True,
                delete_after=Duration.days(7),
            )
        )