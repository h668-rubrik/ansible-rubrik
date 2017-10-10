# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GlobalJarvisConfig(Model):
    """GlobalJarvisConfig.

    :param sfdc_org_id: Salesforce Organization ID for Rubrik
    :type sfdc_org_id: str
    :param sfdc_hostname: Salesforce hostname for Rubrik support portal
    :type sfdc_hostname: str
    :param sfdc_auth_end_point: Salesforce community portal endpoint for login
    :type sfdc_auth_end_point: str
    :param sfdc_registration_svc_end_point: Salesforce community portal
     endpoint for cluster registration Service
    :type sfdc_registration_svc_end_point: str
    """

    _attribute_map = {
        'sfdc_org_id': {'key': 'sfdcOrgId', 'type': 'str'},
        'sfdc_hostname': {'key': 'sfdcHostname', 'type': 'str'},
        'sfdc_auth_end_point': {'key': 'sfdcAuthEndPoint', 'type': 'str'},
        'sfdc_registration_svc_end_point': {'key': 'sfdcRegistrationSvcEndPoint', 'type': 'str'},
    }

    def __init__(self, sfdc_org_id=None, sfdc_hostname=None, sfdc_auth_end_point=None, sfdc_registration_svc_end_point=None):
        self.sfdc_org_id = sfdc_org_id
        self.sfdc_hostname = sfdc_hostname
        self.sfdc_auth_end_point = sfdc_auth_end_point
        self.sfdc_registration_svc_end_point = sfdc_registration_svc_end_point
