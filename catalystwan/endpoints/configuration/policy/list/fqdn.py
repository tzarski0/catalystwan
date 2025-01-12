# mypy: disable-error-code="empty-body"
from uuid import UUID

from catalystwan.endpoints import APIEndpoints, delete, get, post, put
from catalystwan.models.policy.lists import FQDNList
from catalystwan.models.policy.policy_list import (
    InfoTag,
    PolicyListEndpoints,
    PolicyListId,
    PolicyListInfo,
    PolicyListPreview,
)
from catalystwan.typed_list import DataSequence


class FQDNListEditPayload(FQDNList, PolicyListId):
    pass


class FQDNListInfo(FQDNList, PolicyListInfo):
    pass


class ConfigurationPolicyFQDNList(APIEndpoints, PolicyListEndpoints):
    @post("/template/policy/list/fqdn")
    def create_policy_list(self, payload: FQDNList) -> PolicyListId:
        ...

    @delete("/template/policy/list/fqdn/{id}")
    def delete_policy_list(self, id: UUID) -> None:
        ...

    @delete("/template/policy/list/fqdn")
    def delete_policy_lists_with_info_tag(self, params: InfoTag) -> None:
        ...

    @put("/template/policy/list/fqdn/{id}")
    def edit_policy_list(self, id: UUID, payload: FQDNListEditPayload) -> None:
        ...

    @get("/template/policy/list/fqdn/{id}")
    def get_lists_by_id(self, id: UUID) -> FQDNListInfo:
        ...

    @get("/template/policy/list/fqdn", "data")
    def get_policy_lists(self) -> DataSequence[FQDNListInfo]:
        ...

    @get("/template/policy/list/fqdn/filtered", "data")
    def get_policy_lists_with_info_tag(self, params: InfoTag) -> DataSequence[FQDNListInfo]:
        ...

    @post("/template/policy/list/fqdn/preview")
    def preview_policy_list(self, payload: FQDNList) -> PolicyListPreview:
        ...

    @get("/template/policy/list/fqdn/preview/{id}")
    def preview_policy_list_by_id(self, id: UUID) -> PolicyListPreview:
        ...
