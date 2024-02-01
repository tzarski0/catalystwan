# mypy: disable-error-code="empty-body"
from uuid import UUID

from vmngclient.endpoints import APIEndpoints, delete, get, post, put
from vmngclient.models.policy.definitions.mesh import MeshPolicy
from vmngclient.models.policy.policy_definition import (
    PolicyDefinitionEditResponse,
    PolicyDefinitionEndpoints,
    PolicyDefinitionId,
    PolicyDefinitionInfo,
    PolicyDefinitionPreview,
)
from vmngclient.typed_list import DataSequence


class MeshPolicyEditPayload(MeshPolicy, PolicyDefinitionId):
    pass


class MeshPolicyInfo(PolicyDefinitionId, PolicyDefinitionInfo):
    pass


class MeshPolicyGetResponse(MeshPolicy, PolicyDefinitionId, PolicyDefinitionInfo):
    pass


class ConfigurationPolicyMeshDefinition(APIEndpoints, PolicyDefinitionEndpoints):
    @post("/template/policy/definition/mesh")
    def create_policy_definition(self, payload: MeshPolicy) -> PolicyDefinitionId:
        ...

    @delete("/template/policy/definition/mesh/{id}")
    def delete_policy_definition(self, id: UUID) -> None:
        ...

    def edit_multiple_policy_definition(self):
        # PUT /template/policy/definition/mesh/multiple/{id}
        ...

    @put("/template/policy/definition/mesh/{id}")
    def edit_policy_definition(self, id: UUID, payload: MeshPolicyEditPayload) -> PolicyDefinitionEditResponse:
        ...

    @get("/template/policy/definition/mesh", "data")
    def get_definitions(self) -> DataSequence[MeshPolicyInfo]:
        ...

    @get("/template/policy/definition/mesh/{id}")
    def get_policy_definition(self, id: UUID) -> MeshPolicyGetResponse:
        ...

    @post("/template/policy/definition/mesh/preview")
    def preview_policy_definition(self, payload: MeshPolicy) -> PolicyDefinitionPreview:
        ...

    @get("/template/policy/definition/mesh/preview/{id}")
    def preview_policy_definition_by_id(self, id: UUID) -> PolicyDefinitionPreview:
        ...

    def save_policy_definition_in_bulk(self):
        # PUT /template/policy/definition/mesh/bulk
        ...