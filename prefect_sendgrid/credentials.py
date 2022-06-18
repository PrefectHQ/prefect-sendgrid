"""Credential classes used to perform authenticated interactions with SendGrid"""

from dataclasses import dataclass

from httpx import AsyncClient


@dataclass
class SendGridCredentials:
    """
    Dataclass used to manage SendGrid authentication.

    Args:
        token: the token to authenticate into SendGrid.
    """

    token: str = None

    def get_client(self) -> AsyncClient:
        """
        Gets an authenticated SendGrid REST AsyncClient.

        Returns:
            An authenticated SendGrid REST AsyncClient

        Example:
            Gets an authenticated SendGrid REST AsyncClient.
            ```python
            from prefect import flow
            from prefect_sendgrid import SendGridCredentials

            @flow
            def example_get_client_flow():
                token = "consumer_key"
                sendgrid_credentials = SendGridCredentials(token)
                endpoint = sendgrid_credentials.get_client()
                return endpoint

            example_get_client_flow()
            ```
        """
        if self.token is not None:
            headers = {"Authorization": f"Bearer {self.token}"}
        else:
            headers = None
        client = AsyncClient(headers=headers)
        return client
