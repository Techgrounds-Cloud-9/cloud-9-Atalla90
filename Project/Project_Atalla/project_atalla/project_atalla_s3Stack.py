from aws_cdk import (
    Stack,
    aws_kms as kms,
    aws_s3 as s3,
    aws_s3_deployment as deploy,
    RemovalPolicy,
    )
from constructs import Construct

class projectAtallaS3Stack(Stack):

    storage = s3.Bucket

    def __init__(self, scope: Construct, construct_id: str, bucket_key: kms.Key, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        storage_bucket = s3.Bucket(self, "storage_bucket",
            encryption_key = bucket_key,
            versioned = True,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects = True,
            )

        ud_deploy = deploy.BucketDeployment(self, "ud_deploy",
            sources = [deploy.Source.asset(r"./project_atalla/user_data.zip")],
            destination_bucket = storage_bucket,
            )

        self.storage = storage_bucket