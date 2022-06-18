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
async def get_stats(
    start_date: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
    limit: int = None,
    offset: int = None,
    aggregated_by: str = None,
    end_date: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of your global email statistics
    between a given date range.**  Parent accounts will see aggregated stats for
    their account and all subuser accounts. Subuser accounts will only see their
    own stats.

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
    [http://api.sendgrid.com/v3/stats?&on_behalf_of=%s&limit=%s&offset=%s&aggregated_by=%s&start_date=%s&end_date=%s](
    http://api.sendgrid.com/v3/stats?&on_behalf_of=%s&limit=%s&offset=%s&aggregated_by=%s&start_date=%s&end_date=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/stats"  # noqa

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
