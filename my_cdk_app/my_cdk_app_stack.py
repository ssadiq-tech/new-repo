from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
)
from constructs import Construct

class S3BucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an S3 bucket with versioning enabled
        s3.Bucket(self,
            "MySampleBucket",
            bucket_name="my-sample-cdk-bucket-123456",  # Must be globally unique
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,  # Fixed reference
            auto_delete_objects=True
        )
