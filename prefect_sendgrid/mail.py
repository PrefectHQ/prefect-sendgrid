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
async def post_mail_send(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    The Mail Send endpoint allows you to send email over SendGrid’s v3 Web API, the
    most recent version of our API. If you are looking for documentation about
    the v2 Mail Send endpoint, see our [v2 API
    Reference](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).
    Helper Libraries  Twilio SendGrid provides libraries to help you quickly and
    easily integrate with the v3 Web API in 7 different languages:  * [C
    ](https://github.com/sendgrid/sendgrid-csharp)  *
    [Go](https://github.com/sendgrid/sendgrid-go) *
    [Java](https://github.com/sendgrid/sendgrid-java) * [Node
    JS](https://github.com/sendgrid/sendgrid-nodejs) *
    [PHP](https://github.com/sendgrid/sendgrid-php) *
    [Python](https://github.com/sendgrid/sendgrid-python) *
    [Ruby](https://github.com/sendgrid/sendgrid-ruby)
    Dynamic Transactional Templates and Handlebars  In order to send a dynamic
    template, specify the template ID with the `template_id` parameter.
    To specify handlebar substitutions, define your substitutions in the request
    JSON with this syntax:  ``` 'dynamic_template_data': {       'guest': 'Jane
    Doe',       'partysize': '4',       'english': true,       'date': 'April
    1st, 2021'     } ```  For more information about Dynamic Transactional
    Templates and Handlebars, see our documentation and reference pages.  * [How
    to send an email with Dynamic Transactional Templates
    ](https://sendgrid.com/docs/ui/sending-email/how-to-send-an-email-with-
    dynamic-transactional-templates/) * [Using
    Handlebars](https://sendgrid.com/docs/for-developers/sending-email/using-
    handlebars/)
    Mail Body Compression  Mail body compression is available to some high
    volume accounts. Talk to your CSM if you are interested in this
    functionality. Mail body compression works by setting up a JSON payload as
    defined on this page, then compressing it with gzip (the gzip file can be no
    more than 30mb).  To use mail body compression:  1. Add a `Content-Encoding`
    header, with a value of `gzip`.      a. `Content-Encoding: gzip`  2. Send
    the gzip as a data-binary.      a. `--data-binary '@data.json.gz' `
    Multiple Reply-To Emails  Using `reply_to_list` allows senders to include
    more than one recipient email address to receive reply and/or bounce
    messages from the recipient of the email.
    Usage Considerations  * `reply_to` is mutually exclusive with
    `reply_to_list`. If both are used, then the API call will be rejected.  *
    The `reply_to_list` object, when used, must at least have an email parameter
    and may also contain a name parameter. * Each email address in the
    `reply_to_list` should be unique. * There is a limit of 1000 `reply_to_list`
    emails per mail/send request. * In SMTP calls, we will omit any invalid
    emails.
    Possible 400 Error Messages  * `reply_to` is mutually exclusive with
    `reply_to_list`. * The `reply_to_list` object, when used, must at least have
    an email parameter and may also contain a name parameter. * Each email
    address in the `reply_to_list` should be unique. * There is a limit of X
    `reply_to` emails per mail/send request. * The `reply_to_list` email does
    not contain a valid address. * The `reply_to_list` email exceeds the maximum
    total length of X characters. * The `reply_to_list` email parameter is
    required.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail/send?&body=%s](
    http://api.sendgrid.com/v3/mail/send?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail/send"  # noqa

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
async def post_mail_batch(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to generate a new batch ID.**  Once a `batch_id` is
    created, you can associate it with a scheduled send using the `/mail/send`
    endpoint. Passing the `batch_id` as a field in the `/mail/send` request body
    will assign the ID to the send you are creating.  Once an ID is associated
    with a scheduled send, the send can be accessed and its send status can be
    modified using the `batch_id`.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail/batch?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail/batch?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail/batch"  # noqa

    responses = {}

    params = {
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
async def get_mail_batch_batch_id(
    batch_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to validate a batch ID.**  When you pass a valid
    `batch_id` to this endpoint, it will return a `200` status code and the
    batch ID itself.  If you pass an invalid `batch_id` to the endpoint, you
    will receive a `400` level status code and an error message.  A `batch_id`
    does not need to be assigned to a scheduled send to be considered valid. A
    successful response means only that the `batch_id` has been created, but it
    does not indicate that it has been associated with a send.

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
    [http://api.sendgrid.com/v3/mail/batch/{batch_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail/batch/{batch_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/mail/batch/{batch_id}"  # noqa
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
