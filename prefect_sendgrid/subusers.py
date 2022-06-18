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
async def get_subusers(
    sendgrid_credentials: "SendGridCredentials",
    username: str = None,
    limit: int = None,
    offset: int = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all of your subusers.**  You
    can choose to retrieve specific subusers as well as limit the results that
    come back from the API.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        username:
            The username of this subuser.
        limit:
            The number of results you would like to get in each request.
        offset:
            The number of subusers to skip.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers?&username=%s&limit=%s&offset=%s](
    http://api.sendgrid.com/v3/subusers?&username=%s&limit=%s&offset=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 401 | Unexpected error in API call. See HTTP response body for details. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/subusers"  # noqa

    responses = {
        401: "Unexpected error in API call. See HTTP response body for details.",  # noqa
    }

    params = {
        "username": username,
        "limit": limit,
        "offset": offset,
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
async def post_subusers(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new subuser.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers?&body=%s](
    http://api.sendgrid.com/v3/subusers?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/subusers"  # noqa

    responses = {}

    params = {
        "body": body,
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
async def patch_subusers_subuser_name(
    subuser_name: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to enable or disable a subuser.**.

    Args:
        subuser_name:
            Subuser name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/{subuser_name}?&body=%s](
    http://api.sendgrid.com/v3/subusers/{subuser_name}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/subusers/{subuser_name}"  # noqa
    responses = {}

    params = {
        "body": body,
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
async def delete_subusers_subuser_name(
    subuser_name: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a subuser.**  This is a permanent action.
    Once deleted, a subuser cannot be retrieved.

    Args:
        subuser_name:
            Subuser name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/{subuser_name}?](
    http://api.sendgrid.com/v3/subusers/{subuser_name}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/subusers/{subuser_name}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_subusers_reputations(
    sendgrid_credentials: "SendGridCredentials",
    usernames: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to request the reputations for your subusers.**
    Subuser sender reputations give a good idea how well a sender is doing with
    regards to how recipients and recipient servers react to the mail that is
    being received. When a bounce, spam report, or other negative action happens
    on a sent email, it will affect your sender rating.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        usernames:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/reputations?&usernames=%s](
    http://api.sendgrid.com/v3/subusers/reputations?&usernames=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/subusers/reputations"  # noqa

    responses = {}

    params = {
        "usernames": usernames,
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
async def put_subusers_subuser_name_ips(
    subuser_name: str,
    sendgrid_credentials: "SendGridCredentials",
    body: list = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you update your subusers' assigned IP.**  Each subuser
    should be assigned to an IP address from which all of this subuser's mail
    will be sent. Often, this is the same IP as the parent account, but each
    subuser can have one or more of their own IP addresses as well.
    More information:  * [How to request more
    IPs](https://sendgrid.com/docs/ui/account-and-settings/dedicated-ip-
    addresses/) * [Setup Reverse DNS](https://sendgrid.com/docs/ui/account-and-
    settings/how-to-set-up-reverse-dns/).

    Args:
        subuser_name:
            Subuser name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/{subuser_name}/ips?&body=%s](
    http://api.sendgrid.com/v3/subusers/{subuser_name}/ips?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/subusers/{subuser_name}/ips"  # noqa
    responses = {}

    params = {
        "body": body,
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
async def get_subusers_subuser_name_monitor(
    subuser_name: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    Retrieve monitor settings for a subuser.

    Args:
        subuser_name:
            Subuser name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor?](
    http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_subusers_subuser_name_monitor(
    subuser_name: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    Create monitor settings.

    Args:
        subuser_name:
            Subuser name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor?&body=%s](
    http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor"  # noqa
    responses = {}

    params = {
        "body": body,
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
async def put_subusers_subuser_name_monitor(
    subuser_name: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    Update Monitor Settings for a subuser.

    Args:
        subuser_name:
            Subuser name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor?&body=%s](
    http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor"  # noqa
    responses = {}

    params = {
        "body": body,
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
async def delete_subusers_subuser_name_monitor(
    subuser_name: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    Delete monitor settings.

    Args:
        subuser_name:
            Subuser name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor?](
    http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/subusers/{subuser_name}/monitor"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_subusers_subuser_name_stats_monthly(
    subuser_name: str,
    date: str,
    sendgrid_credentials: "SendGridCredentials",
    sort_by_metric: str = "delivered",
    sort_by_direction: str = "desc",
    limit: int = 5,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrive the monthly email statistics for a
    specific subuser.**  When using the `sort_by_metric` to sort your stats by a
    specific metric, you can not sort by the following metrics: `bounce_drops`,
    `deferred`, `invalid_emails`, `processed`, `spam_report_drops`,
    `spam_reports`, or `unsubscribe_drops`.

    Args:
        subuser_name:
            Subuser name used in formatting the endpoint URL.
        date:
            The date of the month to retrieve statistics for. Must be formatted
            YYYY-MM-DD.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        sort_by_metric:
            The metric that you want to sort by. Metrics that you can sort by are:
            `blocks`, `bounces`, `clicks`, `delivered`, `opens`,
            `requests`, `unique_clicks`, `unique_opens`, and
            `unsubscribes`.'.
        sort_by_direction:
            The direction you want to sort.
        limit:
            Optional field to limit the number of results returned.
        offset:
            Optional beginning point in the list to retrieve from.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/{subuser_name}/stats/monthly?&date=%s&sort_by_metric=%s&sort_by_direction=%s&limit=%s&offset=%s](
    http://api.sendgrid.com/v3/subusers/{subuser_name}/stats/monthly?&date=%s&sort_by_metric=%s&sort_by_direction=%s&limit=%s&offset=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/subusers/{subuser_name}/stats/monthly"  # noqa
    responses = {}

    params = {
        "date": date,
        "sort_by_metric": sort_by_metric,
        "sort_by_direction": sort_by_direction,
        "limit": limit,
        "offset": offset,
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
async def get_subusers_stats_monthly(
    date: str,
    sendgrid_credentials: "SendGridCredentials",
    subuser: str = None,
    sort_by_metric: str = "delivered",
    sort_by_direction: str = "desc",
    limit: int = 5,
    offset: int = 0,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the monthly email statistics for all
    subusers over the given date range.**  When using the `sort_by_metric` to
    sort your stats by a specific metric, you can not sort by the following
    metrics: `bounce_drops`, `deferred`, `invalid_emails`, `processed`,
    `spam_report_drops`, `spam_reports`, or `unsubscribe_drops`.

    Args:
        date:
            The date of the month to retrieve statistics for. Must be formatted
            YYYY-MM-DD.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        subuser:
            A substring search of your subusers.
        sort_by_metric:
            The metric that you want to sort by. Metrics that you can sort by are:
            `blocks`, `bounces`, `clicks`, `delivered`, `opens`,
            `requests`, `unique_clicks`, `unique_opens`, and
            `unsubscribes`.'.
        sort_by_direction:
            The direction you want to sort.
        limit:
            Optional field to limit the number of results returned.
        offset:
            Optional beginning point in the list to retrieve from.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/stats/monthly?&date=%s&subuser=%s&sort_by_metric=%s&sort_by_direction=%s&limit=%s&offset=%s](
    http://api.sendgrid.com/v3/subusers/stats/monthly?&date=%s&subuser=%s&sort_by_metric=%s&sort_by_direction=%s&limit=%s&offset=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/subusers/stats/monthly"  # noqa

    responses = {}

    params = {
        "date": date,
        "subuser": subuser,
        "sort_by_metric": sort_by_metric,
        "sort_by_direction": sort_by_direction,
        "limit": limit,
        "offset": offset,
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
async def get_subusers_stats_sums(
    start_date: str,
    sendgrid_credentials: "SendGridCredentials",
    sort_by_direction: str = "desc",
    end_date: str = None,
    limit: int = 5,
    offset: int = 0,
    aggregated_by: str = None,
    sort_by_metric: str = "delivered",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the total sums of each email statistic
    metric for all subusers over the given date range.**.

    Args:
        start_date:
            The starting date of the statistics to retrieve. Must follow format
            YYYY-MM-DD.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        sort_by_direction:
            The direction you want to sort.
        end_date:
            The end date of the statistics to retrieve. Defaults to today. Must
            follow format YYYY-MM-DD.
        limit:
            Limits the number of results returned per page.
        offset:
            The point in the list to begin retrieving results from.
        aggregated_by:
            How to group the statistics. Defaults to today. Must follow format YYYY-
            MM-DD.
        sort_by_metric:
            The metric that you want to sort by.  Must be a single metric.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/stats/sums?&sort_by_direction=%s&start_date=%s&end_date=%s&limit=%s&offset=%s&aggregated_by=%s&sort_by_metric=%s](
    http://api.sendgrid.com/v3/subusers/stats/sums?&sort_by_direction=%s&start_date=%s&end_date=%s&limit=%s&offset=%s&aggregated_by=%s&sort_by_metric=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/subusers/stats/sums"  # noqa

    responses = {}

    params = {
        "sort_by_direction": sort_by_direction,
        "start_date": start_date,
        "end_date": end_date,
        "limit": limit,
        "offset": offset,
        "aggregated_by": aggregated_by,
        "sort_by_metric": sort_by_metric,
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
async def get_subusers_stats(
    subusers: str,
    start_date: str,
    sendgrid_credentials: "SendGridCredentials",
    limit: int = None,
    offset: int = None,
    aggregated_by: str = None,
    end_date: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the email statistics for the given
    subusers.**  You may retrieve statistics for up to 10 different subusers by
    including an additional _subusers_ parameter for each additional subuser.

    Args:
        subusers:
            The subuser you want to retrieve statistics for. You may include this
            parameter up to 10 times to retrieve statistics for multiple
            subusers.
        start_date:
            The starting date of the statistics to retrieve. Must follow format
            YYYY-MM-DD.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            Limits the number of results returned per page.
        offset:
            The point in the list to begin retrieving results from.
        aggregated_by:
            How to group the statistics. Must be either 'day', 'week', or 'month'.
        end_date:
            The end date of the statistics to retrieve. Defaults to today.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/subusers/stats?&limit=%s&offset=%s&aggregated_by=%s&subusers=%s&start_date=%s&end_date=%s](
    http://api.sendgrid.com/v3/subusers/stats?&limit=%s&offset=%s&aggregated_by=%s&subusers=%s&start_date=%s&end_date=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/subusers/stats"  # noqa

    responses = {}

    params = {
        "limit": limit,
        "offset": offset,
        "aggregated_by": aggregated_by,
        "subusers": subusers,
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
