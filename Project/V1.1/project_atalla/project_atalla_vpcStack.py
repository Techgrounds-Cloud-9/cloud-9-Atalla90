from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_kms as kms,
    aws_elasticloadbalancingv2 as elb,
    aws_autoscaling as autoscale,
    aws_iam as iam,
    Duration,
    aws_certificatemanager as acm,
    aws_s3 as s3,
    )
from constructs import Construct

class projectAtallaVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, mng_enc_key: kms.Key, web_cert: acm.Certificate, ud_bucket: s3.Bucket,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc_atalla_web = ec2.Vpc(
            self, "vpc-atalla-web",
            ip_addresses= ec2.IpAddresses.cidr("10.10.10.0/24"),
            vpc_name = "vpc-atalla-web",
            nat_gateways = 1,
            availability_zones = ["eu-central-1a", "eu-central-1b", "eu-central-1c"],
            subnet_configuration = [
                ec2.SubnetConfiguration(name="private-subnet",
                    cidr_mask = 26,
                    subnet_type = ec2.SubnetType.PRIVATE_WITH_EGRESS),
                ec2.SubnetConfiguration(name="public-subnet",
                    cidr_mask = 28,
                    subnet_type = ec2.SubnetType.PUBLIC,
                    map_public_ip_on_launch = False),
            ]
        )

        web_acl = ec2.NetworkAcl(self, "web-acl",
            vpc = vpc_atalla_web,
            subnet_selection = ec2.SubnetSelection(
                availability_zones = ["eu-central-1a", "eu-central-1b", "eu-central-1c"],
                subnet_type = ec2.SubnetType.PRIVATE_WITH_EGRESS
            )
        )

        alb_acl = ec2.NetworkAcl(self, "alb-acl",
            vpc = vpc_atalla_web,
            subnet_selection = ec2.SubnetSelection(
                availability_zones = ["eu-central-1a", "eu-central-1b", "eu-central-1c"],
                subnet_type = ec2.SubnetType.PUBLIC
            )
        )

        web_sg = ec2.SecurityGroup(self, "webSG",
            vpc = vpc_atalla_web,
            allow_all_outbound = True
        )

        vpc_atalla_admin = ec2.Vpc(self, "vpc-atalla-admin",
            ip_addresses= ec2.IpAddresses.cidr("10.20.20.0/24"),
            vpc_name = "vpc-atalla-admin",
            nat_gateways = 0,
            availability_zones = ["eu-central-1a", "eu-central-1b"],
            subnet_configuration = [
                ec2.SubnetConfiguration(name="public-subnet",
                    cidr_mask = 25,
                    subnet_type = ec2.SubnetType.PUBLIC),
            ]
        )

        admin_acl = ec2.NetworkAcl(self, "admin-acl",
            vpc = vpc_atalla_admin,
            subnet_selection = ec2.SubnetSelection(
                availability_zones = ["eu-central-1b"]
                )
        )

        admin_sg = ec2.SecurityGroup(self, "adminSG",
            vpc = vpc_atalla_admin,
            allow_all_outbound = True)

        atalla_peering = ec2.CfnVPCPeeringConnection(self, "atalla_peering",
            peer_vpc_id = vpc_atalla_admin.vpc_id,
            vpc_id = vpc_atalla_web.vpc_id)

        admin_subnet_count = 0
        for admin_subnet in vpc_atalla_admin.public_subnets:
            admin_subnet_count += 1
            ec2.CfnRoute(self, "admin_to_web_route" + str(admin_subnet_count),
                route_table_id = admin_subnet.route_table.route_table_id,
                destination_cidr_block = "10.10.10.0/24",
                vpc_peering_connection_id = atalla_peering.attr_id)
        web_subnet_count = 0
        for web_subnet in vpc_atalla_web.private_subnets:  
            web_subnet_count += 1      
            ec2.CfnRoute(self, "web_to_admin_route" + str(web_subnet_count),
                route_table_id = web_subnet.route_table.route_table_id,
                destination_cidr_block = "10.20.20.0/24",
                vpc_peering_connection_id = atalla_peering.attr_id)

        atalla_ssh_KeyPair = ec2.CfnKeyPair(self, "ws_KeyPair",
            key_name = "Atalla_ssh_KeyPair2390",
        )

        admin_server = ec2.Instance(self, "admin_server",
            vpc = vpc_atalla_admin,
            instance_type = ec2.InstanceType(instance_type_identifier = "t3.micro"),
            vpc_subnets = ec2.SubnetSelection(availability_zones= ["eu-central-1b"]),
            security_group = admin_sg,
            key_name = "Atalla_ssh_KeyPair2390",
            machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),
            user_data = ec2.UserData.for_windows(),
            block_devices = [ec2.BlockDevice(
                device_name = "/dev/sda1",
                volume = ec2.BlockDeviceVolume.ebs(
                    volume_size = 30,
                    encrypted = True,
                    kms_key = mng_enc_key,
                    delete_on_termination = True
                    )
                )
            ],
        )

        admin_server.user_data.add_commands("<powershell>",
            "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0",
            "Start-Service ssh-agent",
            "Start-Service sshd")

        web_ingress100 = web_acl.add_entry("rule-http-ipv4-ingress",
            cidr = ec2.AclCidr.ipv4("10.10.10.0/24"),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        web_ingress120 = web_acl.add_entry("rule-ssh-ingress",
            cidr = ec2.AclCidr.ipv4("10.20.20.0/24"),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        web_ingress130 = web_acl.add_entry("rule-ephemeral-ingress-ipv4",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        web_ingress160 = web_acl.add_entry("rule-ephemeral-ipv6-ingress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 160,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        web_egress100 = web_acl.add_entry("rule-http-ipv4-egress",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        web_egress110 = web_acl.add_entry("rule-https-ipv4-egress",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        web_egress120 = web_acl.add_entry("rule-ephemeral-egress-ipv4",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        web_egress130 = web_acl.add_entry("rule-http-ipv6-egress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        web_egress140 = web_acl.add_entry("rule-https-ipv6-egress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 140,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        web_egress150 = web_acl.add_entry("rule-ephemeral-ipv6-egress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 150,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)

        ws_ingress10 = web_sg.add_ingress_rule(peer = ec2.Peer.ipv4("10.10.10.0/24"), connection = ec2.Port.tcp(80))
        ws_ingress30 = web_sg.add_ingress_rule(peer = ec2.Peer.ipv4("10.20.20.0/24"), connection = ec2.Port.tcp(22))

        alb_ingress100 = alb_acl.add_entry("rule-http-ipv4-ingress",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        alb_ingress110 = alb_acl.add_entry("rule-https-ipv4-ingress",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        alb_ingress120 = alb_acl.add_entry("rule-ephemeral-ingress-ipv4",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        alb_ingress130 = alb_acl.add_entry("rule-http-ipv6-ingress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        alb_ingress140 = alb_acl.add_entry("rule-https-ipv6-ingress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 140,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        alb_ingress150 = alb_acl.add_entry("rule-ephemeral-ipv6-ingress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 150,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        alb_egress100 = alb_acl.add_entry("rule-http-ipv4-egress",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        alb_egress110 = alb_acl.add_entry("rule-https-ipv4-egress",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        alb_egress120 = alb_acl.add_entry("rule-ephemeral-egress-ipv4",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        alb_egress150 = alb_acl.add_entry("rule-ephemeral-ipv6-egress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 150,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)

        admin_ingress100 = admin_acl.add_entry("rule-ssh-ingress-home",
            cidr = ec2.AclCidr.ipv4("217.103.21.122/32"),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_ingress110 = admin_acl.add_entry("rule-rdp-ingress-home",
            cidr = ec2.AclCidr.ipv4("217.103.21.122/32"),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(3389),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_ingress120 = admin_acl.add_entry("rule-ephemeral-ingress-web",
            cidr = ec2.AclCidr.ipv4("10.10.10.0/24"),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_ingress130 = admin_acl.add_entry("rule-ephemeral-ipv6-ingress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_ingress140 = admin_acl.add_entry("rule-ephemeral-ingress",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 140,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_egress100 = admin_acl.add_entry("rule-ssh-egress-web",
            cidr = ec2.AclCidr.ipv4("10.10.10.0/24"),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_egress110 = admin_acl.add_entry("rule-http-ipv6-egress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_egress120 = admin_acl.add_entry("rule-https-ipv6-egress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_egress130 = admin_acl.add_entry("rule-ephemeral-egress-home",
            cidr = ec2.AclCidr.ipv4("217.103.21.122/32"),
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_egress140 = admin_acl.add_entry("rule-http-ingress-home",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 140,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)
        admin_egress150 = admin_acl.add_entry("rule-https-ingress-home",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 150,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW)

        ms_ingress50 = admin_sg.add_ingress_rule(peer = ec2.Peer.ipv4("217.103.21.122/32"), connection = ec2.Port.tcp(22))
        ms_ingress60 = admin_sg.add_ingress_rule(peer = ec2.Peer.ipv4("217.103.21.122/32"), connection = ec2.Port.tcp(3389))

        launchTemp = ec2.LaunchTemplate(self, "launchTemp",
            instance_type = ec2.InstanceType(instance_type_identifier = "t3.micro"),
            machine_image = ec2.AmazonLinuxImage(),
            security_group = web_sg,
            detailed_monitoring = True,
            block_devices = [ec2.BlockDevice(
                device_name = "/dev/xvda",
                volume = ec2.BlockDeviceVolume.ebs(
                    volume_size = 8,
                    encrypted = True,
                    delete_on_termination = True,
                    )
                )
            ],
            key_name = "Atalla_ssh_KeyPair2390",
            role = iam.Role(self, "role", assumed_by= iam.ServicePrincipal("ec2.amazonaws.com")),
            user_data = ec2.UserData.for_linux()
        )

        ssm_policy = launchTemp.role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEC2RoleforSSM"))

        ud_policy = ud_bucket.grant_read(launchTemp.role)
        ud_path = launchTemp.user_data.add_s3_download_command(bucket = ud_bucket, bucket_key = "user_data.sh")
        ud_exe = launchTemp.user_data.add_execute_file_command(file_path = ud_path)

        asg = autoscale.AutoScalingGroup(self, "asg",
            vpc = vpc_atalla_web,
            vpc_subnets = ec2.SubnetSelection(subnet_type = ec2.SubnetType.PRIVATE_WITH_EGRESS),
            launch_template = launchTemp,
            min_capacity = 1,
            max_capacity = 3,
            cooldown = Duration.minutes(5),
            health_check = autoscale.HealthCheck.elb(grace = Duration.minutes(5)),
        )

        scale_policy = asg.scale_on_cpu_utilization(id = "scale_policy",
            target_utilization_percent = 70,
        )
        
        apLb = elb.ApplicationLoadBalancer (self, "apLb",
            vpc = vpc_atalla_web,
            vpc_subnets = ec2.SubnetSelection(subnet_type = ec2.SubnetType.PUBLIC),
            internet_facing = True,
        )

        listener443 = apLb.add_listener("listener443", port = 443, certificates = [web_cert])
        aplLb_redi = apLb.add_redirect()
        target80 = listener443.add_targets("target80",
            port = 80,
            targets = [asg],
            health_check = elb.HealthCheck(
                enabled = True,
                interval = Duration.seconds(5),
                protocol = elb.Protocol.HTTP,
                port = "80",
                timeout = Duration.seconds(2),
                path = "/",
                ),
        )