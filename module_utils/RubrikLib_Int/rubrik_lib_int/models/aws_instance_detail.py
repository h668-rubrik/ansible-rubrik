# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AwsInstanceDetail(Model):
    """AwsInstanceDetail.

    :param aws_instance_type: The AWS instance type
    :type aws_instance_type: str
    :param aws_security_group_ids: For AWS instances, this is the security
     group ID. For images, this is the default security group ID for new
     instances from this image.
    :type aws_security_group_ids: list of str
    :param identity_file: File for AWS identity management
    :type identity_file: str
    """

    _attribute_map = {
        'aws_instance_type': {'key': 'awsInstanceType', 'type': 'str'},
        'aws_security_group_ids': {'key': 'awsSecurityGroupIds', 'type': '[str]'},
        'identity_file': {'key': 'identityFile', 'type': 'str'},
    }

    def __init__(self, aws_instance_type=None, aws_security_group_ids=None, identity_file=None):
        self.aws_instance_type = aws_instance_type
        self.aws_security_group_ids = aws_security_group_ids
        self.identity_file = identity_file
