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
async def post_access_settings_whitelist(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to add one or more allowed IP addresses.**  To allow
    one or more IP addresses, pass them to this endpoint in an array. Once an IP
    address is added to your allow list, it will be assigned an `id` that can be
    used to remove the address. You can retrieve the ID associated with an IP
    using the 'Retrieve a list of currently allowed IPs' endpoint.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/access_settings/whitelist?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/access_settings/whitelist?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/access_settings/whitelist"  # noqa

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
async def get_access_settings_whitelist(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of IP addresses that are currently
    allowed to access your account.**  Each IP address returned to you will have
    `created_at` and `updated_at` dates. Each IP will also be associated with an
    `id` that can be used to remove the address from your allow list.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/access_settings/whitelist?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/access_settings/whitelist?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/access_settings/whitelist"  # noqa

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
async def delete_access_settings_whitelist(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove one or more IP addresses from your list of
    allowed addresses.**  To remove one or more IP addresses, pass this endpoint
    an array containing the ID(s) associated with the IP(s) you intend to
    remove. You can retrieve the IDs associated with your allowed IP addresses
    using the 'Retrieve a list of currently allowed IPs' endpoint.  It is
    possible to remove your own IP address, which will block access to your
    account. You will need to submit a [support
    ticket](https://sendgrid.com/docs/ui/account-and-settings/support/) if this
    happens. For this reason, it is important to double check that you are
    removing only the IPs you intend to remove when using this endpoint.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/access_settings/whitelist?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/access_settings/whitelist?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/access_settings/whitelist"  # noqa

    responses = {}

    params = {
        "body": body,
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
async def get_access_settings_activity(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = 20,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all of the IP addresses that
    recently attempted to access your account either through the User Interface
    or the API.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            Limits the number of IPs to return.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/access_settings/activity?&limit=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/access_settings/activity?&limit=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/access_settings/activity"  # noqa

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
async def get_access_settings_whitelist_rule_id(
    rule_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retreive a specific IP address that has been
    allowed to access your account.**  You must include the ID for the specific
    IP address you want to retrieve in your call. You can retrieve the IDs
    associated with your allowed IP addresses using the 'Retrieve a  list of
    currently allowed IPs' endpoint.

    Args:
        rule_id:
            Rule id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/access_settings/whitelist/{rule_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/access_settings/whitelist/{rule_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/access_settings/whitelist/{rule_id}"  # noqa
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
async def delete_access_settings_whitelist_rule_id(
    rule_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove a specific IP address from your list of
    allowed addresses.**  When removing a specific IP address from your list,
    you must include the ID in your call.  You can retrieve the IDs associated
    with your allowed IP addresses using the 'Retrieve a list of currently
    allowed IPs' endpoint.

    Args:
        rule_id:
            Rule id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/access_settings/whitelist/{rule_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/access_settings/whitelist/{rule_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/access_settings/whitelist/{rule_id}"  # noqa
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
