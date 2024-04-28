#!/usr/bin/env python3
import os

import aws_cdk as cdk

from waf_core_protections.waf_core_protections_stack import WAFCoreProtectionsStack

app = cdk.App()
WAFCoreProtectionsStack(
    app,
    "WafCoreProtectionsStack",
    env=cdk.Environment(
        account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
        region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]),
    ),
)
app.synth()
