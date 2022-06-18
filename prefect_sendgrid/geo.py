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
async def get_geo_stats(
    start_date: str,
    sendgrid_credentials: "SendGridCredentials",
    country: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
    limit: int = None,
    offset: int = None,
    aggregated_by: str = None,
    end_date: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your email statistics segmented by
    country and state/province.**  **We only store up to 7 days of email
    activity in our database.** By default, 500 items will be returned per
    request via the Advanced Stats API endpoints.  Advanced Stats provide a more
    in-depth view of your email statistics and the actions taken by your
    recipients. You can segment these statistics by geographic location, device
    type, client type, browser, and mailbox provider. For more information about
    statistics, please see our [User
    Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

    Args:
        start_date:
            The starting date of the statistics to retrieve. Must follow format
            YYYY-MM-DD.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        country:
            The country you would like to see statistics for. Currently only
            supported for US and CA.
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
    [http://api.sendgrid.com/v3/geo/stats?&country=%s&on_behalf_of=%s&limit=%s&offset=%s&aggregated_by=%s&start_date=%s&end_date=%s](
    http://api.sendgrid.com/v3/geo/stats?&country=%s&on_behalf_of=%s&limit=%s&offset=%s&aggregated_by=%s&start_date=%s&end_date=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/geo/stats"  # noqa

    responses = {}

    params = {
        "country": country,
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
