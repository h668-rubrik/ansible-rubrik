# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateSmtpInstanceDefinition(Model):
    """UpdateSmtpInstanceDefinition.

    :param smtp_hostname:
    :type smtp_hostname: str
    :param smtp_port:
    :type smtp_port: long
    :param smtp_security:
    :type smtp_security: str
    :param smtp_username:
    :type smtp_username: str
    :param smtp_password:
    :type smtp_password: str
    :param from_email_id:
    :type from_email_id: str
    """

    _attribute_map = {
        'smtp_hostname': {'key': 'smtpHostname', 'type': 'str'},
        'smtp_port': {'key': 'smtpPort', 'type': 'long'},
        'smtp_security': {'key': 'smtpSecurity', 'type': 'str'},
        'smtp_username': {'key': 'smtpUsername', 'type': 'str'},
        'smtp_password': {'key': 'smtpPassword', 'type': 'str'},
        'from_email_id': {'key': 'fromEmailId', 'type': 'str'},
    }

    def __init__(self, smtp_hostname=None, smtp_port=None, smtp_security=None, smtp_username=None, smtp_password=None, from_email_id=None):
        self.smtp_hostname = smtp_hostname
        self.smtp_port = smtp_port
        self.smtp_security = smtp_security
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.from_email_id = from_email_id
