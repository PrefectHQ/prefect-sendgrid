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
async def get_verified_senders_domains(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint returns a list of domains known to implement DMARC and
    categorizes them by failure type — hard failure or soft failure**.  Domains
    listed as hard failures will not deliver mail when used as a [Sender
    Identity](https://sendgrid.com/docs/for-developers/sending-email/sender-
    identity/) due to the domain's DMARC policy settings.  For example, using a
    `yahoo.com` email address as a Sender Identity will likely result in the
    rejection of your mail. For more information about DMARC, see [Everything
    about DMARC](https://sendgrid.com/docs/ui/sending-email/dmarc/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/verified_senders/domains?](
    http://api.sendgrid.com/v3/verified_senders/domains?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/verified_senders/domains"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_verified_senders_steps_completed(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to determine which of SendGrid’s verification
    processes have been completed for an account**.  This endpoint returns
    boolean values, `true` and `false`, for [Domain
    Authentication](https://sendgrid.com/docs/for-developers/sending-
    email/sender-identity/
    domain-authentication), `domain_verified`, and [Single Sender
    Verification](https://sendgrid.com/docs/for-developers/sending-email/sender-
    identity/
    single-sender-verification), `sender_verified`, for the account.  An account
    may have one, both, or neither verification steps completed. If you need to
    authenticate a domain rather than a Single Sender, see the 'Authenticate a
    domain' endpoint.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/verified_senders/steps_completed?](
    http://api.sendgrid.com/v3/verified_senders/steps_completed?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/verified_senders/steps_completed"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_verified_senders(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new Sender Identify**.  Upon successful
    submission of a `POST` request to this endpoint, an identity will be
    created, and a verification email will be sent to the address assigned to
    the `from_email` field. You must complete the verification process using the
    sent email to fully verify the sender.  If you need to resend the
    verification email, you can do so with the Resend Verified Sender Request,
    `/resend/{id}`, endpoint.  If you need to authenticate a domain rather than
    a Single Sender, see the [Domain Authentication API](https://sendgrid.api-
    docs.io/v3.0/domain-authentication/authenticate-a-domain).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/verified_senders?&body=%s](
    http://api.sendgrid.com/v3/verified_senders?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/verified_senders"  # noqa

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
async def get_verified_senders(
    sendgrid_credentials: "SendGridCredentials",
    limit: str = None,
    last_seen_id: str = None,
    id: int = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all the Sender Identities associated with
    an account.**  This endpoint will return both verified and unverified
    senders.  You can limit the number of results returned using the `limit`,
    `lastSeenID`, and `id` query string parameters.  * `limit` allows you to
    specify an exact number of Sender Identities to return. * `lastSeenID` will
    return senders with an ID number occuring after the passed in ID. In other
    words, the `lastSeenID` provides a starting point from which SendGrid will
    iterate to find Sender Identities associated with your account. * `id` will
    return information about only the Sender Identity passed in the request.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:

        last_seen_id:

        id:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/verified_senders?&limit=%s&last_seen_id=%s&id=%s](
    http://api.sendgrid.com/v3/verified_senders?&limit=%s&last_seen_id=%s&id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/verified_senders"  # noqa

    responses = {}

    params = {
        "limit": limit,
        "last_seen_id": last_seen_id,
        "id": id,
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
async def get_verified_senders_verify_token(
    token: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to verify a sender requests.**  The token is
    generated by SendGrid and included in a verification email delivered to the
    address that's pending verification.

    Args:
        token:
            Token used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/verified_senders/verify/{token}?](
    http://api.sendgrid.com/v3/verified_senders/verify/{token}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/verified_senders/verify/{token}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def patch_verified_senders_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update an existing Sender Identity**.  Pass the
    `id` assigned to a Sender Identity to this endpoint as a path parameter.
    Include any fields you wish to update in the request body in JSON format.
    You can retrieve the IDs associated with Sender Identities by passing a
    `GET` request to the Get All Verified Senders endpoint, `/verified_senders`.
    **Note:** Unlike a `PUT` request, `PATCH` allows you to update only the
    fields you wish to edit. Fields that are not passed as part of a request
    will remain unaltered.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/verified_senders/{id}?&body=%s](
    http://api.sendgrid.com/v3/verified_senders/{id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/verified_senders/{id}"  # noqa
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
async def delete_verified_senders_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a Sender Identity**.  Pass the `id`
    assigned to a Sender Identity to this endpoint to delete the Sender Identity
    from your account.  You can retrieve the IDs associated with Sender
    Identities using the 'Get All Verified Senders' endpoint.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/verified_senders/{id}?](
    http://api.sendgrid.com/v3/verified_senders/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/verified_senders/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_verified_senders_resend_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to resend a verification email to a specified Sender
    Identity**.  Passing the `id` assigned to a Sender Identity to this endpoint
    will resend a verification email to the `from_address` associated with the
    Sender Identity. This can be useful if someone loses their verification
    email or needs to have it resent for any other reason.  You can retrieve the
    IDs associated with Sender Identities by passing a 'Get All Verified
    Senders' endpoint.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/verified_senders/resend/{id}?](
    http://api.sendgrid.com/v3/verified_senders/resend/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/verified_senders/resend/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result
