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
async def post_user_scheduled_sends(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to cancel or pause a scheduled send associated with a
    `batch_id`.**  Passing this endpoint a `batch_id` and status will cancel or
    pause the scheduled send.  Once a scheduled send is set to `pause` or
    `cancel` you must use the 'Update a scheduled send' endpoint to change its
    status or the 'Delete a cancellation or pause from a scheduled send'
    endpoint to remove the status. Passing a status change to a scheduled send
    that has already been paused or cancelled will result in a `400` level
    status code.  If the maximum number of cancellations/pauses are added to a
    send, a `400` level status code will be returned.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/scheduled_sends?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/scheduled_sends?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/scheduled_sends"  # noqa

    responses = {}

    params = {
        "body": body,
        "on_behalf_of": on_behalf_of,
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
async def get_user_scheduled_sends(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all cancelled and paused scheduled send
    information.**  This endpoint will return only the scheduled sends that are
    associated with a `batch_id`. If you have scheduled a send using the
    `/mail/send` endpoint and the `send_at` field but no `batch_id`, the send
    will be scheduled for delivery; however, it will not be returned by this
    endpoint. For this reason, you should assign a `batch_id` to any scheduled
    send you may need to pause or cancel in the future.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/scheduled_sends?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/scheduled_sends?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/scheduled_sends"  # noqa

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
async def get_user_scheduled_sends_batch_id(
    batch_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the cancel/paused scheduled send
    information for a specific `batch_id`.**.

    Args:
        batch_id:
            Batch id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/scheduled_sends/{batch_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/scheduled_sends/{batch_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/user/scheduled_sends/{batch_id}"  # noqa
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
async def patch_user_scheduled_sends_batch_id(
    batch_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update the status of a scheduled send for the
    given `batch_id`.**  If you have already set a `cancel` or `pause` status on
    a scheduled send using the 'Cancel or pause a scheduled send' endpoint, you
    can update it's status using this endpoint. Attempting to update a status
    once it has been set with the 'Cancel or pause a scheduled send' endpoint
    will result in a `400` error.

    Args:
        batch_id:
            Batch id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/scheduled_sends/{batch_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/scheduled_sends/{batch_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/user/scheduled_sends/{batch_id}"  # noqa
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
async def delete_user_scheduled_sends_batch_id(
    batch_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete the cancellation/pause of a scheduled
    send.**  Scheduled sends cancelled less than 10 minutes before the scheduled
    time are not guaranteed to be cancelled.

    Args:
        batch_id:
            Batch id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/scheduled_sends/{batch_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/scheduled_sends/{batch_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/user/scheduled_sends/{batch_id}"  # noqa
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
async def get_user_settings_enforced_tls(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current Enforced TLS settings.**
    The Enforced TLS settings specify whether or not the recipient is required
    to support TLS or have a valid certificate.  If either `require_tls` or
    `require_valid_cert` is set to `true`, the recipient must support TLS 1.1 or
    higher or have a valid certificate. If these conditions are not met, Twilio
    SendGrid will drop the message and send a block event with “TLS required but
    not supported” as the description.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/settings/enforced_tls?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/settings/enforced_tls?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/settings/enforced_tls"  # noqa

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
async def patch_user_settings_enforced_tls(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your Enforced TLS settings.**  To require
    TLS from recipients, set `require_tls` to `true`. If either `require_tls` or
    `require_valid_cert` is set to `true`, the recipient must support TLS 1.1 or
    higher or have a valid certificate. If these conditions are not met, Twilio
    SendGrid will drop the message and send a block event with “TLS required but
    not supported” as the description.  > Twilio SendGrid supports TLS 1.1 and
    higher and does not support older versions of TLS due to security
    vulnerabilities.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/settings/enforced_tls?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/settings/enforced_tls?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/settings/enforced_tls"  # noqa

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
async def get_user_profile(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    Get a user's profile.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/profile?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/profile?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/profile"  # noqa

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
async def patch_user_profile(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current profile details.**  Any one or
    more of the parameters can be updated via the PATCH `/user/profile`
    endpoint. You must include at least one when you PATCH.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/profile?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/profile?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/profile"  # noqa

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
async def get_user_account(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your user account details.**  Your user's
    account information includes the user's account type and reputation.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/account?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/account?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/account"  # noqa

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
async def get_user_email(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the email address currently on file for
    your account.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/email?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/email?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/email"  # noqa

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
async def put_user_email(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update the email address currently on file for
    your account.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/email?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/email?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/email"  # noqa

    responses = {}

    params = {
        "body": body,
        "on_behalf_of": on_behalf_of,
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
async def get_user_username(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current account username.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/username?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/username?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/username"  # noqa

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
async def put_user_username(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update the username for your account.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/username?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/username?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/username"  # noqa

    responses = {}

    params = {
        "body": body,
        "on_behalf_of": on_behalf_of,
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
async def get_user_credits(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the current credit balance for your
    account.**  Each account has a credit balance, which is a base number of
    emails it can send before receiving per-email charges. For more information
    about credits and billing, see [Billing and Plan details
    information](https://sendgrid.com/docs/ui/account-and-settings/billing/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/credits?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/credits?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/credits"  # noqa

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
async def put_user_password(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your password.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/password?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/password?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/password"  # noqa

    responses = {}

    params = {
        "body": body,
        "on_behalf_of": on_behalf_of,
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
async def get_user_webhooks_event_settings(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current event webhook settings.**
    If an event type is marked as `true`, then the event webhook will include
    information about that event.  SendGrid’s Event Webhook will notify a URL of
    your choice via HTTP POST with information about events that occur as
    SendGrid processes your email.  Common uses of this data are to remove
    unsubscribes, react to spam reports, determine unengaged recipients,
    identify bounced email addresses, or create advanced analytics of your email
    program.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/event/settings?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/event/settings?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/webhooks/event/settings"  # noqa

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
async def patch_user_webhooks_event_settings(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current event webhook settings.**  If
    an event type is marked as `true`, then the event webhook will include
    information about that event.  SendGrid’s Event Webhook will notify a URL of
    your choice via HTTP POST with information about events that occur as
    SendGrid processes your email.  Common uses of this data are to remove
    unsubscribes, react to spam reports, determine unengaged recipients,
    identify bounced email addresses, or create advanced analytics of your email
    program.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/event/settings?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/event/settings?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/webhooks/event/settings"  # noqa

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
async def get_user_webhooks_parse_settings(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of your current inbound parse
    settings.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/parse/settings?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/parse/settings?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/webhooks/parse/settings"  # noqa

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
async def post_user_webhooks_parse_settings(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new inbound parse setting.**  Creating an
    Inbound Parse setting requires two pieces of information: a `url` and a
    `hostname`.  The `hostname` must correspond to a domain authenticated by
    Twilio SendGrid on your account. If you need to complete domain
    authentication, you can use the [Twilio SendGrid
    App](https://app.sendgrid.com/settings/sender_auth) or the 'Authenticate a
    domain' endpoint. See '[How to Set Up Domain
    Authentication](https://sendgrid.com/docs/ui/account-and-settings/how-to-
    set-up-domain-authentication/)' for instructions.  Any email received by the
    `hostname` will be parsed when you complete this setup. You must also add a
    Twilio SendGrid MX record to this domain's DNS records. See '[Setting up the
    Inbound Parse Webhook](https://sendgrid.com/docs/for-developers/parsing-
    email/setting-up-the-inbound-parse-webhook/)' for full instructions.  The
    `url` represents a location where the parsed message data will be delivered.
    Twilio SendGrid will make an HTTP POST request to this `url` with the
    message data. The `url` must be publicly reachable, and your application
    must return a `200` status code to signal that the message data has been
    received.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/parse/settings?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/parse/settings?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/webhooks/parse/settings"  # noqa

    responses = {}

    params = {
        "body": body,
        "on_behalf_of": on_behalf_of,
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
async def get_user_webhooks_parse_stats(
    start_date: str,
    sendgrid_credentials: "SendGridCredentials",
    limit: str = None,
    offset: str = None,
    aggregated_by: str = None,
    end_date: str = "The day the request is made.",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the statistics for your Parse Webhook
    useage.**  SendGrid's Inbound Parse Webhook allows you to parse the contents
    and attachments of incomming emails. The Parse API can then POST the parsed
    emails to a URL that you specify. The Inbound Parse Webhook cannot parse
    messages greater than 30MB in size, including all attachments.  There are a
    number of pre-made integrations for the SendGrid Parse Webhook which make
    processing events easy. You can find these integrations in the [Library
    Index](https://sendgrid.com/docs/Integrate/libraries.html
    -Webhook-Libraries).

    Args:
        start_date:
            The starting date of the statistics you want to retrieve. Must be in the
            format YYYY-MM-DD.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            The number of statistics to return on each page.
        offset:
            The number of statistics to skip.
        aggregated_by:
            How you would like the statistics to by grouped.
        end_date:
            The end date of the statistics you want to retrieve. Must be in the
            format YYYY-MM-DD.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/parse/stats?&limit=%s&offset=%s&aggregated_by=%s&start_date=%s&end_date=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/parse/stats?&limit=%s&offset=%s&aggregated_by=%s&start_date=%s&end_date=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/webhooks/parse/stats"  # noqa

    responses = {}

    params = {
        "limit": limit,
        "offset": offset,
        "aggregated_by": aggregated_by,
        "start_date": start_date,
        "end_date": end_date,
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
async def get_user_webhooks_event_settings_signed(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your signed webhook's public key.**  Once
    you have enabled signing of the Event Webhook, you will need the public key
    provided to verify the signatures on requests coming from Twilio SendGrid.
    You can retrieve the public key from this endpoint at any time.  For more
    information about cryptographically signing the Event Webhook, see [Getting
    Started with the Event Webhook Security
    Features](https://sendgrid.com/docs/for-developers/tracking-events/getting-
    started-event-webhook-security-features).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/event/settings/signed?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/event/settings/signed?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/webhooks/event/settings/signed"  # noqa

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
async def patch_user_webhooks_event_settings_signed(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to enable or disable signing of the Event Webhook.**
    This endpoint takes a single boolean request parameter, `enabled`. You may
    either enable or disable signing of the Event Webhook using this endpoint.
    Once enabled, you can retrieve your public key using the
    `/webhooks/event/settings/signed` endpoint.  For more information about
    cryptographically signing the Event Webhook, see [Getting Started with the
    Event Webhook Security Features](https://sendgrid.com/docs/for-
    developers/tracking-events/getting-started-event-webhook-security-features).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/event/settings/signed?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/event/settings/signed?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/webhooks/event/settings/signed"  # noqa

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
async def post_user_webhooks_event_test(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to test your event webhook by sending a fake event
    notification post to the provided URL.**  SendGrid’s Event Webhook will
    notify a URL of your choice via HTTP POST with information about events that
    occur as SendGrid processes your email.  Common uses of this data are to
    remove unsubscribes, react to spam reports, determine unengaged recipients,
    identify bounced email addresses, or create advanced analytics of your email
    program.  >**Tip**: Retry logic for this endpoint differs from other
    endpoints, which use a rolling 24-hour retry.  If your web server does not
    return a 2xx response type, we will retry a POST request until we receive a
    2xx response or the maximum time of 10 minutes has expired.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/event/test?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/event/test?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/user/webhooks/event/test"  # noqa

    responses = {}

    params = {
        "body": body,
        "on_behalf_of": on_behalf_of,
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
async def get_user_webhooks_parse_settings_hostname(
    hostname: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a specific inbound parse setting by
    hostname.**  You can retrieve all your Inbound Parse settings and their
    associated host names with the 'Retrieve all parse settings' endpoint.

    Args:
        hostname:
            Hostname used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/parse/settings/{hostname}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/parse/settings/{hostname}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/user/webhooks/parse/settings/{hostname}"  # noqa
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
async def patch_user_webhooks_parse_settings_hostname(
    hostname: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update a specific inbound parse setting by
    hostname.**  You can retrieve all your Inbound Parse settings and their
    associated host names with the 'Retrieve all parse settings' endpoint.

    Args:
        hostname:
            Hostname used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/parse/settings/{hostname}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/parse/settings/{hostname}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/user/webhooks/parse/settings/{hostname}"  # noqa
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
async def delete_user_webhooks_parse_settings_hostname(
    hostname: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a specific inbound parse setting by
    hostname.**  You can retrieve all your Inbound Parse settings and their
    associated host names with the 'Retrieve all parse settings' endpoint.

    Args:
        hostname:
            Hostname used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/user/webhooks/parse/settings/{hostname}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/user/webhooks/parse/settings/{hostname}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/user/webhooks/parse/settings/{hostname}"  # noqa
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
