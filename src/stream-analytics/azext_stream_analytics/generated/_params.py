# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from azext_stream_analytics.action import (
    AddIdentity,
    AddTransformation,
    AddJobStorageAccount
)


def load_arguments(self, _):

    with self.argument_context('stream-analytics job list') as c:
        c.argument('expand', type=str, help='The $expand OData query parameter. This is a comma-separated list of '
                   'additional streaming job properties to include in the response, beyond the default set returned '
                   'when this parameter is absent. The default set is all streaming job properties other than '
                   '\'inputs\', \'transformation\', \'outputs\', and \'functions\'.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('stream-analytics job show') as c:
        c.argument('expand', type=str, help='The $expand OData query parameter. This is a comma-separated list of '
                   'additional streaming job properties to include in the response, beyond the default set returned '
                   'when this parameter is absent. The default set is all streaming job properties other than '
                   '\'inputs\', \'transformation\', \'outputs\', and \'functions\'.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the streaming job.')

    with self.argument_context('stream-analytics job create') as c:
        c.argument('if_match', type=str, help='The ETag of the streaming job. Omit this value to always overwrite the '
                   'current record set. Specify the last-seen ETag value to prevent accidentally overwriting '
                   'concurrent changes.')
        c.argument('if_none_match', type=str, help='Set to \'*\' to allow a new streaming job to be created, but to '
                   'prevent updating an existing record set. Other values will result in a 412 Pre-condition Failed '
                   'response.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the streaming job.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('identity', action=AddIdentity, nargs='+', help='Describes the system-assigned managed identity '
                   'assigned to this job that can be used to authenticate with inputs and outputs.')
        c.argument('job_type', arg_type=get_enum_type(['Cloud', 'Edge']), help='Describes the type of the job. Valid '
                   'modes are `Cloud` and \'Edge\'.')
        c.argument('output_start_mode', arg_type=get_enum_type(['JobStartTime', 'CustomTime', 'LastOutputEventTime']),
                   help='This property should only be utilized when it is desired that the job be started immediately '
                   'upon creation. Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether '
                   'the starting point of the output event stream should start whenever the job is started, start at a '
                   'custom user time stamp specified via the outputStartTime property, or start from the last event '
                   'output time.')
        c.argument('output_start_time', help='Value is either an ISO-8601 formatted time stamp that indicates the '
                   'starting point of the output event stream, or null to indicate that the output event stream will '
                   'start whenever the streaming job is started. This property must have a value if outputStartMode is '
                   'set to CustomTime.')
        c.argument('out_of_order_policy', arg_type=get_enum_type(['Adjust', 'Drop']), help='Indicates the policy to '
                   'apply to events that arrive out of order in the input event stream.')
        c.argument('output_error_policy', arg_type=get_enum_type(['Stop', 'Drop']), help='Indicates the policy to '
                   'apply to events that arrive at the output and cannot be written to the external storage due to '
                   'being malformed (missing column values, column values of wrong type or size).')
        c.argument('order_max_delay', type=int, help='The maximum tolerable delay in seconds where out-of-order events '
                   'can be adjusted to be back in order.')
        c.argument('arrival_max_delay', type=int, help='The maximum tolerable delay in seconds where events arriving '
                   'late could be included.  Supported range is -1 to 1814399 (20.23:59:59 days) and -1 is used to '
                   'specify wait indefinitely. If the property is absent, it is interpreted to have a value of -1.')
        c.argument('data_locale', type=str, help='The data locale of the stream analytics job. Value should be the '
                   'name of a supported .NET Culture from the set https://msdn.microsoft.com/en-us/library/system.globa'
                   'lization.culturetypes(v=vs.110).aspx. Defaults to \'en-US\' if none specified.')
        c.argument('compatibility_level', arg_type=get_enum_type(['1.0', '1.2']), help='Controls certain runtime '
                   'behaviors of the streaming job.')
        c.argument('inputs', type=validate_file_or_dict, help='A list of one or more inputs to the streaming job. The '
                   'name property for each input is required when specifying this property in a PUT request. This '
                   'property cannot be modify via a PATCH operation. You must use the PATCH API available for the '
                   'individual input. Expected value: json-string/json-file/@json-file.')
        c.argument('transformation', action=AddTransformation, nargs='+', help='Indicates the query and the number of '
                   'streaming units to use for the streaming job. The name property of the transformation is required '
                   'when specifying this property in a PUT request. This property cannot be modify via a PATCH '
                   'operation. You must use the PATCH API available for the individual transformation.')
        c.argument('outputs', type=validate_file_or_dict, help='A list of one or more outputs for the streaming job. '
                   'The name property for each output is required when specifying this property in a PUT request. This '
                   'property cannot be modify via a PATCH operation. You must use the PATCH API available for the '
                   'individual output. Expected value: json-string/json-file/@json-file.')
        c.argument('functions', type=validate_file_or_dict, help='A list of one or more functions for the streaming '
                   'job. The name property for each function is required when specifying this property in a PUT '
                   'request. This property cannot be modify via a PATCH operation. You must use the PATCH API '
                   'available for the individual transformation. Expected value: json-string/json-file/@json-file.')
        c.argument('job_storage_account', action=AddJobStorageAccount, nargs='+', help='The properties that are '
                   'associated with an Azure Storage account with MSI')
        c.argument('content_storage_policy', arg_type=get_enum_type(['SystemAccount', 'JobStorageAccount']),
                   help='Valid values are JobStorageAccount and SystemAccount. If set to JobStorageAccount, this '
                   'requires the user to also specify jobStorageAccount property. .')
        c.argument('id_', options_list=['--id'], type=str, help='The resource id of cluster.', arg_group='Cluster')

    with self.argument_context('stream-analytics job update') as c:
        c.argument('if_match', type=str, help='The ETag of the streaming job. Omit this value to always overwrite the '
                   'current record set. Specify the last-seen ETag value to prevent accidentally overwriting '
                   'concurrent changes.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the streaming job.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('identity', action=AddIdentity, nargs='+', help='Describes the system-assigned managed identity '
                   'assigned to this job that can be used to authenticate with inputs and outputs.')
        c.argument('job_type', arg_type=get_enum_type(['Cloud', 'Edge']), help='Describes the type of the job. Valid '
                   'modes are `Cloud` and \'Edge\'.')
        c.argument('output_start_mode', arg_type=get_enum_type(['JobStartTime', 'CustomTime', 'LastOutputEventTime']),
                   help='This property should only be utilized when it is desired that the job be started immediately '
                   'upon creation. Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether '
                   'the starting point of the output event stream should start whenever the job is started, start at a '
                   'custom user time stamp specified via the outputStartTime property, or start from the last event '
                   'output time.')
        c.argument('output_start_time', help='Value is either an ISO-8601 formatted time stamp that indicates the '
                   'starting point of the output event stream, or null to indicate that the output event stream will '
                   'start whenever the streaming job is started. This property must have a value if outputStartMode is '
                   'set to CustomTime.')
        c.argument('out_of_order_policy', arg_type=get_enum_type(['Adjust', 'Drop']), help='Indicates the policy to '
                   'apply to events that arrive out of order in the input event stream.')
        c.argument('output_error_policy', arg_type=get_enum_type(['Stop', 'Drop']), help='Indicates the policy to '
                   'apply to events that arrive at the output and cannot be written to the external storage due to '
                   'being malformed (missing column values, column values of wrong type or size).')
        c.argument('order_max_delay', type=int, help='The maximum tolerable delay in seconds where out-of-order events '
                   'can be adjusted to be back in order.')
        c.argument('arrival_max_delay', type=int, help='The maximum tolerable delay in seconds where events arriving '
                   'late could be included.  Supported range is -1 to 1814399 (20.23:59:59 days) and -1 is used to '
                   'specify wait indefinitely. If the property is absent, it is interpreted to have a value of -1.')
        c.argument('data_locale', type=str, help='The data locale of the stream analytics job. Value should be the '
                   'name of a supported .NET Culture from the set https://msdn.microsoft.com/en-us/library/system.globa'
                   'lization.culturetypes(v=vs.110).aspx. Defaults to \'en-US\' if none specified.')
        c.argument('compatibility_level', arg_type=get_enum_type(['1.0', '1.2']), help='Controls certain runtime '
                   'behaviors of the streaming job.')
        c.argument('inputs', type=validate_file_or_dict, help='A list of one or more inputs to the streaming job. The '
                   'name property for each input is required when specifying this property in a PUT request. This '
                   'property cannot be modify via a PATCH operation. You must use the PATCH API available for the '
                   'individual input. Expected value: json-string/json-file/@json-file.')
        c.argument('transformation', action=AddTransformation, nargs='+', help='Indicates the query and the number of '
                   'streaming units to use for the streaming job. The name property of the transformation is required '
                   'when specifying this property in a PUT request. This property cannot be modify via a PATCH '
                   'operation. You must use the PATCH API available for the individual transformation.')
        c.argument('outputs', type=validate_file_or_dict, help='A list of one or more outputs for the streaming job. '
                   'The name property for each output is required when specifying this property in a PUT request. This '
                   'property cannot be modify via a PATCH operation. You must use the PATCH API available for the '
                   'individual output. Expected value: json-string/json-file/@json-file.')
        c.argument('functions', type=validate_file_or_dict, help='A list of one or more functions for the streaming '
                   'job. The name property for each function is required when specifying this property in a PUT '
                   'request. This property cannot be modify via a PATCH operation. You must use the PATCH API '
                   'available for the individual transformation. Expected value: json-string/json-file/@json-file.')
        c.argument('job_storage_account', action=AddJobStorageAccount, nargs='+', help='The properties that are '
                   'associated with an Azure Storage account with MSI')
        c.argument('content_storage_policy', arg_type=get_enum_type(['SystemAccount', 'JobStorageAccount']),
                   help='Valid values are JobStorageAccount and SystemAccount. If set to JobStorageAccount, this '
                   'requires the user to also specify jobStorageAccount property. .')
        c.argument('id_', options_list=['--id'], type=str, help='The resource id of cluster.', arg_group='Cluster')

    with self.argument_context('stream-analytics job delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the streaming job.')

    with self.argument_context('stream-analytics job scale') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the streaming job.')
        c.argument('streaming_units', type=int, help='Specifies the number of streaming units that the streaming job '
                   'will scale to.')

    with self.argument_context('stream-analytics job start') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the streaming job.')
        c.argument('output_start_mode', arg_type=get_enum_type(['JobStartTime', 'CustomTime', 'LastOutputEventTime']),
                   help='Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether the '
                   'starting point of the output event stream should start whenever the job is started, start at a '
                   'custom user time stamp specified via the outputStartTime property, or start from the last event '
                   'output time.')
        c.argument('output_start_time', help='Value is either an ISO-8601 formatted time stamp that indicates the '
                   'starting point of the output event stream, or null to indicate that the output event stream will '
                   'start whenever the streaming job is started. This property must have a value if outputStartMode is '
                   'set to CustomTime.')

    with self.argument_context('stream-analytics job stop') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the streaming job.')

    with self.argument_context('stream-analytics job wait') as c:
        c.argument('expand', type=str, help='The $expand OData query parameter. This is a comma-separated list of '
                   'additional streaming job properties to include in the response, beyond the default set returned '
                   'when this parameter is absent. The default set is all streaming job properties other than '
                   '\'inputs\', \'transformation\', \'outputs\', and \'functions\'.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n', '--job-name'], type=str, help='The name of the streaming job.')

    with self.argument_context('stream-analytics input list') as c:
        c.argument('select', type=str, help='The $select OData query parameter. This is a comma-separated list of '
                   'structural properties to include in the response, or "*" to include all properties. By default, '
                   'all properties are returned except diagnostics. Currently only accepts \'*\' as a valid value.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')

    with self.argument_context('stream-analytics input show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('input_name', options_list=['--name', '-n', '--input-name'], type=str, help='The name of the input.')

    with self.argument_context('stream-analytics input create') as c:
        c.argument('if_match', type=str, help='The ETag of the input. Omit this value to always overwrite the current '
                   'input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.')
        c.argument('if_none_match', type=str, help='Set to \'*\' to allow a new input to be created, but to prevent '
                   'updating an existing input. Other values will result in a 412 Pre-condition Failed response.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('input_name', options_list=['--name', '-n', '--input-name'], type=str, help='The name of the input.')
        c.argument('properties', type=validate_file_or_dict, help='The properties that are associated with an input. '
                   'Required on PUT (CreateOrReplace) requests. Expected value: json-string/json-file/@json-file.')

    with self.argument_context('stream-analytics input update') as c:
        c.argument('if_match', type=str, help='The ETag of the input. Omit this value to always overwrite the current '
                   'input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('input_name', options_list=['--name', '-n', '--input-name'], type=str, help='The name of the input.')
        c.argument('properties', type=validate_file_or_dict, help='The properties that are associated with an input. '
                   'Required on PUT (CreateOrReplace) requests. Expected value: json-string/json-file/@json-file.')

    with self.argument_context('stream-analytics input delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('input_name', options_list=['--name', '-n', '--input-name'], type=str, help='The name of the input.')

    with self.argument_context('stream-analytics input test') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('input_name', options_list=['--name', '-n', '--input-name'], type=str, help='The name of the input.')
        c.argument('properties', type=validate_file_or_dict, help='The properties that are associated with an input. '
                   'Required on PUT (CreateOrReplace) requests. Expected value: json-string/json-file/@json-file.')

    with self.argument_context('stream-analytics input wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('input_name', options_list=['--name', '-n', '--input-name'], type=str, help='The name of the input.')

    with self.argument_context('stream-analytics output list') as c:
        c.argument('select', type=str, help='The $select OData query parameter. This is a comma-separated list of '
                   'structural properties to include in the response, or "*" to include all properties. By default, '
                   'all properties are returned except diagnostics. Currently only accepts \'*\' as a valid value.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')

    with self.argument_context('stream-analytics output show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('output_name', options_list=['--name', '-n', '--output-name'], type=str, help='The name of the output.')

    with self.argument_context('stream-analytics output create') as c:
        c.argument('if_match', type=str, help='The ETag of the output. Omit this value to always overwrite the current '
                   'output. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.')
        c.argument('if_none_match', type=str, help='Set to \'*\' to allow a new output to be created, but to prevent '
                   'updating an existing output. Other values will result in a 412 Pre-condition Failed response.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('output_name', options_list=['--name', '-n', '--output-name'], type=str, help='The name of the output.')
        c.argument('datasource', type=validate_file_or_dict, help='Describes the data source that output will be '
                   'written to. Required on PUT (CreateOrReplace) requests. Expected value: '
                   'json-string/json-file/@json-file.')
        c.argument('time_window', type=str, help='The time frame for filtering Stream Analytics job outputs.')
        c.argument('size_window', type=float, help='The size window to constrain a Stream Analytics output to.')
        c.argument('serialization', type=validate_file_or_dict, help='Describes how data from an input is serialized '
                   'or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests. '
                   'Expected value: json-string/json-file/@json-file.')

    with self.argument_context('stream-analytics output update') as c:
        c.argument('if_match', type=str, help='The ETag of the output. Omit this value to always overwrite the current '
                   'output. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('output_name', options_list=['--name', '-n', '--output-name'], type=str, help='The name of the output.')
        c.argument('datasource', type=validate_file_or_dict, help='Describes the data source that output will be '
                   'written to. Required on PUT (CreateOrReplace) requests. Expected value: '
                   'json-string/json-file/@json-file.')
        c.argument('time_window', type=str, help='The time frame for filtering Stream Analytics job outputs.')
        c.argument('size_window', type=float, help='The size window to constrain a Stream Analytics output to.')
        c.argument('serialization', type=validate_file_or_dict, help='Describes how data from an input is serialized '
                   'or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests. '
                   'Expected value: json-string/json-file/@json-file.')

    with self.argument_context('stream-analytics output delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('output_name', options_list=['--name', '-n', '--output-name'], type=str, help='The name of the '
                   'output.')

    with self.argument_context('stream-analytics output test') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('output_name', options_list=['--name', '-n', '--output-name'], type=str, help='The name of the output.')
        c.argument('datasource', type=validate_file_or_dict, help='Describes the data source that output will be '
                   'written to. Required on PUT (CreateOrReplace) requests. Expected value: '
                   'json-string/json-file/@json-file.')
        c.argument('time_window', type=str, help='The time frame for filtering Stream Analytics job outputs.')
        c.argument('size_window', type=float, help='The size window to constrain a Stream Analytics output to.')
        c.argument('serialization', type=validate_file_or_dict, help='Describes how data from an input is serialized '
                   'or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests. '
                   'Expected value: json-string/json-file/@json-file.')

    with self.argument_context('stream-analytics output wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('output_name', options_list=['--name', '-n', '--output-name'], type=str, help='The name of the output.')

    with self.argument_context('stream-analytics transformation show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('transformation_name', options_list=['--name', '-n', '--transformation-name'], type=str, help='The '
                   'name of the transformation.')

    with self.argument_context('stream-analytics transformation create') as c:
        c.argument('if_match', type=str, help='The ETag of the transformation. Omit this value to always overwrite the '
                   'current transformation. Specify the last-seen ETag value to prevent accidentally overwriting '
                   'concurrent changes.')
        c.argument('if_none_match', type=str, help='Set to \'*\' to allow a new transformation to be created, but to '
                   'prevent updating an existing transformation. Other values will result in a 412 Pre-condition '
                   'Failed response.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('transformation_name', options_list=['--name', '-n', '--transformation-name'], type=str, help='The name of '
                   'the transformation.')
        c.argument('streaming_units', type=int, help='Specifies the number of streaming units that the streaming job '
                   'uses.')
        c.argument('valid_streaming_units', nargs='+', help='Specifies the valid streaming units a streaming job can '
                   'scale to.')
        c.argument('saql', type=str, help='Specifies the query that will be run in the streaming job. You can learn '
                   'more about the Stream Analytics Query Language (SAQL) here: https://msdn.microsoft.com/library/azur'
                   'e/dn834998 . Required on PUT (CreateOrReplace) requests.')

    with self.argument_context('stream-analytics transformation update') as c:
        c.argument('if_match', type=str, help='The ETag of the transformation. Omit this value to always overwrite the '
                   'current transformation. Specify the last-seen ETag value to prevent accidentally overwriting '
                   'concurrent changes.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('transformation_name', options_list=['--name', '-n', '--transformation-name'], type=str, help='The name of '
                   'the transformation.')
        c.argument('streaming_units', type=int, help='Specifies the number of streaming units that the streaming job '
                   'uses.')
        c.argument('valid_streaming_units', nargs='+', help='Specifies the valid streaming units a streaming job can '
                   'scale to.')
        c.argument('saql', type=str, help='Specifies the query that will be run in the streaming job. You can learn '
                   'more about the Stream Analytics Query Language (SAQL) here: https://msdn.microsoft.com/library/azur'
                   'e/dn834998 . Required on PUT (CreateOrReplace) requests.')

    with self.argument_context('stream-analytics function list') as c:
        c.argument('select', type=str, help='The $select OData query parameter. This is a comma-separated list of '
                   'structural properties to include in the response, or "*" to include all properties. By default, '
                   'all properties are returned except diagnostics. Currently only accepts \'*\' as a valid value.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')

    with self.argument_context('stream-analytics function show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('function_name', options_list=['--name', '-n', '--function-name'], type=str, help='The name of the '
                   'function.')

    with self.argument_context('stream-analytics function create') as c:
        c.argument('if_match', type=str, help='The ETag of the function. Omit this value to always overwrite the '
                   'current function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent '
                   'changes.')
        c.argument('if_none_match', type=str, help='Set to \'*\' to allow a new function to be created, but to prevent '
                   'updating an existing function. Other values will result in a 412 Pre-condition Failed response.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('function_name', options_list=['--name', '-n', '--function-name'], type=str,
                   help='The name of the function.')
        c.argument('properties', type=validate_file_or_dict, help='The properties that are associated with a function. '
                   'Expected value: json-string/json-file/@json-file.')

    with self.argument_context('stream-analytics function update') as c:
        c.argument('if_match', type=str, help='The ETag of the function. Omit this value to always overwrite the '
                   'current function. Specify the last-seen ETag value to prevent accidentally overwriting concurrent '
                   'changes.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('function_name', options_list=['--name', '-n', '--function-name'], type=str,
                   help='The name of the function.')
        c.argument('properties', type=validate_file_or_dict, help='The properties that are associated with a function. '
                   'Expected value: json-string/json-file/@json-file.')

    with self.argument_context('stream-analytics function delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('function_name', options_list=['--name', '-n', '--function-name'], type=str, help='The name of the '
                   'function.')

    with self.argument_context('stream-analytics function test') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('function_name', options_list=['--name', '-n', '--function-name'], type=str,
                   help='The name of the function.')
        c.argument('properties', type=validate_file_or_dict, help='The properties that are associated with a function. '
                   'Expected value: json-string/json-file/@json-file.')

    with self.argument_context('stream-analytics function wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', type=str, help='The name of the streaming job.')
        c.argument('function_name', options_list=['--name', '-n', '--function-name'], type=str, help='The name of the '
                   'function.')

    with self.argument_context('stream-analytics subscription inspect') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), id_part='name')
