from aws_cdk import Stack
from aws_cdk import aws_wafv2 as wafv2
from constructs import Construct


class WAFCoreProtectionsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        wafv2.CfnWebACL(
            scope_=self,
            id="WebACL",
            default_action=wafv2.CfnWebACL.DefaultActionProperty(
                allow=wafv2.CfnWebACL.AllowActionProperty()
            ),
            scope="CLOUDFRONT",
            visibility_config=wafv2.CfnWebACL.VisibilityConfigProperty(
                cloud_watch_metrics_enabled=True,
                metric_name="WebACL",
                sampled_requests_enabled=True,
            ),
            rules=[
                wafv2.CfnWebACL.RuleProperty(
                    name="AIPRLRule",
                    priority=0,
                    statement=wafv2.CfnWebACL.StatementProperty(
                        managed_rule_group_statement=wafv2.CfnWebACL.ManagedRuleGroupStatementProperty(
                            name="AWSManagedRulesAmazonIpReputationList",
                            vendor_name="AWS",
                        ),
                    ),
                    visibility_config=wafv2.CfnWebACL.VisibilityConfigProperty(
                        cloud_watch_metrics_enabled=True,
                        metric_name="WebACL-AIPRL",
                        sampled_requests_enabled=True,
                    ),
                ),
                wafv2.CfnWebACL.RuleProperty(
                    name="CRSRule",
                    priority=10,
                    statement=wafv2.CfnWebACL.StatementProperty(
                        managed_rule_group_statement=wafv2.CfnWebACL.ManagedRuleGroupStatementProperty(
                            name="AWSManagedRulesCommonRuleSet", vendor_name="AWS"
                        ),
                    ),
                    visibility_config=wafv2.CfnWebACL.VisibilityConfigProperty(
                        cloud_watch_metrics_enabled=True,
                        metric_name="WebACL-CRS",
                        sampled_requests_enabled=True,
                    ),
                ),
                wafv2.CfnWebACL.RuleProperty(
                    name="KBIRSRule",
                    priority=20,
                    statement=wafv2.CfnWebACL.StatementProperty(
                        managed_rule_group_statement=wafv2.CfnWebACL.ManagedRuleGroupStatementProperty(
                            name="AWSManagedRulesKnownBadInputsRuleSet",
                            vendor_name="AWS",
                        ),
                    ),
                    visibility_config=wafv2.CfnWebACL.VisibilityConfigProperty(
                        cloud_watch_metrics_enabled=True,
                        metric_name="WebACL-KBIRS",
                        sampled_requests_enabled=True,
                    ),
                ),
            ],
        )
