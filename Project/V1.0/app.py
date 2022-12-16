#!/usr/bin/env python3
import aws_cdk as cdk

from project_atalla.project_atalla_vpcStack import projectAtallaVpcStack
from project_atalla.project_atalla_kmsStack import projectAtallaKmsStack
from project_atalla.project_atalla_backupStack import projectAtallaBackupStack


app = cdk.App()


enc_Stack = projectAtallaKmsStack(app, "ProjectAtallaKmsStack",
    )

Network_Stack = projectAtallaVpcStack(app, "ProjectAtallaVpcStack",
    ws_enc_key = enc_Stack.ebs_web_key,
    mng_enc_key = enc_Stack.ebs_admin_key,
    )

Backup_Stack = projectAtallaBackupStack(app, "ProjectAtallaBackupStack",
    ws = Network_Stack.webserver, ws_bkp_key = enc_Stack.vault_key)

app.synth()
