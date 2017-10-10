# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .chart_summary import ChartSummary


class ChartData(ChartSummary):
    """ChartData.

    :param id: ID of the chart.
    :type id: str
    :param name: Name of the chart.
    :type name: str
    :param chart_type: Type of the chart. Possible values include: 'Donut',
     'VerticalBar', 'HorizontalBar', 'Line', 'StackedVerticalBar',
     'StackedHorizontalBar'
    :type chart_type: str or :class:`enum <rubriklib_int.models.enum>`
    :param attribute: Attribute for the chart. Possible values include:
     'TaskStatus', 'Hour', 'Day', 'Month', 'Quarter', 'Year', 'SlaDomain',
     'ObjectType', 'Location', 'ObjectName', 'ClusterLocation', 'TaskType',
     'ComplianceStatus'
    :type attribute: str or :class:`enum <rubriklib_int.models.enum>`
    :param measure: Measure for the chart. Possible values include:
     'NumberOfTasks', 'SuccessfulTaskCount', 'FailedTaskCount',
     'CanceledTaskCount', 'RunningTaskCount', 'AverageDuration',
     'DataTransferred', 'LogicalDataProtected', 'DataStored', 'DedupRatio',
     'LogicalDedupRatio', 'DataReductionPercent',
     'LogicalDataReductionPercent', 'TotalLocalStorage', 'TotalReplicaStorage',
     'TotalArchiveStorage', 'LocalStorageGrowth', 'ArchiveStorageGrowth',
     'ReplicaStorageGrowth', 'ComplianceStatusCount', 'InComplianceCount',
     'NonComplianceCount', 'StackedTaskCountByStatus', 'StackedTotalData',
     'StackedComplianceCountByStatus'
    :type measure: str or :class:`enum <rubriklib_int.models.enum>`
    :param data_columns: Data columns for the chart.
    :type data_columns: list of :class:`ChartDataColumn
     <rubriklib_int.models.ChartDataColumn>`
    :param remainder_data_column: Aggregated values for any remaining data.
    :type remainder_data_column: :class:`ChartDataColumn
     <rubriklib_int.models.ChartDataColumn>`
    """

    _validation = {
        'id': {'required': True},
        'name': {'required': True},
        'chart_type': {'required': True},
        'attribute': {'required': True},
        'measure': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'chart_type': {'key': 'chartType', 'type': 'str'},
        'attribute': {'key': 'attribute', 'type': 'str'},
        'measure': {'key': 'measure', 'type': 'str'},
        'data_columns': {'key': 'dataColumns', 'type': '[ChartDataColumn]'},
        'remainder_data_column': {'key': 'remainderDataColumn', 'type': 'ChartDataColumn'},
    }

    def __init__(self, id, name, chart_type, attribute, measure, data_columns=None, remainder_data_column=None):
        super(ChartData, self).__init__(id=id, name=name, chart_type=chart_type, attribute=attribute, measure=measure)
        self.data_columns = data_columns
        self.remainder_data_column = remainder_data_column
