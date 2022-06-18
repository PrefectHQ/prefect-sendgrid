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
async def post_ips_warmup(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to put an IP address into warmup mode.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/warmup?&body=%s](
    http://api.sendgrid.com/v3/ips/warmup?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/ips/warmup"  # noqa

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
async def get_ips_warmup(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of your IP addresses that are
    currently warming up.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/warmup?](
    http://api.sendgrid.com/v3/ips/warmup?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/ips/warmup"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_ips_warmup_ip_address(
    ip_address: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the warmup status for a specific IP
    address.**  You can retrieve all of your warming IPs using the 'Retrieve all
    IPs currently in warmup' endpoint.

    Args:
        ip_address:
            Ip address used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/warmup/{ip_address}?](
    http://api.sendgrid.com/v3/ips/warmup/{ip_address}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/ips/warmup/{ip_address}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def delete_ips_warmup_ip_address(
    ip_address: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove an IP address from warmup mode.**  Your
    request will return a 204 status code if the specified IP was successfully
    removed from warmup mode. To retrieve details of the IP’s warmup status
    *before* removing it from warmup mode, call the  'Retrieve the warmpup
    status for a specific IP address' endpoint.

    Args:
        ip_address:
            Ip address used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/warmup/{ip_address}?](
    http://api.sendgrid.com/v3/ips/warmup/{ip_address}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/ips/warmup/{ip_address}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_ips_pools(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create an IP pool.**  Before you can create an IP
    pool, you need to activate the IP in your SendGrid account:
    1. Log into your SendGrid account.   1. Navigate to **Settings** and then
    select **IP Addresses**.   1. Find the IP address you want to activate and
    then click **Edit**.   1. Check **Allow my account to send mail using this
    IP address**. 1. Click **Save**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/pools?&body=%s](
    http://api.sendgrid.com/v3/ips/pools?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/ips/pools"  # noqa

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
async def get_ips_pools(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to get all of your IP pools.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/pools?](
    http://api.sendgrid.com/v3/ips/pools?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/ips/pools"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_ips_pools_pool_name_ips(
    pool_name: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to add an IP address to an IP pool.**  You can add
    the same IP address to multiple pools. It may take up to 60 seconds for your
    IP address to be added to a pool after your request is made.  Before you can
    add an IP to a pool, you need to activate it in your SendGrid account:  1.
    Log into your SendGrid account.   1. Navigate to **Settings** and then
    select **IP Addresses**.   1. Find the IP address you want to activate and
    then click **Edit**.   1. Check **Allow my account to send mail using this
    IP address**. 1. Click **Save**.  You can retrieve all of your available IP
    addresses from the 'Retrieve all IP addresses' endpoint.

    Args:
        pool_name:
            Pool name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/pools/{pool_name}/ips?&body=%s](
    http://api.sendgrid.com/v3/ips/pools/{pool_name}/ips?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/ips/pools/{pool_name}/ips"  # noqa
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
async def get_ips_pools_pool_name(
    pool_name: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to get all of the IP addresses that are in a specific
    IP pool.**.

    Args:
        pool_name:
            Pool name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/pools/{pool_name}?](
    http://api.sendgrid.com/v3/ips/pools/{pool_name}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/ips/pools/{pool_name}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def put_ips_pools_pool_name(
    pool_name: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update the name of an IP pool.**.

    Args:
        pool_name:
            Pool name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/pools/{pool_name}?&body=%s](
    http://api.sendgrid.com/v3/ips/pools/{pool_name}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/ips/pools/{pool_name}"  # noqa
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
async def delete_ips_pools_pool_name(
    pool_name: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete an IP pool.**.

    Args:
        pool_name:
            Pool name used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/pools/{pool_name}?](
    http://api.sendgrid.com/v3/ips/pools/{pool_name}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/ips/pools/{pool_name}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def delete_ips_pools_pool_name_ips_ip(
    pool_name: str,
    ip: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove an IP address from an IP pool.**.

    Args:
        pool_name:
            Pool name used in formatting the endpoint URL.
        ip:
            Ip used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/pools/{pool_name}/ips/{ip}?](
    http://api.sendgrid.com/v3/ips/pools/{pool_name}/ips/{ip}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/ips/pools/{pool_name}/ips/{ip}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_ips(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint is for adding a(n) IP Address(es) to your account.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips?&body=%s](
    http://api.sendgrid.com/v3/ips?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/ips"  # noqa

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
async def get_ips(
    sendgrid_credentials: "SendGridCredentials",
    ip: str = None,
    exclude_whitelabels: bool = None,
    limit: int = 10,
    offset: int = 0,
    subuser: str = None,
    sort_by_direction: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all assigned and unassigned
    IPs.**  Response includes warm up status, pools, assigned subusers, and
    reverse DNS info. The start_date field corresponds to when warmup started
    for that IP.  A single IP address or a range of IP addresses may be
    dedicated to an account in order to send email for multiple domains. The
    reputation of this IP is based on the aggregate performance of all the
    senders who use it.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        ip:
            The IP address to get.
        exclude_whitelabels:
            Should we exclude reverse DNS records (whitelabels)?.
        limit:
            The number of IPs you want returned at the same time.
        offset:
            The offset for the number of IPs that you are requesting.
        subuser:
            The subuser you are requesting for.
        sort_by_direction:
            The direction to sort the results.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips?&ip=%s&exclude_whitelabels=%s&limit=%s&offset=%s&subuser=%s&sort_by_direction=%s](
    http://api.sendgrid.com/v3/ips?&ip=%s&exclude_whitelabels=%s&limit=%s&offset=%s&subuser=%s&sort_by_direction=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/ips"  # noqa

    responses = {}

    params = {
        "ip": ip,
        "exclude_whitelabels": exclude_whitelabels,
        "limit": limit,
        "offset": offset,
        "subuser": subuser,
        "sort_by_direction": sort_by_direction,
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
async def get_ips_remaining(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint gets amount of IP Addresses that can still be created during a
    given period and the price of those IPs.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/remaining?](
    http://api.sendgrid.com/v3/ips/remaining?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/ips/remaining"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_ips_assigned(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve only assigned IP addresses.**  A single
    IP address or a range of IP addresses may be dedicated to an account in
    order to send email for multiple domains. The reputation of this IP is based
    on the aggregate performance of all the senders who use it.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/assigned?](
    http://api.sendgrid.com/v3/ips/assigned?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/ips/assigned"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_ips_ip_address(
    ip_address: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to see which IP pools a particular IP address has
    been added to.**  The same IP address can be added to multiple IP pools.  A
    single IP address or a range of IP addresses may be dedicated to an account
    in order to send email for multiple domains. The reputation of this IP is
    based on the aggregate performance of all the senders who use it.

    Args:
        ip_address:
            Ip address used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/ips/{ip_address}?](
    http://api.sendgrid.com/v3/ips/{ip_address}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/ips/{ip_address}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result
