from __future__ import annotations

from typing import Optional
import boto3


class AWSSession:
    """
    Wrapper around boto3.Session to centralize AWS access.
    """

    def __init__(
        self,
        profile: Optional[str] = None,
        region: Optional[str] = None,
    ) -> None:
        self._session = boto3.Session(
            profile_name=profile,
            region_name=region,
        )

    def client(self, service_name: str):
        return self._session.client(service_name)

    def resource(self, service_name: str):
        return self._session.resource(service_name)

    @property
    def region(self) -> str | None:
        return self._session.region_name
