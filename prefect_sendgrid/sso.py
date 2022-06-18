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
async def post_sso_certificates(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create an SSO certificate.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/certificates?&body=%s](
    http://api.sendgrid.com/v3/sso/certificates?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/sso/certificates"  # noqa

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
async def get_sso_integrations_integration_id_certificates(
    integration_id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all your IdP configurations by
    configuration ID.**  The `integration_id` expected by this endpoint is the
    `id` returned in the response by the 'Get All SSO Integrations' endpoint.

    Args:
        integration_id:
            Integration id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/integrations/{integration_id}/certificates?](
    http://api.sendgrid.com/v3/sso/integrations/{integration_id}/certificates?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/sso/integrations/{integration_id}/certificates"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_sso_certificates_cert_id(
    cert_id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve an individual SSO certificate.**.

    Args:
        cert_id:
            Cert id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/certificates/{cert_id}?](
    http://api.sendgrid.com/v3/sso/certificates/{cert_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/sso/certificates/{cert_id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def patch_sso_certificates_cert_id(
    cert_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update an existing certificate by ID.**  You can
    retrieve a certificate's ID from the response provided by the 'Get All SSO
    Integrations' endpoint.

    Args:
        cert_id:
            Cert id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/certificates/{cert_id}?&body=%s](
    http://api.sendgrid.com/v3/sso/certificates/{cert_id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/sso/certificates/{cert_id}"  # noqa
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
async def delete_sso_certificates_cert_id(
    cert_id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete an SSO certificate.**  You can retrieve a
    certificate's ID from the response provided by the 'Get All SSO
    Integrations' endpoint.

    Args:
        cert_id:
            Cert id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/certificates/{cert_id}?](
    http://api.sendgrid.com/v3/sso/certificates/{cert_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/sso/certificates/{cert_id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_sso_integrations(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create an SSO integration.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/integrations?&body=%s](
    http://api.sendgrid.com/v3/sso/integrations?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/sso/integrations"  # noqa

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
async def get_sso_integrations(
    sendgrid_credentials: "SendGridCredentials",
    si: bool = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all SSO integrations tied to your Twilio
    SendGrid account.**  The IDs returned by this endpoint can be used by the
    APIs additional endpoints to modify your SSO integrations.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        si:
            If this parameter is set to `true`, the response will include the
            `completed_integration` field.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/integrations?&si=%s](
    http://api.sendgrid.com/v3/sso/integrations?&si=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/sso/integrations"  # noqa

    responses = {}

    params = {
        "si": si,
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
async def get_sso_integrations_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    si: bool = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve an SSO integration by ID.**  You can
    retrieve the IDs for your configurations from the response provided by the
    'Get All SSO Integrations' endpoint.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        si:
            If this parameter is set to `true`, the response will include the
            `completed_integration` field.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/integrations/{id}?&si=%s](
    http://api.sendgrid.com/v3/sso/integrations/{id}?&si=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/sso/integrations/{id}"  # noqa
    responses = {}

    params = {
        "si": si,
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
async def patch_sso_integrations_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    si: bool = None,
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to modify an exisiting SSO integration.**  You can
    retrieve the IDs for your configurations from the response provided by the
    'Get All SSO Integrations' endpoint.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        si:
            If this parameter is set to `true`, the response will include the
            `completed_integration` field.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/integrations/{id}?&si=%s&body=%s](
    http://api.sendgrid.com/v3/sso/integrations/{id}?&si=%s&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/sso/integrations/{id}"  # noqa
    responses = {}

    params = {
        "si": si,
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
async def delete_sso_integrations_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete an IdP configuration by ID.**  You can
    retrieve the IDs for your configurations from the response provided by the
    'Get All SSO Integrations' endpoint.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/integrations/{id}?](
    http://api.sendgrid.com/v3/sso/integrations/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/sso/integrations/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_sso_teammates(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create an SSO Teammate.**  The email provided for
    this user will also function as the Teammate’s username.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/teammates?&body=%s](
    http://api.sendgrid.com/v3/sso/teammates?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/sso/teammates"  # noqa

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
async def patch_sso_teammates_username(
    username: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to modify an existing SSO Teammate.**  To turn a
    teammate into an admin, the request body should contain the `is_admin` field
    set to `true`. Otherwise, set `is_admin` to false and pass in all the scopes
    that a teammate should have.  Only the parent user and Teammates with admin
    permissions can update another Teammate’s permissions. Admin users can only
    update permissions.

    Args:
        username:
            Username used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/sso/teammates/{username}?&body=%s](
    http://api.sendgrid.com/v3/sso/teammates/{username}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/sso/teammates/{username}"  # noqa
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
