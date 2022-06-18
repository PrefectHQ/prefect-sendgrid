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
async def post_asm_suppressions_global(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to add one or more email addresses to the global
    suppressions group.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/suppressions/global?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/suppressions/global?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/asm/suppressions/global"  # noqa

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
async def get_asm_suppressions_global_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a global suppression. You can also use
    this endpoint to confirm if an email address is already globally
    suppresed.**  If the email address you include in the URL path parameter
    `{email}` is already globally suppressed, the response will include that
    email address. If the address you enter for `{email}` is not globally
    suppressed, an empty JSON object `{}` will be returned.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/suppressions/global/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/suppressions/global/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/asm/suppressions/global/{email}"  # noqa
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
async def delete_asm_suppressions_global_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove an email address from the global
    suppressions group.**  Deleting a suppression group will remove the
    suppression, meaning email will once again be sent to the previously
    suppressed addresses. This should be avoided unless a recipient indicates
    they wish to receive email from you again. You can use our [bypass
    filters](https://sendgrid.com/docs/ui/sending-email/index-suppressions/
    bypass-suppressions) to deliver messages to otherwise suppressed addresses
    when exceptions are required.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/suppressions/global/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/suppressions/global/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/asm/suppressions/global/{email}"  # noqa
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


@task
async def post_asm_groups(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new suppression group.**  To add an email
    address to the suppression group, [create a
    Suppression](https://sendgrid.api-docs.io/v3.0/suppressions-
    suppressions/add-suppressions-to-a-suppression-group).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/groups?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/groups?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/asm/groups"  # noqa

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
async def get_asm_groups(
    sendgrid_credentials: "SendGridCredentials",
    id: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all suppression groups created
    by this user.**  This endpoint can also return information for multiple
    group IDs that you include in your request. To add a group ID to your
    request, simply append `?id=123456&id=123456`, with the appropriate group
    IDs.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        id:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/groups?&id=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/groups?&id=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/asm/groups"  # noqa

    responses = {}

    params = {
        "id": id,
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
async def get_asm_groups_group_id(
    group_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a single suppression group.**.

    Args:
        group_id:
            Group id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/groups/{group_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/groups/{group_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/asm/groups/{group_id}"  # noqa
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
async def patch_asm_groups_group_id(
    group_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update or change a suppression group.**.

    Args:
        group_id:
            Group id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/groups/{group_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/groups/{group_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/asm/groups/{group_id}"  # noqa
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
async def delete_asm_groups_group_id(
    group_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a suppression group.**  If a recipient uses
    the 'one-click unsubscribe' option on an email associated with a deleted
    group, that recipient will be added to the global suppression list.
    Deleting a suppression group will remove the suppression, meaning email will
    once again be sent to the previously suppressed addresses. This should be
    avoided unless a recipient indicates they wish to receive email from you
    again. You can use our [bypass
    filters](https://sendgrid.com/docs/ui/sending-email/index-suppressions/
    bypass-suppressions) to deliver messages to otherwise suppressed addresses
    when exceptions are required.

    Args:
        group_id:
            Group id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/groups/{group_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/groups/{group_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/asm/groups/{group_id}"  # noqa
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


@task
async def post_asm_groups_group_id_suppressions(
    group_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to add email addresses to an unsubscribe group.**  If
    you attempt to add suppressions to a group that has been deleted or does not
    exist, the suppressions will be added to the global suppressions list.

    Args:
        group_id:
            Group id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions"  # noqa
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
async def get_asm_groups_group_id_suppressions(
    group_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all suppressed email addresses belonging
    to the given group.**.

    Args:
        group_id:
            Group id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions"  # noqa
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
async def post_asm_groups_group_id_suppressions_search(
    group_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to search a suppression group for multiple
    suppressions.**  When given a list of email addresses and a group ID, this
    endpoint will only return the email addresses that have been unsubscribed
    from the given group.

    Args:
        group_id:
            Group id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions/search?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions/search?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = (
        f"http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions/search"  # noqa
    )
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
async def get_asm_suppressions(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all suppressions.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/suppressions?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/suppressions?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/asm/suppressions"  # noqa

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
async def get_asm_suppressions_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint returns a list of all groups from which the given email address
    has been unsubscribed.**.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/suppressions/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/suppressions/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/asm/suppressions/{email}"  # noqa
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
async def delete_asm_groups_group_id_suppressions_email(
    group_id: str,
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove a suppressed email address from the given
    suppression group.**  Removing an address will remove the suppression,
    meaning email will once again be sent to the previously suppressed
    addresses. This should be avoided unless a recipient indicates they wish to
    receive email from you again. You can use our [bypass
    filters](https://sendgrid.com/docs/ui/sending-email/index-suppressions/
    bypass-suppressions) to deliver messages to otherwise suppressed addresses
    when exceptions are required.

    Args:
        group_id:
            Group id used in formatting the endpoint URL.
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = (
        f"http://api.sendgrid.com/v3/asm/groups/{group_id}/suppressions/{email}"  # noqa
    )
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
