# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HostFilesetShareSummary(Model):
    """HostFilesetShareSummary.

    :param id:
    :type id: str
    :param host_id:
    :type host_id: str
    :param hostname:
    :type hostname: str
    :param share_type: Possible values include: 'NFS', 'SMB'
    :type share_type: str or :class:`enum <rubriklib_int.models.enum>`
    :param export_point:
    :type export_point: str
    :param status:
    :type status: str
    :param primary_cluster_id:
    :type primary_cluster_id: str
    :param filesets:
    :type filesets: list of :class:`FilesetSummary
     <rubriklib_int.models.FilesetSummary>`
    :param username:
    :type username: str
    :param domain:
    :type domain: str
    """

    _validation = {
        'id': {'required': True},
        'host_id': {'required': True},
        'hostname': {'required': True},
        'share_type': {'required': True},
        'export_point': {'required': True},
        'status': {'required': True},
        'primary_cluster_id': {'required': True},
        'filesets': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'host_id': {'key': 'hostId', 'type': 'str'},
        'hostname': {'key': 'hostname', 'type': 'str'},
        'share_type': {'key': 'shareType', 'type': 'str'},
        'export_point': {'key': 'exportPoint', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'primary_cluster_id': {'key': 'primaryClusterId', 'type': 'str'},
        'filesets': {'key': 'filesets', 'type': '[FilesetSummary]'},
        'username': {'key': 'username', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
    }

    def __init__(self, id, host_id, hostname, share_type, export_point, status, primary_cluster_id, filesets, username=None, domain=None):
        self.id = id
        self.host_id = host_id
        self.hostname = hostname
        self.share_type = share_type
        self.export_point = export_point
        self.status = status
        self.primary_cluster_id = primary_cluster_id
        self.filesets = filesets
        self.username = username
        self.domain = domain
