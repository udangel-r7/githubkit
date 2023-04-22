"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Missing, exclude_unset

from .models import (
    BasicError,
    ValidationError,
    RepositoryAdvisory,
    RepositoryAdvisoryCreate,
    RepositoryAdvisoryUpdate,
    PrivateVulnerabilityReportCreate,
)
from .types import (
    RepositoryAdvisoryCreateType,
    RepositoryAdvisoryUpdateType,
    PrivateVulnerabilityReportCreateType,
    RepositoryAdvisoryCreatePropCreditsItemsType,
    RepositoryAdvisoryUpdatePropCreditsItemsType,
    RepositoryAdvisoryCreatePropVulnerabilitiesItemsType,
    RepositoryAdvisoryUpdatePropVulnerabilitiesItemsType,
    PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsType,
)

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class SecurityAdvisoriesClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def list_repository_advisories(
        self,
        owner: str,
        repo: str,
        direction: Missing[Literal["asc", "desc"]] = "desc",
        sort: Missing[Literal["created", "updated", "published"]] = "created",
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        per_page: Missing[int] = 30,
        state: Missing[Literal["triage", "draft", "published", "closed"]] = UNSET,
    ) -> "Response[List[RepositoryAdvisory]]":
        url = f"/repos/{owner}/{repo}/security-advisories"

        params = {
            "direction": direction,
            "sort": sort,
            "before": before,
            "after": after,
            "per_page": per_page,
            "state": state,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[RepositoryAdvisory],
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    async def async_list_repository_advisories(
        self,
        owner: str,
        repo: str,
        direction: Missing[Literal["asc", "desc"]] = "desc",
        sort: Missing[Literal["created", "updated", "published"]] = "created",
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        per_page: Missing[int] = 30,
        state: Missing[Literal["triage", "draft", "published", "closed"]] = UNSET,
    ) -> "Response[List[RepositoryAdvisory]]":
        url = f"/repos/{owner}/{repo}/security-advisories"

        params = {
            "direction": direction,
            "sort": sort,
            "before": before,
            "after": after,
            "per_page": per_page,
            "state": state,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[RepositoryAdvisory],
            error_models={
                "400": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def create_repository_advisory(
        self, owner: str, repo: str, *, data: RepositoryAdvisoryCreateType
    ) -> "Response[RepositoryAdvisory]":
        ...

    @overload
    def create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        summary: str,
        description: str,
        cve_id: Missing[Union[str, None]] = UNSET,
        vulnerabilities: List[RepositoryAdvisoryCreatePropVulnerabilitiesItemsType],
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        credits_: Missing[
            Union[List[RepositoryAdvisoryCreatePropCreditsItemsType], None]
        ] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
    ) -> "Response[RepositoryAdvisory]":
        ...

    def create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[RepositoryAdvisoryCreateType] = UNSET,
        **kwargs,
    ) -> "Response[RepositoryAdvisory]":
        url = f"/repos/{owner}/{repo}/security-advisories"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(RepositoryAdvisoryCreate, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_repository_advisory(
        self, owner: str, repo: str, *, data: RepositoryAdvisoryCreateType
    ) -> "Response[RepositoryAdvisory]":
        ...

    @overload
    async def async_create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        summary: str,
        description: str,
        cve_id: Missing[Union[str, None]] = UNSET,
        vulnerabilities: List[RepositoryAdvisoryCreatePropVulnerabilitiesItemsType],
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        credits_: Missing[
            Union[List[RepositoryAdvisoryCreatePropCreditsItemsType], None]
        ] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
    ) -> "Response[RepositoryAdvisory]":
        ...

    async def async_create_repository_advisory(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[RepositoryAdvisoryCreateType] = UNSET,
        **kwargs,
    ) -> "Response[RepositoryAdvisory]":
        url = f"/repos/{owner}/{repo}/security-advisories"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(RepositoryAdvisoryCreate, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    def create_private_vulnerability_report(
        self, owner: str, repo: str, *, data: PrivateVulnerabilityReportCreateType
    ) -> "Response[RepositoryAdvisory]":
        ...

    @overload
    def create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        summary: str,
        description: str,
        vulnerabilities: Missing[
            Union[
                List[PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsType], None
            ]
        ] = UNSET,
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
    ) -> "Response[RepositoryAdvisory]":
        ...

    def create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[PrivateVulnerabilityReportCreateType] = UNSET,
        **kwargs,
    ) -> "Response[RepositoryAdvisory]":
        url = f"/repos/{owner}/{repo}/security-advisories/reports"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(PrivateVulnerabilityReportCreate, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_private_vulnerability_report(
        self, owner: str, repo: str, *, data: PrivateVulnerabilityReportCreateType
    ) -> "Response[RepositoryAdvisory]":
        ...

    @overload
    async def async_create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        summary: str,
        description: str,
        vulnerabilities: Missing[
            Union[
                List[PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsType], None
            ]
        ] = UNSET,
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
    ) -> "Response[RepositoryAdvisory]":
        ...

    async def async_create_private_vulnerability_report(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[PrivateVulnerabilityReportCreateType] = UNSET,
        **kwargs,
    ) -> "Response[RepositoryAdvisory]":
        url = f"/repos/{owner}/{repo}/security-advisories/reports"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(PrivateVulnerabilityReportCreate, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    def get_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
    ) -> "Response[RepositoryAdvisory]":
        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
    ) -> "Response[RepositoryAdvisory]":
        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def update_repository_advisory(
        self, owner: str, repo: str, ghsa_id: str, *, data: RepositoryAdvisoryUpdateType
    ) -> "Response[RepositoryAdvisory]":
        ...

    @overload
    def update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        data: Literal[UNSET] = UNSET,
        summary: Missing[str] = UNSET,
        description: Missing[str] = UNSET,
        cve_id: Missing[Union[str, None]] = UNSET,
        vulnerabilities: Missing[
            List[RepositoryAdvisoryUpdatePropVulnerabilitiesItemsType]
        ] = UNSET,
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        credits_: Missing[
            Union[List[RepositoryAdvisoryUpdatePropCreditsItemsType], None]
        ] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
        state: Missing[Literal["published", "closed", "draft"]] = UNSET,
    ) -> "Response[RepositoryAdvisory]":
        ...

    def update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        data: Missing[RepositoryAdvisoryUpdateType] = UNSET,
        **kwargs,
    ) -> "Response[RepositoryAdvisory]":
        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(RepositoryAdvisoryUpdate, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_update_repository_advisory(
        self, owner: str, repo: str, ghsa_id: str, *, data: RepositoryAdvisoryUpdateType
    ) -> "Response[RepositoryAdvisory]":
        ...

    @overload
    async def async_update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        data: Literal[UNSET] = UNSET,
        summary: Missing[str] = UNSET,
        description: Missing[str] = UNSET,
        cve_id: Missing[Union[str, None]] = UNSET,
        vulnerabilities: Missing[
            List[RepositoryAdvisoryUpdatePropVulnerabilitiesItemsType]
        ] = UNSET,
        cwe_ids: Missing[Union[List[str], None]] = UNSET,
        credits_: Missing[
            Union[List[RepositoryAdvisoryUpdatePropCreditsItemsType], None]
        ] = UNSET,
        severity: Missing[
            Union[None, Literal["critical", "high", "medium", "low"]]
        ] = UNSET,
        cvss_vector_string: Missing[Union[str, None]] = UNSET,
        state: Missing[Literal["published", "closed", "draft"]] = UNSET,
    ) -> "Response[RepositoryAdvisory]":
        ...

    async def async_update_repository_advisory(
        self,
        owner: str,
        repo: str,
        ghsa_id: str,
        *,
        data: Missing[RepositoryAdvisoryUpdateType] = UNSET,
        **kwargs,
    ) -> "Response[RepositoryAdvisory]":
        url = f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(RepositoryAdvisoryUpdate, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=RepositoryAdvisory,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "422": ValidationError,
            },
        )
