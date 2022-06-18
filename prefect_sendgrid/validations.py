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
async def post_validations_email(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to validate an email address.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/validations/email?&body=%s](
    http://api.sendgrid.com/v3/validations/email?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/validations/email"  # noqa

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
