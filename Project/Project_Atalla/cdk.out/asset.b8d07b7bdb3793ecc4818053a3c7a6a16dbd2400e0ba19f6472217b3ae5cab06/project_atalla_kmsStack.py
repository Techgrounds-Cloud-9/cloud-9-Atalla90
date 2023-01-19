from aws_cdk import (
    Stack,
    aws_kms as kms,
    RemovalPolicy
)
from constructs import Construct

class projectAtallaKmsStack(Stack):

    ebs_admin_key = kms.Key
    ebs_web_key = kms.Key
    vault_key = kms.Key

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ebs_Admin_Key = kms.Key(self, "EBS_Admin_Key",
            enable_key_rotation = True,
            alias = "EBS_Admin_Key",
            removal_policy = RemovalPolicy.DESTROY)
        self.ebs_admin_key = ebs_Admin_Key

        ebs_Web_Key = kms.Key(self, "EBS_Web_Key",
            enable_key_rotation = True,
            alias = "EBS_Web_Key",
            removal_policy = RemovalPolicy.DESTROY)
        self.ebs_web_key = ebs_Web_Key

        vault_Key = kms.Key(self, "Vault_Key",
            enable_key_rotation = True,
            alias = "Vault_Key",
            removal_policy = RemovalPolicy.DESTROY)
        self.vault_key = vault_Key



