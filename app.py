#!/usr/bin/env python3
import os

import aws_cdk as cdk

from wayback.wayback_stack import WaybackStack


app = cdk.App()
WaybackStack(app, "WaybackStack",
    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    )

app.synth()
