# mypy: disable-error-code="empty-body"
from uuid import UUID

from vmngclient.endpoints import APIEndpoints, delete, get, post, put
from vmngclient.models.policy.definitions.access_control_list_ipv6 import AclIPv6Policy
from vmngclient.models.policy.policy_definition import (
    PolicyDefinitionEditResponse,
    PolicyDefinitionEndpoints,
    PolicyDefinitionId,
    PolicyDefinitionInfo,
    PolicyDefinitionPreview,
)
from vmngclient.typed_list import DataSequence


class AclIPv6PolicyEditPayload(AclIPv6Policy, PolicyDefinitionId):
    pass


class AclIPv6PolicyInfo(AclIPv6Policy, PolicyDefinitionId, PolicyDefinitionInfo):
    pass


class AclIPv6PolicyGetResponse(AclIPv6Policy, PolicyDefinitionId, PolicyDefinitionInfo):
    pass


class ConfigurationPolicyAclIPv6Definition(APIEndpoints, PolicyDefinitionEndpoints):
    @post("/template/policy/definition/aclv6")
    def create_policy_definition(self, payload: AclIPv6Policy) -> PolicyDefinitionId:
        ...

    @delete("/template/policy/definition/aclv6/{id}")
    def delete_policy_definition(self, id: UUID) -> None:
        ...

    def edit_multiple_policy_definition(self):
        # PUT /template/policy/definition/aclv6/multiple/{id}
        ...

    @put("/template/policy/definition/aclv6/{id}")
    def edit_policy_definition(self, id: UUID, payload: AclIPv6PolicyEditPayload) -> PolicyDefinitionEditResponse:
        ...

    @get("/template/policy/definition/aclv6", "data")
    def get_definitions(self) -> DataSequence[AclIPv6PolicyInfo]:
        ...

    @get("/template/policy/definition/aclv6/{id}")
    def get_policy_definition(self, id: UUID) -> AclIPv6PolicyGetResponse:
        ...

    @post("/template/policy/definition/aclv6/preview")
    def preview_policy_definition(self, payload: AclIPv6Policy) -> PolicyDefinitionPreview:
        ...

    @get("/template/policy/definition/aclv6/preview/{id}")
    def preview_policy_definition_by_id(self, id: UUID) -> PolicyDefinitionPreview:
        ...

    def save_policy_definition_in_bulk(self):
        # PUT /template/policy/definition/aclv6/bulk
        ...