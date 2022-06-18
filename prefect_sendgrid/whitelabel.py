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
async def post_whitelabel_links(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new branded link.**  To create the link
    branding, supply the root domain and, optionally, the subdomain — these go
    into separate fields in your request body. The root domain should match your
    FROM email address. If you provide a  subdomain, it must be different from
    the subdomain you used for authenticating your domain.  You can submit this
    request as one of your subusers if you include their ID in the `on-behalf-
    of` header in the request.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/links?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/links"  # noqa

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
async def get_whitelabel_links(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all branded links**.  You can submit this
    request as one of your subusers if you include their ID in the `on-behalf-
    of` header in the request.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            Limits the number of results returned per page.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links?&limit=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/links?&limit=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/links"  # noqa

    responses = {}

    params = {
        "limit": limit,
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
async def post_whitelabel_links_id_validate(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to validate a branded link.**  You can submit this
    request as one of your subusers if you include their ID in the `on-behalf-
    of` header in the request.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links/{id}/validate?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/links/{id}/validate?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/links/{id}/validate"  # noqa
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
async def post_whitelabel_links_link_id_subuser(
    link_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to associate a branded link with a subuser account.**
    Link branding can be associated with subusers from the parent account. This
    functionality allows subusers to send mail using their parent's link
    branding. To associate link branding, the parent account must first create a
    branded link and validate it. The parent may then associate that branded
    link with a subuser via the API or the [Subuser Management page of the
    Twilio SendGrid App](https://app.sendgrid.com/settings/subusers).

    Args:
        link_id:
            Link id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links/{link_id}/subuser?&body=%s](
    http://api.sendgrid.com/v3/whitelabel/links/{link_id}/subuser?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/links/{link_id}/subuser"  # noqa
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
async def get_whitelabel_links_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a specific branded link by providing its
    ID.**  You can submit this request as one of your subusers if you include
    their ID in the `on-behalf-of` header in the request.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links/{id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/links/{id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/links/{id}"  # noqa
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
async def patch_whitelabel_links_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update a specific branded link. You can use this
    endpoint to change a branded link's default status.**  You can submit this
    request as one of your subusers if you include their ID in the `on-behalf-
    of` header in the request.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links/{id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/links/{id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/links/{id}"  # noqa
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
async def delete_whitelabel_links_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a branded link.**  Your request will
    receive a response with a 204 status code if the deletion was successful.
    The call does not return the link's details, so if you wish to record these
    make sure you call the  'Retrieve a branded link' endpoint *before* you
    request its deletion.  You can submit this request as one of your subusers
    if you include their ID in the `on-behalf-of` header in the request.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links/{id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/links/{id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/links/{id}"  # noqa
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
async def get_whitelabel_links_default(
    sendgrid_credentials: "SendGridCredentials",
    domain: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the default branded link.**  The default
    branded link is the actual URL to be used when sending messages. If you have
    more than one branded link, the default is determined by the following
    order:  * The validated branded link marked as `default` (set when you call
    the 'Create a branded link' endpoint or by calling the 'Update a branded
    link' endpoint on an existing link) * Legacy branded links (migrated from
    the whitelabel wizard) * Default SendGrid-branded links (i.e.,
    `100.ct.sendgrid.net`)  You can submit this request as one of your subusers
    if you include their ID in the `on-behalf-of` header in the request.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        domain:
            The domain to match against when finding the default branded link.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links/default?&domain=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/links/default?&domain=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/links/default"  # noqa

    responses = {}

    params = {
        "domain": domain,
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
async def get_whitelabel_links_subuser(
    username: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the branded link associated with a
    subuser.**  Link branding can be associated with subusers from the parent
    account. This functionality allows subusers to send mail using their
    parent's link branding. To associate link branding, the parent account must
    first create a branded link and then validate it. The parent may then
    associate that branded link with a subuser via the API or the [Subuser
    Management page of the Twilio SendGrid
    App](https://app.sendgrid.com/settings/subusers).

    Args:
        username:
            The username of the subuser to retrieve associated branded links for.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links/subuser?&username=%s](
    http://api.sendgrid.com/v3/whitelabel/links/subuser?&username=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/links/subuser"  # noqa

    responses = {}

    params = {
        "username": username,
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
async def delete_whitelabel_links_subuser(
    username: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to take a branded link away from a subuser.**  Link
    branding can be associated with subusers from the parent account. This
    functionality allows subusers to send mail using their parent's link
    branding. To associate link branding, the parent account must first create a
    branded link and validate it. The parent may then associate that branded
    link with a subuser via the API or the [Subuser Management page of the
    Twilio SendGrid App](https://app.sendgrid.com/settings/subusers).  Your
    request will receive a response with a 204 status code if the disassociation
    was successful.

    Args:
        username:
            The username of the subuser account that you want to disassociate a
            branded link from.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/links/subuser?&username=%s](
    http://api.sendgrid.com/v3/whitelabel/links/subuser?&username=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/links/subuser"  # noqa

    responses = {}

    params = {
        "username": username,
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
async def post_whitelabel_ips(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to set up reverse DNS.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/ips?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/ips?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/ips"  # noqa

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
async def get_whitelabel_ips(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = None,
    offset: int = None,
    ip: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of the Reverse DNS records created by
    this account.**  You may include a search key by using the `ip` query string
    parameter. This enables you to perform a prefix search for a given IP
    segment (e.g., `?ip='192.'`).  Use the `limit` query string parameter to
    reduce the number of records returned. All records will be returned if you
    have fewer records than the specified limit.  The `offset` query string
    parameter allows you to specify a non-zero index from which records will be
    returned. For example, if you have ten records, `?offset=5` will return the
    last five records (at indexes 5 through 9). The list starts at index zero.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            The maximum number of results to retrieve.
        offset:
            The point in the list of results to begin retrieving IP addresses from.
        ip:
            The IP address segment that you'd like to use in a prefix search.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/ips?&limit=%s&offset=%s&ip=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/ips?&limit=%s&offset=%s&ip=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/ips"  # noqa

    responses = {}

    params = {
        "limit": limit,
        "offset": offset,
        "ip": ip,
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
async def post_whitelabel_ips_id_validate(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to validate a reverse DNS record.**  Always check the
    `valid` property of the response’s `validation_results.a_record` object.
    This field will indicate whether it was possible to validate the reverse DNS
    record. If the `validation_results.a_record.valid` is `false`, this
    indicates only that Twilio SendGrid could not determine the validity your
    reverse DNS record — it may still be valid.  If validity couldn’t be
    determined, you can check the value of `validation_results.a_record.reason`
    to find out why.  You can retrieve the IDs associated with all your reverse
    DNS records using the 'Retrieve all reverse DNS records' endpoint.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/ips/{id}/validate?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/ips/{id}/validate?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 404 | Unexpected error in API call. See HTTP response body for details. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/ips/{id}/validate"  # noqa
    responses = {
        404: "Unexpected error in API call. See HTTP response body for details.",  # noqa
    }

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
async def get_whitelabel_ips_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a reverse DNS record.**  You can retrieve
    the IDs associated with all your reverse DNS records using the 'Retrieve all
    reverse DNS records' endpoint.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/ips/{id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/ips/{id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/ips/{id}"  # noqa
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
async def delete_whitelabel_ips_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a reverse DNS record.**  A call to this
    endpoint will respond with a 204 status code if the deletion was successful.
    You can retrieve the IDs associated with all your reverse DNS records using
    the 'Retrieve all reverse DNS records' endpoint.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/ips/{id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/ips/{id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/ips/{id}"  # noqa
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
async def post_whitelabel_dns_email(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint is used to share DNS records with a colleagues**  Use this
    endpoint to send SendGrid-generated DNS record information to a co-worker so
    they can enter it into your DNS provider to validate your domain and link
    branding.
    What type of records are sent will depend on whether you have chosen
    Automated Security or not. When using Automated Security, SendGrid provides
    you with three CNAME records. If you turn Automated Security off, you are
    instead given TXT and MX records.  If you pass a `link_id` to this endpoint,
    the generated email will supply the DNS records necessary to complete [Link
    Branding](https://sendgrid.com/docs/ui/account-and-settings/how-to-set-up-
    link-branding/) setup. If you pass a `domain_id` to this endpoint, the
    generated email will supply the DNS records needed to complete [Domain
    Authentication](https://sendgrid.com/docs/ui/account-and-settings/how-to-
    set-up-domain-authentication/). Passing both IDs will generate an email with
    the records needed to complete both setup steps.  You can retrieve all your
    domain IDs from the returned `id` fields for each domain using the 'List all
    authenticated domains' endpoint. You can retrieve all of your link IDs using
    the 'Retrieve all branded links' endpoint.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/dns/email?&body=%s](
    http://api.sendgrid.com/v3/whitelabel/dns/email?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/dns/email"  # noqa

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
async def get_whitelabel_domains(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = None,
    offset: int = None,
    exclude_subusers: bool = None,
    username: str = None,
    domain: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all domains you have
    authenticated.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            Number of domains to return.
        offset:
            Paging offset.
        exclude_subusers:
            Exclude subuser domains from the result.
        username:
            The username associated with an authenticated domain.
        domain:
            Search for authenticated domains.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains?&limit=%s&offset=%s&exclude_subusers=%s&username=%s&domain=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/domains?&limit=%s&offset=%s&exclude_subusers=%s&username=%s&domain=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/domains"  # noqa

    responses = {}

    params = {
        "limit": limit,
        "offset": offset,
        "exclude_subusers": exclude_subusers,
        "username": username,
        "domain": domain,
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
async def post_whitelabel_domains(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to authenticate a domain.**  If you are
    authenticating a domain for a subuser, you have two options: 1. Use the
    'username' parameter. This allows you to authenticate a domain on behalf of
    your subuser. This means the subuser is able to see and modify the
    authenticated domain. 2. Use the Association workflow (see Associate Domain
    section). This allows you to authenticate a domain created by the parent to
    a subuser. This means the subuser will default to the assigned domain, but
    will not be able to see or modify that authenticated domain. However, if the
    subuser authenticates their own domain it will overwrite the assigned
    domain.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/domains?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/domains"  # noqa

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
async def get_whitelabel_domains_domain_id(
    domain_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a specific authenticated domain.**.

    Args:
        domain_id:
            Domain id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}"  # noqa
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
async def patch_whitelabel_domains_domain_id(
    domain_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update the settings for an authenticated domain.**.

    Args:
        domain_id:
            Domain id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}"  # noqa
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
async def delete_whitelabel_domains_domain_id(
    domain_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete an authenticated domain.**.

    Args:
        domain_id:
            Domain id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}"  # noqa
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
async def get_whitelabel_domains_default(
    sendgrid_credentials: "SendGridCredentials",
    domain: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the default authentication for a
    domain.**  When creating or updating a domain authentication, you can set
    the domain as a default. The default domain will be used to send all mail.
    If you have multiple authenticated domains, the authenticated domain
    matching the domain of the From address will be used, and the default will
    be overridden.  This endpoint will return a default domain and its details
    only if a default is set. You are not required to set a default. If you do
    not set a default domain, this endpoint will return general information
    about your domain authentication status.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        domain:
            The domain to find a default authentication.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/default?&domain=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/default?&domain=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/domains/default"  # noqa

    responses = {}

    params = {
        "domain": domain,
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
async def post_whitelabel_domains_id_ips(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to add an IP address to an authenticated domain.**.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/{id}/ips?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/{id}/ips?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/domains/{id}/ips"  # noqa
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
async def delete_whitelabel_domains_id_ips_ip(
    id: str,
    ip: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove an IP address from that domain's
    authentication.**.

    Args:
        id:
            Id used in formatting the endpoint URL.
        ip:
            Ip used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/{id}/ips/{ip}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/{id}/ips/{ip}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/domains/{id}/ips/{ip}"  # noqa
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
async def post_whitelabel_domains_id_validate(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to validate an authenticated domain. If it fails, it
    will return an error message describing why the domain could not be
    validated.**.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/{id}/validate?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/{id}/validate?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/domains/{id}/validate"  # noqa
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
async def get_whitelabel_domains_subuser(
    username: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of the authenticated domains that
    have been assigned to a specific subuser.**  Authenticated domains can be
    associated with (i.e. assigned to) subusers from a parent account. This
    functionality allows subusers to send mail using their parent's domain
    authentication. To associate a authenticated domain with a subuser, the
    parent account must first authenticate and validate the domain. The the
    parent may then associate the authenticated domain via the subuser
    management tools.

    Args:
        username:
            Username for the subuser to find associated authenticated domain.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/subuser?&username=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/subuser?&username=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/domains/subuser"  # noqa

    responses = {}

    params = {
        "username": username,
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
async def delete_whitelabel_domains_subuser(
    sendgrid_credentials: "SendGridCredentials",
    username: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to disassociate a specific authenticated domain from
    a subuser.**  Authenticated domains can be associated with (i.e. assigned
    to) subusers from a parent account. This functionality allows subusers to
    send mail using their parent's domain authentication. To associate a
    authenticated domain with a subuser, the parent account must first
    authenticate and validate the domain. The the parent may then associate the
    authenticated domain via the subuser management tools.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        username:
            Username for the subuser to find associated authenticated domain.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/subuser?&username=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/subuser?&username=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/whitelabel/domains/subuser"  # noqa

    responses = {}

    params = {
        "username": username,
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
async def post_whitelabel_domains_domain_id_subuser(
    domain_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to associate a specific authenticated domain with a
    subuser.**  Authenticated domains can be associated with (i.e. assigned to)
    subusers from a parent account. This functionality allows subusers to send
    mail using their parent's domain authentication. To associate a
    authenticated domain with a subuser, the parent account must first
    authenticate and validate the domain. The the parent may then associate the
    authenticated domain via the subuser management tools.

    Args:
        domain_id:
            Domain id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}/subuser?&body=%s](
    http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}/subuser?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/whitelabel/domains/{domain_id}/subuser"  # noqa
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
