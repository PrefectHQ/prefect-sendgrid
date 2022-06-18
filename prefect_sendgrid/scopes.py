"""
This is a module for interacting with SendGrid REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from typing import TYPE_CHECKING, Any, Dict

from prefect import task

from prefect_sendgrid.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_sendgrid import SendGridCredentials


@task
async def get_scopes(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint returns a list of all scopes that this user has access to.**
    API Keys are used to authenticate with [SendGrid's v3
    API](https://sendgrid.api-docs.io/v3.0/how-to-use-the-sendgrid-v3-api/api-
    authorization).  API Keys may be assigned certain permissions, or scopes,
    that limit which API endpoints they are able to access.  This endpoint
    returns all the scopes assigned to the key you use to authenticate with it.
    To retrieve the scopes assigned to another key, you can pass an API key ID
    to the 'Retrieve an existing API key' endpoint.  For a more detailed
    explanation of how you can use API Key permissions, please visit our [API
    Keys documentation](https://sendgrid.com/docs/ui/account-and-settings/api-
    keys/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/scopes?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/scopes?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/scopes"  # noqa

    responses = {}

    params = {
        "on_behalf_of": on_behalf_of,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_scopes_requests(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = 50,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all recent access requests.**
    The Response Header's `link` parameter will include pagination info.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            Optional field to limit the number of results returned.
        offset:
            Optional beginning point in the list to retrieve from.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/scopes/requests?&limit=%s&offset=%s](
    http://api.sendgrid.com/v3/scopes/requests?&limit=%s&offset=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/scopes/requests"  # noqa

    responses = {}

    params = {
        "limit": limit,
        "offset": offset,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result


@task
async def patch_scopes_requests_request_id_approve(
    request_id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to approve an access attempt.**  **Note:** Only
    teammate admins may approve another teammate’s access request.

    Args:
        request_id:
            Request id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/scopes/requests/{request_id}/approve?](
    http://api.sendgrid.com/v3/scopes/requests/{request_id}/approve?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/scopes/requests/{request_id}/approve"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result


@task
async def delete_scopes_requests_request_id(
    request_id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to deny an attempt to access your account.**
    **Note:** Only teammate admins may delete a teammate's access request.

    Args:
        request_id:
            Request id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/scopes/requests/{request_id}?](
    http://api.sendgrid.com/v3/scopes/requests/{request_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/scopes/requests/{request_id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result
