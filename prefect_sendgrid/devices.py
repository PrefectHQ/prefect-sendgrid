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
async def get_devices_stats(
    start_date: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
    limit: int = None,
    offset: int = None,
    aggregated_by: str = None,
    end_date: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your email statistics segmented by the
    device type.**  **We only store up to 7 days of email activity in our
    database.** By default, 500 items will be returned per request via the
    Advanced Stats API endpoints.
    Available Device Types | **Device** | **Description** | **Example** |
    |---|---|---| | Desktop | Email software on desktop computer. | I.E.,
    Outlook, Sparrow, or Apple Mail. | | Webmail |     A web-based email client.
    | I.E., Yahoo, Google, AOL, or Outlook.com. | | Phone | A smart phone. |
    iPhone, Android, Blackberry, etc. | Tablet | A tablet computer. | iPad,
    android based tablet, etc. | | Other | An unrecognized device. |  Advanced
    Stats provide a more in-depth view of your email statistics and the actions
    taken by your recipients. You can segment these statistics by geographic
    location, device type, client type, browser, and mailbox provider. For more
    information about statistics, please see our [Statistics
    Overview](https://sendgrid.com/docs/ui/analytics-and-reporting/stats-
    overview/).

    Args:
        start_date:
            The starting date of the statistics to retrieve. Must follow format
            YYYY-MM-DD.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:

        limit:
            The number of results to return.
        offset:
            The point in the list to begin retrieving results.
        aggregated_by:
            How to group the statistics. Must be either 'day', 'week', or 'month'.
        end_date:
            The end date of the statistics to retrieve. Defaults to today. Must
            follow format YYYY-MM-DD.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/devices/stats?&on_behalf_of=%s&limit=%s&offset=%s&aggregated_by=%s&start_date=%s&end_date=%s](
    http://api.sendgrid.com/v3/devices/stats?&on_behalf_of=%s&limit=%s&offset=%s&aggregated_by=%s&start_date=%s&end_date=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/devices/stats"  # noqa

    responses = {}

    params = {
        "on_behalf_of": on_behalf_of,
        "limit": limit,
        "offset": offset,
        "aggregated_by": aggregated_by,
        "start_date": start_date,
        "end_date": end_date,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
