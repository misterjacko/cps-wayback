import aws_cdk as core
import aws_cdk.assertions as assertions

from wayback.wayback_stack import WaybackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in wayback/wayback_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = WaybackStack(app, "wayback")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
