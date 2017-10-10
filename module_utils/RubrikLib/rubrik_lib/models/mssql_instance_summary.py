# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .mssql_non_sla_properties import MssqlNonSlaProperties


class MssqlInstanceSummary(MssqlNonSlaProperties):
    """MssqlInstanceSummary.

    :param log_backup_frequency_in_seconds: Seconds between two log backups. A
     value of 0 disables log backup.
    :type log_backup_frequency_in_seconds: int
    :param log_retention_hours: Number of hours to retain a log backup. When
     the value is set to -1 the Rubrik cluster retains the log backup until the
     database snapshots that precede the log backup have expired.
    :type log_retention_hours: int
    :param copy_only: Set to true for copy-only backups of the database. Set
     to false for full or differential backups of the database.
    :type copy_only: bool
    :param id:
    :type id: str
    :param internal_timestamp:
    :type internal_timestamp: long
    :param name:
    :type name: str
    :param primary_cluster_id:
    :type primary_cluster_id: str
    :param root_properties:
    :type root_properties: :class:`MssqlRootProperties
     <rubriklib.models.MssqlRootProperties>`
    :param cluster_instance_address: The address of the instance in a Windows
     server failover cluster, populated only if it belongs to one.
    :type cluster_instance_address: str
    :param protection_date:
    :type protection_date: date
    :param version:
    :type version: str
    :param configured_sla_domain_id: SLA Domain ID assigned to instance
    :type configured_sla_domain_id: str
    :param configured_sla_domain_name: SLA Domain name assigned to instance
    :type configured_sla_domain_name: str
    """

    _attribute_map = {
        'log_backup_frequency_in_seconds': {'key': 'logBackupFrequencyInSeconds', 'type': 'int'},
        'log_retention_hours': {'key': 'logRetentionHours', 'type': 'int'},
        'copy_only': {'key': 'copyOnly', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'internal_timestamp': {'key': 'internalTimestamp', 'type': 'long'},
        'name': {'key': 'name', 'type': 'str'},
        'primary_cluster_id': {'key': 'primaryClusterId', 'type': 'str'},
        'root_properties': {'key': 'rootProperties', 'type': 'MssqlRootProperties'},
        'cluster_instance_address': {'key': 'clusterInstanceAddress', 'type': 'str'},
        'protection_date': {'key': 'protectionDate', 'type': 'date'},
        'version': {'key': 'version', 'type': 'str'},
        'configured_sla_domain_id': {'key': 'configuredSlaDomainId', 'type': 'str'},
        'configured_sla_domain_name': {'key': 'configuredSlaDomainName', 'type': 'str'},
    }

    def __init__(self, log_backup_frequency_in_seconds=None, log_retention_hours=None, copy_only=None, id=None, internal_timestamp=None, name=None, primary_cluster_id=None, root_properties=None, cluster_instance_address=None, protection_date=None, version=None, configured_sla_domain_id=None, configured_sla_domain_name=None):
        super(MssqlInstanceSummary, self).__init__(log_backup_frequency_in_seconds=log_backup_frequency_in_seconds, log_retention_hours=log_retention_hours, copy_only=copy_only)
        self.id = id
        self.internal_timestamp = internal_timestamp
        self.name = name
        self.primary_cluster_id = primary_cluster_id
        self.root_properties = root_properties
        self.cluster_instance_address = cluster_instance_address
        self.protection_date = protection_date
        self.version = version
        self.configured_sla_domain_id = configured_sla_domain_id
        self.configured_sla_domain_name = configured_sla_domain_name
