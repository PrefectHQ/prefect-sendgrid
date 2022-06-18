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
async def get_mail_settings(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = None,
    offset: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all mail settings.**  Each
    setting will be returned with an `enabled` status set to `true` or `false`
    and a short description that explains what the setting does.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            The number of settings to return.
        offset:
            Where in the list of results to begin displaying settings.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings?&limit=%s&offset=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings?&limit=%s&offset=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings"  # noqa

    responses = {}

    params = {
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
async def patch_mail_settings_address_whitelist(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current email address whitelist
    settings.**  You can select whether or not this setting should be enabled by
    assigning the `enabled` field a `true` or `false` value.  Passing only the
    `enabled` field to this endpoint will not alter your current `list` of
    whitelist entries. However, any modifications to your `list` of entries will
    overwrite the entire list. For this reason, you must included all existing
    entries you wish to retain in your `list` in addition to any new entries you
    intend to add. To remove one or more `list` entries, pass a `list` with only
    the entries you wish to retain.  You should not add generic domains such as
    `gmail.com` or `yahoo.com`  in your `list` because your emails will not
    honor recipients' unsubscribes. This may cause a legal violation of [CAN-
    SPAM](https://sendgrid.com/docs/glossary/can-spam/) and could damage your
    sending reputation.  The Address Whitelist setting allows you to specify
    email addresses or domains for which mail should never be suppressed.  For
    example, if you own the domain `example.com`, and one or more of your
    recipients use `email@example.com` addresses, placing `example.com` in the
    address whitelist setting instructs Twilio SendGrid to ignore all bounces,
    blocks, and unsubscribes logged for that domain. In other words, all
    bounces, blocks, and unsubscribes will still be sent to `example.com` as if
    they were sent under normal sending conditions.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/address_whitelist?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/address_whitelist?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/address_whitelist"  # noqa

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
async def get_mail_settings_address_whitelist(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current email address whitelist
    settings.**  The Address Whitelist setting allows you to specify email
    addresses or domains for which mail should never be suppressed.  For
    example, if you own the domain `example.com`, and one or more of your
    recipients use `email@example.com` addresses, placing `example.com` in the
    address whitelist setting instructs Twilio SendGrid to ignore all bounces,
    blocks, and unsubscribes logged for that domain. In other words, all
    bounces, blocks, and unsubscribes will still be sent to `example.com` as if
    they were sent under normal sending conditions.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/address_whitelist?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/address_whitelist?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/address_whitelist"  # noqa

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
async def patch_mail_settings_footer(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current Footer mail settings.**  The
    Footer setting will insert a custom footer at the bottom of your text and
    HTML email message bodies.  You can insert your HTML or plain text directly
    using this endpoint, or you can create the footer using the [Mail Settings
    menu in the Twilio SendGrid
    App](https://app.sendgrid.com/settings/mail_settings).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/footer?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/footer?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/footer"  # noqa

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
async def get_mail_settings_footer(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current Footer mail settings.**  The
    Footer setting will insert a custom footer at the bottom of your text and
    HTML email message bodies.  You can insert your HTML or plain text directly
    using the 'Update footer mail settings' endpoint, or you can create the
    footer using the [Mail Settings menu in the Twilio SendGrid
    App](https://app.sendgrid.com/settings/mail_settings).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/footer?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/footer?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/footer"  # noqa

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
async def patch_mail_settings_forward_spam(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current Forward Spam mail settings.**
    Enabling the Forward Spam setting allows you to specify `email` addresses to
    which spam reports will be forwarded. You can set multiple addresses by
    passing this endpoint a comma separated list of emails in a single string.
    ``` {   'email': 'address1@example.com, address2@exapmle.com',   'enabled':
    true } ```  The Forward Spam setting may also be used to receive emails sent
    to `abuse@` and `postmaster@` role addresses if you have authenticated your
    domain.  For example, if you authenticated `example.com` as your root domain
    and set a custom return path of `sub` for that domain, you could turn on
    Forward Spam, and any emails sent to `abuse@sub.example.com` or
    `postmaster@sub.example.com` would be forwarded to the email address you
    entered in the `email` field.  You can authenticate your domain using the
    'Authenticate a domain' endpoint or in the [Sender Authentication section of
    the Twilio SendGrid App](https://app.sendgrid.com/settings/sender_auth). You
    can also configure the Forward Spam mail settings in the [Mail Settings
    section of the Twilio SendGrid
    App](https://app.sendgrid.com/settings/mail_settings).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/forward_spam?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/forward_spam?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/forward_spam"  # noqa

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
async def get_mail_settings_forward_spam(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current Forward Spam mail
    settings.**  Enabling the Forward Spam setting allows you to specify `email`
    addresses to which spam reports will be forwarded. This endpoint returns any
    email address(es) you have set to receive forwarded spam and an `enabled`
    status indicating if the setting is active.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/forward_spam?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/forward_spam?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/forward_spam"  # noqa

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
async def patch_mail_settings_template(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current legacy email template
    settings.**  This setting refers to our original email templates. We
    currently support more fully featured [Dynamic Transactional
    Templates](https://sendgrid.com/docs/ui/sending-email/how-to-send-an-email-
    with-dynamic-transactional-templates/).  The legacy email template setting
    wraps an HTML template around your email content. This can be useful for
    sending out marketing email and/or other HTML formatted messages. For
    instructions on using legacy templates, see how to ['Create and Edit Legacy
    Transactional Templates](https://sendgrid.com/docs/ui/sending-email/create-
    and-edit-legacy-transactional-templates/). For help migrating to our current
    template system, see ['Migrating from Legacy
    Templates'](https://sendgrid.com/docs/ui/sending-email/migrating-from-
    legacy-templates/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/template?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/template?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/template"  # noqa

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
async def get_mail_settings_template(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current legacy email template
    settings.**  This setting refers to our original email templates. We
    currently support more fully featured [Dynamic Transactional
    Templates](https://sendgrid.com/docs/ui/sending-email/how-to-send-an-email-
    with-dynamic-transactional-templates/).  The legacy email template setting
    wraps an HTML template around your email content. This can be useful for
    sending out marketing email and/or other HTML formatted messages. For
    instructions on using legacy templates, see how to ['Create and Edit Legacy
    Transactional Templates](https://sendgrid.com/docs/ui/sending-email/create-
    and-edit-legacy-transactional-templates/). For help migrating to our current
    template system, see ['Migrating from Legacy
    Templates'](https://sendgrid.com/docs/ui/sending-email/migrating-from-
    legacy-templates/).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/template?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/template?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/template"  # noqa

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
async def patch_mail_settings_bounce_purge(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current bounce and purge settings.**
    The Bounce Perge setting allows you to set a schedule that Twilio SendGrid
    will use to automatically delete contacts from your soft and hard bounce
    suppression lists. The schedule is set in full days by assigning the number
    of days, an integer, to the `soft_bounces` and/or `hard_bounces` fields.  A
    hard bounce occurs when an email message has been returned to the sender
    because the recipient's address is invalid. A hard bounce might occur
    because the domain name doesn't exist or because the recipient is unknown.
    A soft bounce occurs when an email message reaches the recipient's mail
    server but is bounced back undelivered before it actually reaches the
    recipient. A soft bounce might occur because the recipient's inbox is full.
    You can also manage this setting in the [Mail Settings section of the Twilio
    SendGrid App](https://app.sendgrid.com/settings/mail_settings). You can
    manage your bounces manually using the [Bounces API](https://sendgrid.api-
    docs.io/v3.0/bounces-api) or the [Bounces menu in the Twilio SendGrid
    App](https://app.sendgrid.com/suppressions/bounces).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/bounce_purge?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/bounce_purge?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/bounce_purge"  # noqa

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
async def get_mail_settings_bounce_purge(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current bounce and purge settings.**
    The Bounce Perge setting allows you to set a schedule that Twilio SendGrid
    will use to automatically delete contacts from your soft and hard bounce
    suppression lists.  A hard bounce occurs when an email message has been
    returned to the sender because the recipient's address is invalid. A hard
    bounce might occur because the domain name doesn't exist or because the
    recipient is unknown.  A soft bounce occurs when an email message reaches
    the recipient's mail server but is bounced back undelivered before it
    actually reaches the recipient. A soft bounce might occur because the
    recipient's inbox is full.  You can also manage this setting in the [Mail
    Settings section of the Twilio SendGrid
    App](https://app.sendgrid.com/settings/mail_settings). You can manage your
    bounces manually using the [Bounces API](https://sendgrid.api-
    docs.io/v3.0/bounces-api) or the [Bounces menu in the Twilio SendGrid
    App](https://app.sendgrid.com/suppressions/bounces).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/bounce_purge?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/bounce_purge?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/bounce_purge"  # noqa

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
async def patch_mail_settings_forward_bounce(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update your current bounce forwarding mail
    settings.**  Enabling the Forward Bounce setting allows you to specify an
    `email` address to which bounce reports will be forwarded.  You can also
    configure the Forward Spam mail settings in the [Mail Settings section of
    the Twilio SendGrid App](https://app.sendgrid.com/settings/mail_settings).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/forward_bounce?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/forward_bounce?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/forward_bounce"  # noqa

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
async def get_mail_settings_forward_bounce(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve your current bounce forwarding mail
    settings.**  Enabling the Forward Bounce setting allows you to specify
    `email` addresses to which bounce reports will be forwarded. This endpoint
    returns the email address you have set to receive forwarded bounces and an
    `enabled` status indicating if the setting is active.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/mail_settings/forward_bounce?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/mail_settings/forward_bounce?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/mail_settings/forward_bounce"  # noqa

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
