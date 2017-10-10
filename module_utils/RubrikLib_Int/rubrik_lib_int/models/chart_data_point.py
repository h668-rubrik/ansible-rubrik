# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChartDataPoint(Model):
    """ChartDataPoint.

    :param measure: Measure label for the data.
    :type measure: str
    :param value: The number value.
    :type value: float
    """

    _validation = {
        'measure': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'measure': {'key': 'measure', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(self, measure, value):
        self.measure = measure
        self.value = value
