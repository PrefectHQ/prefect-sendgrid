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
async def patch_partner_settings_new_relic(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update or change your New Relic partner
    settings.**  Our partner settings allow you to integrate your SendGrid
    account with our partners to increase your SendGrid experience and
    functionality. For more information about our partners, and how you can
    begin integrating with them, please visit our [Partners
    documentation](https://sendgrid.com/docs/ui/account-and-settings/partners/).
    By integrating with New Relic, you can send your SendGrid email statistics
    to your New Relic Dashboard. If you enable this setting, your stats will be
    sent to New Relic every 5 minutes. You will need your New Relic License Key
    to enable this setting. For more information, please see our [SendGrid for
    New Relic documentation](https://sendgrid.com/docs/ui/analytics-and-
    reporting/tracking-stats-using-new-relic/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/partner_settings/new_relic?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/partner_settings/new_relic?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/partner_settings/new_relic"  # noqa

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
async def get_partner_settings_new_relic(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current New Relic partner
    settings.**  Our partner settings allow you to integrate your SendGrid
    account with our partners to increase your SendGrid experience and
    functionality. For more information about our partners, and how you can
    begin integrating with them, please visit our [Partners
    documentation](https://sendgrid.com/docs/ui/account-and-settings/partners/).
    By integrating with New Relic, you can send your SendGrid email statistics
    to your New Relic Dashboard. If you enable this setting, your stats will be
    sent to New Relic every 5 minutes. You will need your New Relic License Key
    to enable this setting. For more information, please see our [SendGrid for
    New Relic documentation](https://sendgrid.com/docs/ui/analytics-and-
    reporting/tracking-stats-using-new-relic/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/partner_settings/new_relic?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/partner_settings/new_relic?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/partner_settings/new_relic"  # noqa

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
async def get_partner_settings(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = None,
    offset: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all partner settings that you
    can enable.**  Our partner settings allow you to integrate your SendGrid
    account with our partners to increase your SendGrid experience and
    functionality. For more information about our partners, and how you can
    begin integrating with them, please visit our [Partners
    documentation](https://sendgrid.com/docs/ui/account-and-settings/partners/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            The number of settings to return per page.
        offset:
            The paging offset.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/partner_settings?&limit=%s&offset=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/partner_settings?&limit=%s&offset=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/partner_settings"  # noqa

    responses = {}

    params = {
        "limit": limit,
        "offset": offset,
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
