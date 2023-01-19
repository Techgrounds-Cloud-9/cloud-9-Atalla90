#!/usr/bin/env python3
import aws_cdk as cdk

from project_atalla.project_atalla_vpcStack import projectAtallaVpcStack
from project_atalla.project_atalla_kmsStack import projectAtallaKmsStack
from project_atalla.project_atalla_s3Stack import projectAtallaS3Stack
from project_atalla.project_atalla_certStack import projectAtallaCertStack

app = cdk.App()

enc_Stack = projectAtallaKmsStack(app, "ProjectAtallaKmsStack",
    )

cert_Stack = projectAtallaCertStack(app, "ProjectAtallaCertStack"
    )

s3_Stack = projectAtallaS3Stack(app, "ProjectAtallaS3Stack",
    bucket_key = enc_Stack.bucket_key
    )

network_Stack = projectAtallaVpcStack(app, "ProjectAtallaVpcStack",
    web_cert = cert_Stack.atallaCert,
    mng_enc_key = enc_Stack.ebs_admin_key,
    ud_bucket = s3_Stack.storage
    )

app.synth()
