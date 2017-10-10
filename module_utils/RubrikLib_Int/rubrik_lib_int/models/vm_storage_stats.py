# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VmStorageStats(Model):
    """VmStorageStats.

    :param id:
    :type id: str
    :param logical_bytes:
    :type logical_bytes: long
    :param ingested_bytes:
    :type ingested_bytes: long
    :param exclusive_physical_bytes:
    :type exclusive_physical_bytes: long
    :param shared_physical_bytes:
    :type shared_physical_bytes: long
    :param index_storage_bytes:
    :type index_storage_bytes: long
    """

    _validation = {
        'id': {'required': True},
        'logical_bytes': {'required': True},
        'ingested_bytes': {'required': True},
        'exclusive_physical_bytes': {'required': True},
        'shared_physical_bytes': {'required': True},
        'index_storage_bytes': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'logical_bytes': {'key': 'logicalBytes', 'type': 'long'},
        'ingested_bytes': {'key': 'ingestedBytes', 'type': 'long'},
        'exclusive_physical_bytes': {'key': 'exclusivePhysicalBytes', 'type': 'long'},
        'shared_physical_bytes': {'key': 'sharedPhysicalBytes', 'type': 'long'},
        'index_storage_bytes': {'key': 'indexStorageBytes', 'type': 'long'},
    }

    def __init__(self, id, logical_bytes, ingested_bytes, exclusive_physical_bytes, shared_physical_bytes, index_storage_bytes):
        self.id = id
        self.logical_bytes = logical_bytes
        self.ingested_bytes = ingested_bytes
        self.exclusive_physical_bytes = exclusive_physical_bytes
        self.shared_physical_bytes = shared_physical_bytes
        self.index_storage_bytes = index_storage_bytes
