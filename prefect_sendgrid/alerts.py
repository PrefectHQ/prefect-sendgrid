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
async def post_alerts(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    authorization: str = None,
    on_behalf_of: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new alert.**  Alerts allow you to specify
    an email address to receive notifications regarding your email usage or
    statistics. There are two types of alerts that can be created with this
    endpoint:  * `usage_limit` allows you to set the threshold at which an alert
    will be sent. * `stats_notification` allows you to set how frequently you
    would like to receive email statistics reports. For example, 'daily',
    'weekly', or 'monthly'.  For more information about alerts, please see our
    [Alerts documentation](https://sendgrid.com/docs/ui/account-and-
    settings/alerts/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        authorization:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/alerts?&body=%s&authorization=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/alerts?&body=%s&authorization=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/alerts"  # noqa

    responses = {}

    params = {
        "body": body,
        "authorization": authorization,
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
async def get_alerts(
    sendgrid_credentials: "SendGridCredentials",
    authorization: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of your alerts.**  Alerts allow you
    to specify an email address to receive notifications regarding your email
    usage or statistics.  * Usage alerts allow you to set the threshold at which
    an alert will be sent. * Stats notifications allow you to set how frequently
    you would like to receive email statistics reports. For example, 'daily',
    'weekly', or 'monthly'.  For more information about alerts, please see our
    [Alerts documentation](https://sendgrid.com/docs/ui/account-and-
    settings/alerts/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        authorization:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/alerts?&authorization=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/alerts?&authorization=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/alerts"  # noqa

    responses = {}

    params = {
        "authorization": authorization,
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
async def get_alerts_alert_id(
    alert_id: str,
    sendgrid_credentials: "SendGridCredentials",
    authorization: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a specific alert.**  Alerts allow you to
    specify an email address to receive notifications regarding your email usage
    or statistics.  * Usage alerts allow you to set the threshold at which an
    alert will be sent. * Stats notifications allow you to set how frequently
    you would like to receive email statistics reports. For example, 'daily',
    'weekly', or 'monthly'.  For more information about alerts, please see our
    [Alerts documentation](https://sendgrid.com/docs/ui/account-and-
    settings/alerts/).

    Args:
        alert_id:
            Alert id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        authorization:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/alerts/{alert_id}?&authorization=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/alerts/{alert_id}?&authorization=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/alerts/{alert_id}"  # noqa
    responses = {}

    params = {
        "authorization": authorization,
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
async def delete_alerts_alert_id(
    alert_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete an alert.**  Alerts allow you to specify an
    email address to receive notifications regarding your email usage or
    statistics.  * Usage alerts allow you to set the threshold at which an alert
    will be sent. * Stats notifications allow you to set how frequently you
    would like to receive email statistics reports. For example, 'daily',
    'weekly', or 'monthly'.  For more information about alerts, please see our
    [Alerts documentation](https://sendgrid.com/docs/ui/account-and-
    settings/alerts/).

    Args:
        alert_id:
            Alert id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/alerts/{alert_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/alerts/{alert_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/alerts/{alert_id}"  # noqa
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
async def patch_alerts_alert_id(
    alert_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update an alert.**  Alerts allow you to specify an
    email address to receive notifications regarding your email usage or
    statistics.  * Usage alerts allow you to set the threshold at which an alert
    will be sent. * Stats notifications allow you to set how frequently you
    would like to receive email statistics reports. For example, 'daily',
    'weekly', or 'monthly'.  For more information about alerts, please see our
    [Alerts documentation](https://sendgrid.com/docs/ui/account-and-
    settings/alerts/).

    Args:
        alert_id:
            Alert id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/alerts/{alert_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/alerts/{alert_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/alerts/{alert_id}"  # noqa
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
