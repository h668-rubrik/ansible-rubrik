# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HypervHierarchyObjectDescendentCount(Model):
    """HypervHierarchyObjectDescendentCount.

    :param cluster:
    :type cluster: int
    :param host:
    :type host: int
    :param vm:
    :type vm: int
    """

    _attribute_map = {
        'cluster': {'key': 'cluster', 'type': 'int'},
        'host': {'key': 'host', 'type': 'int'},
        'vm': {'key': 'vm', 'type': 'int'},
    }

    def __init__(self, cluster=None, host=None, vm=None):
        self.cluster = cluster
        self.host = host
        self.vm = vm
