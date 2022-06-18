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
async def get_messages(
    query: str,
    authorization: str,
    sendgrid_credentials: "SendGridCredentials",
    limit: str = 10,
    x_query_id: str = None,
    x_cursor: str = None,
) -> Dict[str, Any]:
    """
    This is **BETA** functionality. You may not have access, and we reserve the
    right to change functionality without notice.  Filter all messages to search
    your Email Activity. All queries need to be [URL
    encoded](https://meyerweb.com/eric/tools/dencoder/), and have this format:
    `query={query_type}='{query_content}'`  encoded, this would look like this:
    `query=type%3D%22query_content%22`  for example:  Filter by a specific email
    - `query=to_email%3D%22example%40example.com%22`  Filter by subject line -
    `query=subject%3d%22A%20Great%20Subject%22`  **Full list of basic query
    types and examples:**   | **Filter query**    | **Unencoded Example** (put
    this one into the try it out query - it'll automatically encode it for you)
    | **Encoded Example** (use this one in your code)                        |
    |-----------------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
    | msg_id          | msg_id=“filter0307p1las1-16816-5A023E36-1.0”
    | msg_id%3D%22filter0307p1las1-16816-5A023E36-1.0%22           | |
    from_email      | from_email=“testing@sendgrid.net”
    | from_email%3D%22testing%40sendgrid.net%22                    | | subject
    | subject='This is a subject test'
    | subject%22This%20is%20a%20subject%20test%22                  | | to_email
    | to_email='example@example.com'
    | to_email%3D%22example%40example.com%22                       | | status
    |
    | status%22processed%22                                        | |
    template_id     |
    |                                                                    | |
    asm_group_id    |
    |                                                                    | |
    api_key_id      |
    |                                                                    | |
    events          | status='processed'
    | status%3D%22processed%22                                     | |
    originating_ip  |
    |                                                                    | |
    categories      |
    |                                                                    | |
    unique_args     |
    |                                                                    | |
    outbound_ip     |
    |                                                                    | |
    last_event_time | last_event_time=“2017-11-07T23:13:58Z”
    | last_event_time%3D%E2%80%9C2017-11-07T23%3A13%3A58Z%E2%80%9D | | clicks
    | clicks='0'
    | clicks%3D%220%22                                             |  For
    information about building compound queries, and for the full query language
    functionality, see the [query language
    reference](https://docs.google.com/a/sendgrid.com/document/d/1fWoKTFNfg5UUsB6t9KuIcSo9CetKF_T0bGfWJ_gdPCs/edit?usp=sharing).
    Coming soon, example compound queries: limit + to email + date.

    Args:
        query:
            Use the query syntax  to filter your email activity.
        authorization:

        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            The number of messages returned. This parameter must be greater than 0
            and less than or equal to 1000.
        x_query_id:

        x_cursor:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/messages?&query=%s&limit=%s&x_query_id=%s&x_cursor=%s&authorization=%s](
    http://api.sendgrid.com/v3/messages?&query=%s&limit=%s&x_query_id=%s&x_cursor=%s&authorization=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/messages"  # noqa

    responses = {}

    params = {
        "query": query,
        "limit": limit,
        "x_query_id": x_query_id,
        "x_cursor": x_cursor,
        "authorization": authorization,
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
async def get_messages_msg_id(
    msg_id: str,
    authorization: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    This is BETA functionality. You may not have access, and we reserve the right to
    change functionality without notice.  Get all of the details about the
    specified message.

    Args:
        msg_id:
            Msg id used in formatting the endpoint URL.
        authorization:

        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/messages/{msg_id}?&authorization=%s](
    http://api.sendgrid.com/v3/messages/{msg_id}?&authorization=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/messages/{msg_id}"  # noqa
    responses = {}

    params = {
        "authorization": authorization,
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
async def post_messages_download(
    authorization: str,
    sendgrid_credentials: "SendGridCredentials",
    query: str = None,
) -> Dict[str, Any]:
    """
    This is BETA functionality. You may not have access, and we reserve the right to
    change functionality without notice.  This request will kick off a backend
    process to generate a CSV file. Once generated, the worker will then send an
    email for the user download the file. The link will expire in 3 days.  The
    CSV fill contain the last 1 million messages. This endpoint will be rate
    limited to 1 request every 12 hours (rate limit may change).  This endpoint
    is similar to the GET Single Message endpoint - the only difference is that
    /download is added to indicate that this is a CSV download requests but the
    same query is used to determine what the CSV should contain.

    Args:
        authorization:

        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        query:
            Uses a SQL like syntax to indicate which messages to include in the CSV.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/messages/download?&query=%s&authorization=%s](
    http://api.sendgrid.com/v3/messages/download?&query=%s&authorization=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/messages/download"  # noqa

    responses = {}

    params = {
        "query": query,
        "authorization": authorization,
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
async def get_messages_download_download_uuid(
    download_uuid: str,
    authorization: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint will return a presigned URL that can be used to download the CSV
    that was requested from the 'Request a CSV' endpoint.**.

    Args:
        download_uuid:
            Download uuid used in formatting the endpoint URL.
        authorization:

        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/messages/download/{download_uuid}?&authorization=%s](
    http://api.sendgrid.com/v3/messages/download/{download_uuid}?&authorization=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/messages/download/{download_uuid}"  # noqa
    responses = {}

    params = {
        "authorization": authorization,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
