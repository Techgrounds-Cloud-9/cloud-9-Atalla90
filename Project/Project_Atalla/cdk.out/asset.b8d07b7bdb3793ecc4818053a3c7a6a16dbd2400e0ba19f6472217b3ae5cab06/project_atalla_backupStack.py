from aws_cdk import (
    Stack,
    aws_kms as kms,
    aws_backup as backup,
    aws_ec2 as ec2,
    aws_events as events,
    Duration,
    RemovalPolicy,
    aws_autoscaling as autoscale
)
from constructs import Construct

class projectAtallaBackupStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, ws_bkp_key: kms.Key, ws: autoscale.AutoScalingGroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ws_bkp_vault = backup.BackupVault(self, "ws_bkp_vault",
            encryption_key = ws_bkp_key,
            removal_policy = RemovalPolicy.DESTROY,
        )

        ws_bkp_plan = backup.BackupPlan(self, "ws_bkp_plan",
            backup_plan_name = "ws_bkp_plan",
            backup_plan_rules = [backup.BackupPlanRule(schedule_expression = events.Schedule.cron
                (day = "*", hour = "0", minute = "0", month = "*", year = "*")),
                backup.BackupPlanRule(delete_after = Duration.days(7)),
            ],
            backup_vault = ws_bkp_vault
        )

        ws_bkp_plan.add_selection("ws_bkp_res", resources = [
            backup.BackupResource.from_ec2_instance
            ],
            allow_restores = True,
        )