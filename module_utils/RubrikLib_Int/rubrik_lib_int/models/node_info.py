# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .node_status import NodeStatus


class NodeInfo(NodeStatus):
    """NodeInfo.

    :param id:
    :type id: str
    :param brik_id:
    :type brik_id: str
    :param status:
    :type status: str
    :param ip_address:
    :type ip_address: str
    :param needs_inspection:
    :type needs_inspection: bool
    :param cpu_cores:
    :type cpu_cores: long
    :param ram:
    :type ram: long
    :param network_speed:
    :type network_speed: str
    :param hdd:
    :type hdd: list of :class:`DiskInfo <rubriklib_int.models.DiskInfo>`
    :param ssd:
    :type ssd: list of :class:`DiskInfo <rubriklib_int.models.DiskInfo>`
    """

    _validation = {
        'id': {'required': True},
        'brik_id': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'brik_id': {'key': 'brikId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'needs_inspection': {'key': 'needsInspection', 'type': 'bool'},
        'cpu_cores': {'key': 'cpuCores', 'type': 'long'},
        'ram': {'key': 'ram', 'type': 'long'},
        'network_speed': {'key': 'networkSpeed', 'type': 'str'},
        'hdd': {'key': 'hdd', 'type': '[DiskInfo]'},
        'ssd': {'key': 'ssd', 'type': '[DiskInfo]'},
    }

    def __init__(self, id, brik_id, status, ip_address=None, needs_inspection=None, cpu_cores=None, ram=None, network_speed=None, hdd=None, ssd=None):
        super(NodeInfo, self).__init__(id=id, brik_id=brik_id, status=status, ip_address=ip_address, needs_inspection=needs_inspection)
        self.cpu_cores = cpu_cores
        self.ram = ram
        self.network_speed = network_speed
        self.hdd = hdd
        self.ssd = ssd
