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
async def get_categories(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = 50,
    category: str = None,
    offset: int = 0,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all of your categories.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            The number of categories to display per page.
        category:
            Allows you to perform a prefix search on this particular category.
        offset:
            The point in the list that you would like to begin displaying results.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/categories?&limit=%s&category=%s&offset=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/categories?&limit=%s&category=%s&offset=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/categories"  # noqa

    responses = {}

    params = {
        "limit": limit,
        "category": category,
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


@task
async def get_categories_stats_sums(
    start_date: str,
    sendgrid_credentials: "SendGridCredentials",
    sort_by_metric: str = "delivered",
    sort_by_direction: str = "desc",
    end_date: str = None,
    limit: int = 5,
    offset: int = 0,
    aggregated_by: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the total sum of each email statistic for
    every category over the given date range.**  If you do not define any query
    parameters, this endpoint will return a sum for each category in groups of
    10.

    Args:
        start_date:
            The starting date of the statistics to retrieve. Must follow format
            YYYY-MM-DD.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        sort_by_metric:
            The metric that you want to sort by.  Must be a single metric.
        sort_by_direction:
            The direction you want to sort.
        end_date:
            The end date of the statistics to retrieve. Defaults to today. Must
            follow format YYYY-MM-DD.
        limit:
            Limits the number of results returned.
        offset:
            The point in the list to begin retrieving results.
        aggregated_by:
            How to group the statistics. Must be either 'day', 'week', or 'month'.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/categories/stats/sums?&sort_by_metric=%s&sort_by_direction=%s&start_date=%s&end_date=%s&limit=%s&offset=%s&aggregated_by=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/categories/stats/sums?&sort_by_metric=%s&sort_by_direction=%s&start_date=%s&end_date=%s&limit=%s&offset=%s&aggregated_by=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/categories/stats/sums"  # noqa

    responses = {}

    params = {
        "sort_by_metric": sort_by_metric,
        "sort_by_direction": sort_by_direction,
        "start_date": start_date,
        "end_date": end_date,
        "limit": limit,
        "offset": offset,
        "aggregated_by": aggregated_by,
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
async def get_categories_stats(
    start_date: str,
    categories: str,
    sendgrid_credentials: "SendGridCredentials",
    end_date: str = None,
    limit: int = 500,
    offset: int = None,
    aggregated_by: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of your email statistics for each of
    your categories.**  If you do not define any query parameters, this endpoint
    will return a sum for each category in groups of 10.

    Args:
        start_date:
            The starting date of the statistics to retrieve. Must follow format
            YYYY-MM-DD.
        categories:
            The individual categories that you want to retrieve statistics for. You
            may include up to 10 different categories.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        end_date:
            The end date of the statistics to retrieve. Defaults to today. Must
            follow format YYYY-MM-DD.
        limit:
            The number of results to include.
        offset:
            The number of results to skip.
        aggregated_by:
            How to group the statistics. Must be either 'day', 'week', or 'month'.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/categories/stats?&start_date=%s&end_date=%s&categories=%s&limit=%s&offset=%s&aggregated_by=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/categories/stats?&start_date=%s&end_date=%s&categories=%s&limit=%s&offset=%s&aggregated_by=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/categories/stats"  # noqa

    responses = {}

    params = {
        "start_date": start_date,
        "end_date": end_date,
        "categories": categories,
        "limit": limit,
        "offset": offset,
        "aggregated_by": aggregated_by,
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
