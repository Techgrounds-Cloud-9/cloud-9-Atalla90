from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_s3_assets as assets,
    aws_kms as kms,
    aws_elasticloadbalancingv2 as elb,
    aws_autoscaling as autoscale,
    aws_iam as iam,
    Duration,
    )
from constructs import Construct

class projectAtallaVpcStack(Stack):

    # webserver = ec2.Instance
    web_asg = autoscale.AutoScalingGroup

    def __init__(self, scope: Construct, construct_id: str, ws_enc_key: kms.Key, mng_enc_key: kms.Key, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc_atalla_web = ec2.Vpc(
            self, "vpc-atalla-web",
            ip_addresses= ec2.IpAddresses.cidr("10.10.10.0/24"),
            vpc_name = "vpc-atalla-web",
            nat_gateways = 0,
            availability_zones = ["eu-central-1a", "eu-central-1b"],
            subnet_configuration = [
                ec2.SubnetConfiguration(name="public-subnet",
                    cidr_mask = 25,
                    subnet_type = ec2.SubnetType.PUBLIC),
            ]
        )

        web_acl = ec2.NetworkAcl(self, "web-acl",
            vpc = vpc_atalla_web,
            subnet_selection = ec2.SubnetSelection(
                availability_zones = ["eu-central-1a"]
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

        admin_to_web_route = ec2.CfnRoute(self, "admin_to_web_route",
            route_table_id = vpc_atalla_admin.public_subnets[1].route_table.route_table_id,
            destination_cidr_block = "10.10.10.0/25",
            vpc_peering_connection_id = atalla_peering.attr_id)
        web_to_admin_route = ec2.CfnRoute(self, "web_to_admin_route",
            route_table_id = vpc_atalla_web.public_subnets[0].route_table.route_table_id,
            destination_cidr_block = "10.20.20.128/25",
            vpc_peering_connection_id = atalla_peering.attr_id)

        ws_KeyPair = ec2.CfnKeyPair(self, "ws_KeyPair",
            key_name = "ws_KeyPair2390",
            tags = [{"key":"name", "value":"web-key"}])

        mng_KeyPair = ec2.CfnKeyPair(self, "mng_KeyPair",
            key_name = "mng_KeyPair2390",
            tags = [{"key":"name", "value":"admin-key"}])

        # web_server = ec2.Instance(self, "web_server",
        #     vpc = vpc_atalla_web,
        #     instance_type = ec2.InstanceType(instance_type_identifier = "t3.micro"),
        #     vpc_subnets = ec2.SubnetSelection(availability_zones= ["eu-central-1a"]),
        #     security_group = web_sg,
        #     key_name = "ws_KeyPair2390",
        #     machine_image=ec2.AmazonLinuxImage(),
        #     block_devices = [ec2.BlockDevice(
        #         device_name = "/dev/xvda",
        #         volume = ec2.BlockDeviceVolume.ebs(
        #             volume_size = 8,
        #             encrypted = True,
        #             kms_key = ws_enc_key,
        #             delete_on_termination = True
        #             )
        #         )
        #     ],
        # )

        # ud_source = assets.Asset(self, "ud_source", path= r"./project_atalla/user_data.sh")
        # ud_policy = ud_source.bucket.grant_read(web_server.role)
        # ud_path = web_server.user_data.add_s3_download_command(bucket = ud_source.bucket, bucket_key = ud_source.s3_object_key)
        # ud_exe = web_server.user_data.add_execute_file_command(file_path = ud_path)

        # self.webserver = web_server

        admin_server = ec2.Instance(self, "admin_server",
            vpc = vpc_atalla_admin,
            instance_type = ec2.InstanceType(instance_type_identifier = "t3.micro"),
            vpc_subnets = ec2.SubnetSelection(availability_zones= ["eu-central-1b"]),
            security_group = admin_sg,
            key_name = "mng_KeyPair2390",
            machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE),
            block_devices = [ec2.BlockDevice(
                device_name = "/dev/xvda",
                volume = ec2.BlockDeviceVolume.ebs(
                    volume_size = 8,
                    encrypted = True,
                    kms_key = mng_enc_key,
                    delete_on_termination = True
                    )
                )
            ]
        )

        web_ingress100 = web_acl.add_entry("rule-http-ipv4-ingress",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        web_ingress110 = web_acl.add_entry("rule-https-ipv4-ingress",
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        web_ingress120 = web_acl.add_entry("rule-ssh-ingress",
            cidr = ec2.AclCidr.ipv4("10.20.20.128/25"),
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
        web_ingress140 = web_acl.add_entry("rule-http-ipv6-ingress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 140,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW)
        web_ingress150 = web_acl.add_entry("rule-https-ipv6-ingress",
            cidr = ec2.AclCidr.any_ipv6(),
            rule_number = 150,
            traffic = ec2.AclTraffic.tcp_port(443),
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

        ws_ingress10 = web_sg.add_ingress_rule(peer = ec2.Peer.any_ipv4(), connection = ec2.Port.tcp(80))
        ws_ingress20 = web_sg.add_ingress_rule(peer = ec2.Peer.any_ipv4(), connection = ec2.Port.tcp(443))
        ws_ingress30 = web_sg.add_ingress_rule(peer = ec2.Peer.ipv4("10.20.20.128/25"), connection = ec2.Port.tcp(22))
        ws_ingress60 = web_sg.add_ingress_rule(peer = ec2.Peer.any_ipv6(), connection = ec2.Port.tcp(80))
        ws_ingress70 = web_sg.add_ingress_rule(peer = ec2.Peer.any_ipv6(), connection = ec2.Port.tcp(443))

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
            cidr = ec2.AclCidr.ipv4("10.10.10.0/25"),
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
            cidr = ec2.AclCidr.ipv4("10.10.10.0/25"),
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
            block_devices = [ec2.BlockDevice(
                device_name = "/dev/xvda",
                volume = ec2.BlockDeviceVolume.ebs(
                    volume_size = 8,
                    encrypted = True,
                    kms_key = ws_enc_key,
                    delete_on_termination = True,
                    )
                )
            ],
            key_name = "ws_KeyPair2390",
            role = iam.Role(
                self,
               "id",
                assumed_by = iam.ServicePrincipal("ec2.amazonaws.com")
                ),
            user_data = ec2.UserData.for_linux()
            )

        asg = autoscale.AutoScalingGroup(self, "asg",
            vpc = vpc_atalla_web,
            # instance_type = ec2.InstanceType(instance_type_identifier = "t3.micro"),
            launch_template = launchTemp,
            # machine_image = ec2.AmazonLinuxImage(),
            # security_group = web_sg,
            # block_devices = [autoscale.BlockDevice(
            #     device_name = "/dev/xvda",
            #     volume = autoscale.BlockDeviceVolume.ebs(
            #         volume_size = 8,
            #         encrypted = True,
            #         kms_key = ws_enc_key,
            #         delete_on_termination = True
            #         )
            #     )
            # ],
            min_capacity = 1,
            max_capacity = 3,
            health_check = autoscale.HealthCheck.elb(grace = Duration.minutes(30))
            # key_name = "ws_KeyPair2390",
        )

        apLb = elb.ApplicationLoadBalancer (self, "apLb",
            vpc = vpc_atalla_web,
            internet_facing = True,
            )

        listener80 = apLb.add_listener("listener80", port = 80)
        # listener443 = apLb.add_listener("listener443", port = 443)

        target80 = listener80.add_targets("target80", port = 80, targets = [asg])
        # target443 = listener443.add_targets("target443", port = 443, targets = [asg])

        ud_source = assets.Asset(self, "ud_source", path= r"./project_atalla/user_data.sh")
        ud_policy = ud_source.bucket.grant_read(launchTemp.role)
        ud_path = launchTemp.user_data.add_s3_download_command(bucket = ud_source.bucket, bucket_key = ud_source.s3_object_key)
        ud_exe = launchTemp.user_data.add_execute_file_command(file_path = ud_path)

        self.web_asg = asg






