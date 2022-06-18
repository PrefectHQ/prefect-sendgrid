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
async def get_tracking_settings(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all tracking settings on your
    account.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/tracking_settings?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/tracking_settings?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/tracking_settings"  # noqa

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
async def get_tracking_settings_click(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current click tracking setting.**
    Click Tracking overrides all the links and URLs in your emails and points
    them to either SendGrid’s servers or the domain with which you branded your
    link. When a customer clicks a link, SendGrid tracks those
    [clicks](https://sendgrid.com/docs/glossary/clicks/).  Click tracking helps
    you understand how users are engaging with your communications. SendGrid can
    track up to 1000 links per email.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/tracking_settings/click?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/tracking_settings/click?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/tracking_settings/click"  # noqa

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
async def patch_tracking_settings_click(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to enable or disable your current click tracking
    setting.**  Click Tracking overrides all the links and URLs in your emails
    and points them to either SendGrid’s servers or the domain with which you
    branded your link. When a customer clicks a link, SendGrid tracks those
    [clicks](https://sendgrid.com/docs/glossary/clicks/).  Click tracking helps
    you understand how users are engaging with your communications. SendGrid can
    track up to 1000 links per email.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/tracking_settings/click?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/tracking_settings/click?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/tracking_settings/click"  # noqa

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
async def get_tracking_settings_google_analytics(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current setting for Google
    Analytics.**   Google Analytics helps you understand how users got to your
    site and what they're doing there. For more information about using Google
    Analytics, please refer to [Google’s URL
    Builder](https://support.google.com/analytics/answer/1033867?hl=en) and
    their article on ['Best Practices for Campaign
    Building'](https://support.google.com/analytics/answer/1037445).  We default
    the settings to Google’s recommendations. For more information, see [Google
    Analytics Demystified](https://sendgrid.com/docs/ui/analytics-and-
    reporting/google-analytics/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/tracking_settings/google_analytics?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/tracking_settings/google_analytics?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/tracking_settings/google_analytics"  # noqa

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
async def patch_tracking_settings_google_analytics(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current setting for Google
    Analytics.**  Google Analytics helps you understand how users got to your
    site and what they're doing there. For more information about using Google
    Analytics, please refer to [Google’s URL
    Builder](https://support.google.com/analytics/answer/1033867?hl=en) and
    their article on ['Best Practices for Campaign
    Building'](https://support.google.com/analytics/answer/1037445).  We default
    the settings to Google’s recommendations. For more information, see [Google
    Analytics Demystified](https://sendgrid.com/docs/ui/analytics-and-
    reporting/google-analytics/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/tracking_settings/google_analytics?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/tracking_settings/google_analytics?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/tracking_settings/google_analytics"  # noqa

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
async def get_tracking_settings_open(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current settings for open
    tracking.**  Open Tracking adds an invisible image at the end of the email
    which can track email opens.  If the email recipient has images enabled on
    their email client, a request to SendGrid’s server for the invisible image
    is executed and an open event is logged.  These events are logged in the
    Statistics portal, Email Activity interface, and are reported by the Event
    Webhook.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/tracking_settings/open?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/tracking_settings/open?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/tracking_settings/open"  # noqa

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
async def patch_tracking_settings_open(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current settings for open tracking.**
    Open Tracking adds an invisible image at the end of the email which can
    track email opens.  If the email recipient has images enabled on their email
    client, a request to SendGrid’s server for the invisible image is executed
    and an open event is logged.  These events are logged in the Statistics
    portal, Email Activity interface, and are reported by the Event Webhook.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/tracking_settings/open?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/tracking_settings/open?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/tracking_settings/open"  # noqa

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
async def get_tracking_settings_subscription(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current settings for subscription
    tracking.**  Subscription tracking adds links to the bottom of your emails
    that allows your recipients to subscribe to, or unsubscribe from, your
    emails.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/tracking_settings/subscription?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/tracking_settings/subscription?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/tracking_settings/subscription"  # noqa

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
async def patch_tracking_settings_subscription(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current settings for subscription
    tracking.**  Subscription tracking adds links to the bottom of your emails
    that allows your recipients to subscribe to, or unsubscribe from, your
    emails.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/tracking_settings/subscription?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/tracking_settings/subscription?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/tracking_settings/subscription"  # noqa

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
