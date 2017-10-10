# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HypervHostUpdate(Model):
    """HypervHostUpdate.

    :param configured_sla_domain_id: Assign this VM to the given SLA domain.
    :type configured_sla_domain_id: str
    """

    _attribute_map = {
        'configured_sla_domain_id': {'key': 'configuredSlaDomainId', 'type': 'str'},
    }

    def __init__(self, configured_sla_domain_id=None):
        self.configured_sla_domain_id = configured_sla_domain_id
