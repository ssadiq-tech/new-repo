
import aws_cdk as cdk
from my_cdk_app.my_cdk_app_stack import S3BucketStack

app = cdk.App()
S3BucketStack(app, "S3BucketStack")
app.synth()
