from aws_cdk import (
    Duration,
    aws_lambda as lambda_,
    aws_events as event,
    aws_events_targets as targets,
    Stack,
)
from constructs import Construct
import aws_cdk.aws_lambda_python_alpha as lambda_python

class WaybackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        wayback_function = lambda_python.PythonFunction(
            self,
            "wayback",
            function_name="WaybackArchiver",
            runtime=lambda_.Runtime.PYTHON_3_9,
            entry="./wayback_app",
            index="app.py",
            handler="lambda_handler",
            memory_size=128,
            timeout=Duration.seconds(300),
            )

        event.Rule(self, "WaybackRule",
            rule_name="WaybackRule",
            schedule=event.Schedule.cron(
                minute="0", 
                hour="10",
                ),
            targets=[
                targets.LambdaFunction(wayback_function),
                ],
            )
