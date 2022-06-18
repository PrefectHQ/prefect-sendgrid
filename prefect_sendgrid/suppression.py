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
async def get_suppression_bounces(
    accept: str,
    sendgrid_credentials: "SendGridCredentials",
    start_time: int = None,
    end_time: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of your bounces.**.

    Args:
        accept:

        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        start_time:
            Refers start of the time range in unix timestamp when a bounce was
            created (inclusive).
        end_time:
            Refers end of the time range in unix timestamp when a bounce was created
            (inclusive).
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/bounces?&start_time=%s&end_time=%s&accept=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/bounces?&start_time=%s&end_time=%s&accept=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/suppression/bounces"  # noqa

    responses = {}

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "accept": accept,
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
async def delete_suppression_bounces(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete all emails on your bounces list.**  There
    are two options for deleting bounced emails:
    1. You can delete all bounced emails by setting `delete_all` to `true` in
    the request body.  2. You can delete a selection of bounced emails by
    specifying the email addresses in the `emails` array of the request body.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/bounces?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/bounces?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/suppression/bounces"  # noqa

    responses = {}

    params = {
        "body": body,
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
async def get_suppression_bounces_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a specific bounce by email address.**.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/bounces/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/bounces/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/suppression/bounces/{email}"  # noqa
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
async def delete_suppression_bounces_email(
    email: str,
    email_address: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove an email address from your bounce list.**.

    Args:
        email:
            Email used in formatting the endpoint URL.
        email_address:
            The email address you would like to remove from the bounce list.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/bounces/{email}?&email_address=%s&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/bounces/{email}?&email_address=%s&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/suppression/bounces/{email}"  # noqa
    responses = {}

    params = {
        "email_address": email_address,
        "body": body,
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
async def get_suppression_blocks(
    sendgrid_credentials: "SendGridCredentials",
    start_time: int = None,
    end_time: int = None,
    limit: int = None,
    offset: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all email addresses that are currently on
    your blocks list.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        start_time:
            The start of the time range when a blocked email was created
            (inclusive). This is a unix timestamp.
        end_time:
            The end of the time range when a blocked email was created (inclusive).
            This is a unix timestamp.
        limit:
            Limit the number of results to be displayed per page.
        offset:
            The point in the list to begin displaying results.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/blocks?&start_time=%s&end_time=%s&limit=%s&offset=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/blocks?&start_time=%s&end_time=%s&limit=%s&offset=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/suppression/blocks"  # noqa

    responses = {}

    params = {
        "start_time": start_time,
        "end_time": end_time,
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


@task
async def delete_suppression_blocks(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete all email addresses on your blocks list.**
    There are two options for deleting blocked emails:
    1. You can delete all blocked emails by setting `delete_all` to `true` in
    the request body.  2. You can delete a selection of blocked emails by
    specifying the email addresses in the `emails` array of the request body.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/blocks?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/blocks?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/suppression/blocks"  # noqa

    responses = {}

    params = {
        "body": body,
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
async def get_suppression_blocks_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a specific email address from your blocks
    list.**.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/blocks/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/blocks/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/suppression/blocks/{email}"  # noqa
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
async def delete_suppression_blocks_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a specific email address from your blocks
    list.**.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/blocks/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/blocks/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/suppression/blocks/{email}"  # noqa
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
async def get_suppression_spam_reports(
    sendgrid_credentials: "SendGridCredentials",
    start_time: int = None,
    end_time: int = None,
    limit: int = None,
    offset: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all spam reports.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        start_time:
            The start of the time range when a spam report was created (inclusive).
            This is a unix timestamp.
        end_time:
            The end of the time range when a spam report was created (inclusive).
            This is a unix timestamp.
        limit:
            Limit the number of results to be displayed per page.
        offset:
            Paging offset. The point in the list to begin displaying results.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/spam_reports?&start_time=%s&end_time=%s&limit=%s&offset=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/spam_reports?&start_time=%s&end_time=%s&limit=%s&offset=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/suppression/spam_reports"  # noqa

    responses = {}

    params = {
        "start_time": start_time,
        "end_time": end_time,
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


@task
async def delete_suppression_spam_reports(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete your spam reports.**  Deleting a spam
    report will remove the suppression, meaning email will once again be sent to
    the previously suppressed address. This should be avoided unless a recipient
    indicates they wish to receive email from you again. You can use our [bypass
    filters](https://sendgrid.com/docs/ui/sending-email/index-suppressions/
    bypass-suppressions) to deliver messages to otherwise suppressed addresses
    when exceptions are required.  There are two options for deleting spam
    reports:
    1. You can delete all spam reports by setting the `delete_all` field to
    `true` in the request body. 2. You can delete a list of select spam reports
    by specifying the email addresses in the `emails` array of the request body.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/spam_reports?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/spam_reports?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/suppression/spam_reports"  # noqa

    responses = {}

    params = {
        "body": body,
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
async def get_suppression_spam_reports_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a specific spam report by email
    address.**.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/spam_reports/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/spam_reports/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/suppression/spam_reports/{email}"  # noqa
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
async def delete_suppression_spam_reports_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a specific spam report by email address.**
    Deleting a spam report will remove the suppression, meaning email will once
    again be sent to the previously suppressed address. This should be avoided
    unless a recipient indicates they wish to receive email from you again. You
    can use our [bypass filters](https://sendgrid.com/docs/ui/sending-
    email/index-suppressions/
    bypass-suppressions) to deliver messages to otherwise suppressed addresses
    when exceptions are required.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/spam_reports/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/spam_reports/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/suppression/spam_reports/{email}"  # noqa
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
async def get_suppression_unsubscribes(
    sendgrid_credentials: "SendGridCredentials",
    start_time: int = None,
    end_time: int = None,
    limit: int = None,
    offset: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all email address that are
    globally suppressed.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        start_time:
            Refers start of the time range in unix timestamp when an unsubscribe
            email was created (inclusive).
        end_time:
            Refers end of the time range in unix timestamp when an unsubscribe email
            was created (inclusive).
        limit:
            The number of results to display on each page.
        offset:
            The point in the list of results to begin displaying global
            suppressions.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/unsubscribes?&start_time=%s&end_time=%s&limit=%s&offset=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/unsubscribes?&start_time=%s&end_time=%s&limit=%s&offset=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/suppression/unsubscribes"  # noqa

    responses = {}

    params = {
        "start_time": start_time,
        "end_time": end_time,
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


@task
async def get_suppression_invalid_emails(
    sendgrid_credentials: "SendGridCredentials",
    start_time: int = None,
    end_time: int = None,
    limit: int = None,
    offset: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all invalid email addresses.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        start_time:
            Refers start of the time range in unix timestamp when an invalid email
            was created (inclusive).
        end_time:
            Refers end of the time range in unix timestamp when an invalid email was
            created (inclusive).
        limit:
            Limit the number of results to be displayed per page.
        offset:
            Paging offset. The point in the list to begin displaying results.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/invalid_emails?&start_time=%s&end_time=%s&limit=%s&offset=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/invalid_emails?&start_time=%s&end_time=%s&limit=%s&offset=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/suppression/invalid_emails"  # noqa

    responses = {}

    params = {
        "start_time": start_time,
        "end_time": end_time,
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


@task
async def delete_suppression_invalid_emails(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove email addresses from your invalid email
    address list.**  There are two options for deleting invalid email addresses:
    1) You can delete all invalid email addresses by setting `delete_all` to
    true in the request body. 2) You can delete some invalid email addresses by
    specifying certain addresses in an array in the request body.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/invalid_emails?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/invalid_emails?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/suppression/invalid_emails"  # noqa

    responses = {}

    params = {
        "body": body,
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
async def get_suppression_invalid_emails_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a specific invalid email addresses.**.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/invalid_emails/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/invalid_emails/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/suppression/invalid_emails/{email}"  # noqa
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
async def delete_suppression_invalid_emails_email(
    email: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove a specific email address from the invalid
    email address list.**.

    Args:
        email:
            Email used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/suppression/invalid_emails/{email}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/suppression/invalid_emails/{email}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/suppression/invalid_emails/{email}"  # noqa
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
