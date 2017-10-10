# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MssqlRestoreEstimateResult(Model):
    """MssqlRestoreEstimateResult.

    :param bytes_from_cloud: Estimate of number of bytes that need to be
     downloaded from the cloud.
    :type bytes_from_cloud: long
    """

    _validation = {
        'bytes_from_cloud': {'required': True},
    }

    _attribute_map = {
        'bytes_from_cloud': {'key': 'bytesFromCloud', 'type': 'long'},
    }

    def __init__(self, bytes_from_cloud):
        self.bytes_from_cloud = bytes_from_cloud
