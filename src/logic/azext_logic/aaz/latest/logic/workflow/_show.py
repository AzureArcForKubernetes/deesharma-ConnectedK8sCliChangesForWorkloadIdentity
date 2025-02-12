# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "logic workflow show",
)
class Show(AAZCommand):
    """Get a workflow.

    :example: Show workflow
        az logic workflow show --resource-group rg --name workflow
    """

    _aaz_info = {
        "version": "2019-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.logic/workflows/{}", "2019-05-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The workflow name.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.WorkflowsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class WorkflowsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workflowName", self.ctx.args.name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.access_control = AAZObjectType(
                serialized_name="accessControl",
            )
            properties.access_endpoint = AAZStrType(
                serialized_name="accessEndpoint",
                flags={"read_only": True},
            )
            properties.changed_time = AAZStrType(
                serialized_name="changedTime",
                flags={"read_only": True},
            )
            properties.created_time = AAZStrType(
                serialized_name="createdTime",
                flags={"read_only": True},
            )
            properties.definition = AAZFreeFormDictType()
            properties.endpoints_configuration = AAZObjectType(
                serialized_name="endpointsConfiguration",
            )
            properties.integration_account = AAZObjectType(
                serialized_name="integrationAccount",
            )
            _ShowHelper._build_schema_resource_reference_read(properties.integration_account)
            properties.integration_service_environment = AAZObjectType(
                serialized_name="integrationServiceEnvironment",
            )
            _ShowHelper._build_schema_resource_reference_read(properties.integration_service_environment)
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.sku = AAZObjectType()
            properties.state = AAZStrType()
            properties.version = AAZStrType(
                flags={"read_only": True},
            )

            access_control = cls._schema_on_200.properties.access_control
            access_control.actions = AAZObjectType()
            _ShowHelper._build_schema_flow_access_control_configuration_policy_read(access_control.actions)
            access_control.contents = AAZObjectType()
            _ShowHelper._build_schema_flow_access_control_configuration_policy_read(access_control.contents)
            access_control.triggers = AAZObjectType()
            _ShowHelper._build_schema_flow_access_control_configuration_policy_read(access_control.triggers)
            access_control.workflow_management = AAZObjectType(
                serialized_name="workflowManagement",
            )
            _ShowHelper._build_schema_flow_access_control_configuration_policy_read(access_control.workflow_management)

            endpoints_configuration = cls._schema_on_200.properties.endpoints_configuration
            endpoints_configuration.connector = AAZObjectType()
            _ShowHelper._build_schema_flow_endpoints_read(endpoints_configuration.connector)
            endpoints_configuration.workflow = AAZObjectType()
            _ShowHelper._build_schema_flow_endpoints_read(endpoints_configuration.workflow)

            sku = cls._schema_on_200.properties.sku
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.plan = AAZObjectType()
            _ShowHelper._build_schema_resource_reference_read(sku.plan)

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_flow_access_control_configuration_policy_read = None

    @classmethod
    def _build_schema_flow_access_control_configuration_policy_read(cls, _schema):
        if cls._schema_flow_access_control_configuration_policy_read is not None:
            _schema.allowed_caller_ip_addresses = cls._schema_flow_access_control_configuration_policy_read.allowed_caller_ip_addresses
            _schema.open_authentication_policies = cls._schema_flow_access_control_configuration_policy_read.open_authentication_policies
            return

        cls._schema_flow_access_control_configuration_policy_read = _schema_flow_access_control_configuration_policy_read = AAZObjectType()

        flow_access_control_configuration_policy_read = _schema_flow_access_control_configuration_policy_read
        flow_access_control_configuration_policy_read.allowed_caller_ip_addresses = AAZListType(
            serialized_name="allowedCallerIpAddresses",
        )
        flow_access_control_configuration_policy_read.open_authentication_policies = AAZObjectType(
            serialized_name="openAuthenticationPolicies",
        )

        allowed_caller_ip_addresses = _schema_flow_access_control_configuration_policy_read.allowed_caller_ip_addresses
        allowed_caller_ip_addresses.Element = AAZObjectType()

        _element = _schema_flow_access_control_configuration_policy_read.allowed_caller_ip_addresses.Element
        _element.address_range = AAZStrType(
            serialized_name="addressRange",
        )

        open_authentication_policies = _schema_flow_access_control_configuration_policy_read.open_authentication_policies
        open_authentication_policies.policies = AAZDictType()

        policies = _schema_flow_access_control_configuration_policy_read.open_authentication_policies.policies
        policies.Element = AAZObjectType()

        _element = _schema_flow_access_control_configuration_policy_read.open_authentication_policies.policies.Element
        _element.claims = AAZListType()
        _element.type = AAZStrType()

        claims = _schema_flow_access_control_configuration_policy_read.open_authentication_policies.policies.Element.claims
        claims.Element = AAZObjectType()

        _element = _schema_flow_access_control_configuration_policy_read.open_authentication_policies.policies.Element.claims.Element
        _element.name = AAZStrType()
        _element.value = AAZStrType()

        _schema.allowed_caller_ip_addresses = cls._schema_flow_access_control_configuration_policy_read.allowed_caller_ip_addresses
        _schema.open_authentication_policies = cls._schema_flow_access_control_configuration_policy_read.open_authentication_policies

    _schema_flow_endpoints_read = None

    @classmethod
    def _build_schema_flow_endpoints_read(cls, _schema):
        if cls._schema_flow_endpoints_read is not None:
            _schema.access_endpoint_ip_addresses = cls._schema_flow_endpoints_read.access_endpoint_ip_addresses
            _schema.outgoing_ip_addresses = cls._schema_flow_endpoints_read.outgoing_ip_addresses
            return

        cls._schema_flow_endpoints_read = _schema_flow_endpoints_read = AAZObjectType()

        flow_endpoints_read = _schema_flow_endpoints_read
        flow_endpoints_read.access_endpoint_ip_addresses = AAZListType(
            serialized_name="accessEndpointIpAddresses",
        )
        flow_endpoints_read.outgoing_ip_addresses = AAZListType(
            serialized_name="outgoingIpAddresses",
        )

        access_endpoint_ip_addresses = _schema_flow_endpoints_read.access_endpoint_ip_addresses
        access_endpoint_ip_addresses.Element = AAZObjectType()
        cls._build_schema_ip_address_read(access_endpoint_ip_addresses.Element)

        outgoing_ip_addresses = _schema_flow_endpoints_read.outgoing_ip_addresses
        outgoing_ip_addresses.Element = AAZObjectType()
        cls._build_schema_ip_address_read(outgoing_ip_addresses.Element)

        _schema.access_endpoint_ip_addresses = cls._schema_flow_endpoints_read.access_endpoint_ip_addresses
        _schema.outgoing_ip_addresses = cls._schema_flow_endpoints_read.outgoing_ip_addresses

    _schema_ip_address_read = None

    @classmethod
    def _build_schema_ip_address_read(cls, _schema):
        if cls._schema_ip_address_read is not None:
            _schema.address = cls._schema_ip_address_read.address
            return

        cls._schema_ip_address_read = _schema_ip_address_read = AAZObjectType()

        ip_address_read = _schema_ip_address_read
        ip_address_read.address = AAZStrType()

        _schema.address = cls._schema_ip_address_read.address

    _schema_resource_reference_read = None

    @classmethod
    def _build_schema_resource_reference_read(cls, _schema):
        if cls._schema_resource_reference_read is not None:
            _schema.id = cls._schema_resource_reference_read.id
            _schema.name = cls._schema_resource_reference_read.name
            _schema.type = cls._schema_resource_reference_read.type
            return

        cls._schema_resource_reference_read = _schema_resource_reference_read = AAZObjectType()

        resource_reference_read = _schema_resource_reference_read
        resource_reference_read.id = AAZStrType()
        resource_reference_read.name = AAZStrType(
            flags={"read_only": True},
        )
        resource_reference_read.type = AAZStrType(
            flags={"read_only": True},
        )

        _schema.id = cls._schema_resource_reference_read.id
        _schema.name = cls._schema_resource_reference_read.name
        _schema.type = cls._schema_resource_reference_read.type


__all__ = ["Show"]
