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
async def post_api_keys(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new API Key for the user.**  To create
    your initial SendGrid API Key, you should [use the SendGrid
    App](https://app.sendgrid.com/settings/api_keys). Once you have created a
    first key with scopes to manage additional API keys, you can use this API
    for all other key management.  > There is a limit of 100 API Keys on your
    account.  A JSON request body containing a `name` property is required when
    making requests to this endpoint. If the number of maximum keys, 100, is
    reached, a `403` status will be returned.  Though the `name` field is
    required, it does not need to be unique. A unique API key ID will be
    generated for each key you create and returned in the response body.  It is
    not necessary to pass a `scopes` field to the API when creating a key, but
    you should be aware that omitting the `scopes` field from your request will
    create a key with 'Full Access' permissions by default.  See the [API Key
    Permissions List](https://sendgrid.api-docs.io/v3.0/how-to-use-the-
    sendgrid-v3-api/api-authorization) for all available scopes. An API key's
    scopes can be updated after creation using the 'Update API keys' endpoint.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/api_keys?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/api_keys?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/api_keys"  # noqa

    responses = {}

    params = {
        "body": body,
        "on_behalf_of": on_behalf_of,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_api_keys(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all API Keys that belong to the
    authenticated user.**  A successful response from this API will include all
    available API keys' names and IDs.  For security reasons, there is not a way
    to retrieve the key itself after it's created. If you lose your API key, you
    must create a new one. Only the 'Create API keys' endpoint will return a key
    to you and only at the time of creation.  An `api_key_id` can be used to
    update or delete the key, as well as retrieve the key's details, such as its
    scopes.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/api_keys?&limit=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/api_keys?&limit=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/api_keys"  # noqa

    responses = {}

    params = {
        "limit": limit,
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
async def get_api_keys_api_key_id(
    api_key_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a single API key using an `api_key_id`.**
    The endpoint will return a key's name, ID, and scopes. If the API Key ID
    does not, exist a `404` status will be returned.  See the [API Key
    Permissions List](https://sendgrid.api-docs.io/v3.0/how-to-use-the-
    sendgrid-v3-api/api-authorization) for all available scopes. An API key's
    scopes can be updated after creation using the 'Update API keys' endpoint.

    Args:
        api_key_id:
            Api key id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/api_keys/{api_key_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/api_keys/{api_key_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/api_keys/{api_key_id}"  # noqa
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
async def patch_api_keys_api_key_id(
    api_key_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update the name of an existing API Key.**  You
    must pass this endpoint a JSON request body with a `name` property, which
    will be used to rename the key associated with the `api_key_id` passed in
    the URL.

    Args:
        api_key_id:
            Api key id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/api_keys/{api_key_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/api_keys/{api_key_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/api_keys/{api_key_id}"  # noqa
    responses = {}

    params = {
        "body": body,
        "on_behalf_of": on_behalf_of,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.PATCH,
        params=params,
        responses=responses,
    )
    return result


@task
async def put_api_keys_api_key_id(
    api_key_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update the name and scopes of a given API key.**
    You must pass this endpoint a JSON request body with a `name` field and a
    `scopes` array containing at least one scope. The `name` and `scopes` fields
    will be used to update the key associated with the `api_key_id` in the
    request URL.  If you need to update a key's scopes only, pass the `name`
    field with the key's existing name; the `name` will not be modified. If you
    need to update a key's name only, use the 'Update API key name' endpoint.
    See the [API Key Permissions List](https://sendgrid.api-docs.io/v3.0/how-to-
    use-the-sendgrid-v3-api/api-authorization) for all available scopes.

    Args:
        api_key_id:
            Api key id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/api_keys/{api_key_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/api_keys/{api_key_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/api_keys/{api_key_id}"  # noqa
    responses = {}

    params = {
        "body": body,
        "on_behalf_of": on_behalf_of,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.PUT,
        params=params,
        responses=responses,
    )
    return result


@task
async def delete_api_keys_api_key_id(
    api_key_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to revoke an existing API Key using an `api_key_id`**
    Authentications using a revoked API Key will fail after after some small
    propogation delay. If the API Key ID does not exist, a `404` status will be
    returned.

    Args:
        api_key_id:
            Api key id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/api_keys/{api_key_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/api_keys/{api_key_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/api_keys/{api_key_id}"  # noqa
    responses = {}

    params = {
        "on_behalf_of": on_behalf_of,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
        responses=responses,
    )
    return result
