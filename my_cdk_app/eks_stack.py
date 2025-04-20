from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_eks as eks,
)
from constructs import Construct

class EksClusterStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Use default VPC
        vpc = ec2.Vpc.from_lookup(self, "DefaultVpc", is_default=True)


        # Create the EKS Cluster
        cluster = eks.Cluster(
            self, "MyEksCluster",
            vpc=vpc,
            default_capacity=2,
            version=eks.KubernetesVersion.V1_24,
        )

        # Example: Add Helm chart or manifest if needed
        # cluster.add_helm_chart(...)
