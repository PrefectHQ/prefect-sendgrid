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
async def post_contactdb_lists(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a list for your recipients.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'name' : 'Returned if list name is a duplicate of an existing list or segment'    'name' : 'Returned if list name is not a string' '' : 'Returned if request    body is invalid JSON'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/lists"  # noqa

    responses = {
        400: "'name' : 'Returned if list name is a duplicate of an existing list or segment'    'name' : 'Returned if list name is not a string' '' : 'Returned if request    body is invalid JSON'.",  # noqa
    }

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
async def get_contactdb_lists(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of your recipient lists. If you don't
    have any lists, an empty array will be returned.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/lists"  # noqa

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
async def delete_contactdb_lists(
    sendgrid_credentials: "SendGridCredentials",
    body: list = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete multiple recipient lists.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'id' : 'Returned if all list ids are not valid'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/lists"  # noqa

    responses = {
        400: "'id' : 'Returned if all list ids are not valid'.",  # noqa
    }

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
async def get_contactdb_lists_list_id(
    list_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a single recipient list.**.

    Args:
        list_id:
            List id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists/{list_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists/{list_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'list_id' : 'Returned if list_id is not valid'. |
    | 404 | 'list_id' : 'Returned if list_id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/lists/{list_id}"  # noqa
    responses = {
        400: "'list_id' : 'Returned if list_id is not valid'.",  # noqa
        404: "'list_id' : 'Returned if list_id does not exist'.",  # noqa
    }

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
async def patch_contactdb_lists_list_id(
    list_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update the name of one of your recipient lists.**.

    Args:
        list_id:
            List id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists/{list_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists/{list_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'name' : 'Returned if list name is a duplicate of existing list or segment'    'name' : 'Returned if list name is invalid or not provided' 'list_id' :    'Returned if list_id is not valid' '' : 'Returned if request body is invalid    JSON'. |
    | 404 | 'list_id' : 'Returned if list_id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/lists/{list_id}"  # noqa
    responses = {
        400: "'name' : 'Returned if list name is a duplicate of existing list or segment'    'name' : 'Returned if list name is invalid or not provided' 'list_id' :    'Returned if list_id is not valid' '' : 'Returned if request body is invalid    JSON'.",  # noqa
        404: "'list_id' : 'Returned if list_id does not exist'.",  # noqa
    }

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
async def delete_contactdb_lists_list_id(
    list_id: str,
    sendgrid_credentials: "SendGridCredentials",
    delete_contacts: bool = None,
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a specific recipient list with the given
    ID.**.

    Args:
        list_id:
            List id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        delete_contacts:
            Adds the ability to delete all contacts on the list in addition to
            deleting the list.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists/{list_id}?&delete_contacts=%s&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists/{list_id}?&delete_contacts=%s&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'list_id' : 'Returned if list_id is not valid' 'delete_contacts' : 'Returned if    delete_contacts is not valid'. |
    | 404 | 'list_id' : 'Returned if list_id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/lists/{list_id}"  # noqa
    responses = {
        400: "'list_id' : 'Returned if list_id is not valid' 'delete_contacts' : 'Returned if    delete_contacts is not valid'.",  # noqa
        404: "'list_id' : 'Returned if list_id does not exist'.",  # noqa
    }

    params = {
        "delete_contacts": delete_contacts,
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
async def get_contactdb_lists_list_id_recipients(
    list_id: str,
    sendgrid_credentials: "SendGridCredentials",
    page: int = None,
    page_size: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all recipients on the list with the given
    ID.**.

    Args:
        list_id:
            List id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        page:
            Page index of first recipient to return (must be a positive integer).
        page_size:
            Number of recipients to return at a time (must be a positive integer
            between 1 and 1000).
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients?&page=%s&page_size=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients?&page=%s&page_size=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'list_id' : 'Returned if list_id is not a valid integer' 'page' : 'Returned if    page is not a valid integer' 'page' : 'Returned if page is less than 1'    'page_size' : 'Returned if page_size is not a valid integer' 'page_size' :    'Returned if page_size is less than 1 or greater than 1000'. |
    | 404 | 'list_id' : 'Returned if list_id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients"  # noqa
    responses = {
        400: "'list_id' : 'Returned if list_id is not a valid integer' 'page' : 'Returned if    page is not a valid integer' 'page' : 'Returned if page is less than 1'    'page_size' : 'Returned if page_size is not a valid integer' 'page_size' :    'Returned if page_size is less than 1 or greater than 1000'.",  # noqa
        404: "'list_id' : 'Returned if list_id does not exist'.",  # noqa
    }

    params = {
        "page": page,
        "page_size": page_size,
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
async def post_contactdb_lists_list_id_recipients(
    list_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: list = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to add multiple recipients to a list.**  Adds
    existing recipients to a list, passing in the recipient IDs to add.
    Recipient IDs should be passed exactly as they are returned from recipient
    endpoints.

    Args:
        list_id:
            List id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'list_id' : 'Returned if list_id is not a valid integer' '' : 'Returned if no    valid recipient ids were passed' '' : 'Returned if no recipients were added'    '' : 'Returned if request body is invalid JSON'. |
    | 404 | 'list_id': 'Returned if list_id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients"  # noqa
    responses = {
        400: "'list_id' : 'Returned if list_id is not a valid integer' '' : 'Returned if no    valid recipient ids were passed' '' : 'Returned if no recipients were added'    '' : 'Returned if request body is invalid JSON'.",  # noqa
        404: "'list_id': 'Returned if list_id does not exist'.",  # noqa
    }

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
async def post_contactdb_lists_list_id_recipients_recipient_id(
    list_id: str,
    recipient_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to add a single recipient to a list.**.

    Args:
        list_id:
            List id used in formatting the endpoint URL.
        recipient_id:
            Recipient id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients/{recipient_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients/{recipient_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'list_id' : 'Returned if list_id is invalid' 'recipient_id' : 'Returned if    recipient_id is invalid'. |
    | 404 | 'list_id' : 'Returned if list_id does not exist' 'recipient_id' : 'Returned if    recipient_id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients/{recipient_id}"  # noqa
    responses = {
        400: "'list_id' : 'Returned if list_id is invalid' 'recipient_id' : 'Returned if    recipient_id is invalid'.",  # noqa
        404: "'list_id' : 'Returned if list_id does not exist' 'recipient_id' : 'Returned if    recipient_id does not exist'.",  # noqa
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
async def delete_contactdb_lists_list_id_recipients_recipient_id(
    list_id: str,
    recipient_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a single recipient from a list.**.

    Args:
        list_id:
            List id used in formatting the endpoint URL.
        recipient_id:
            Recipient id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients/{recipient_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients/{recipient_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'list_id' : 'Returned if list_id is not valid' 'recipient_id' : 'Returned if    recipient_id is not valid'. |
    | 404 | 'list_id' : 'Returned if list_id does not exist' 'recipient_id' : 'Returned if    recipient_id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/lists/{list_id}/recipients/{recipient_id}"  # noqa
    responses = {
        400: "'list_id' : 'Returned if list_id is not valid' 'recipient_id' : 'Returned if    recipient_id is not valid'.",  # noqa
        404: "'list_id' : 'Returned if list_id does not exist' 'recipient_id' : 'Returned if    recipient_id does not exist'.",  # noqa
    }

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
async def post_contactdb_recipients(
    sendgrid_credentials: "SendGridCredentials",
    body: list = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to add a Marketing Campaigns recipient.**  You can
    add custom field data as a parameter on this endpoint. We have provided an
    example using some of the default custom fields SendGrid provides.  The rate
    limit is three requests every 2 seconds. You can upload 1000  contacts per
    request. So the maximum upload rate is 1500 recipients per second.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | '' : 'Returned if request body is not valid json'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/recipients"  # noqa

    responses = {
        400: "'' : 'Returned if request body is not valid json'.",  # noqa
    }

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
async def patch_contactdb_recipients(
    sendgrid_credentials: "SendGridCredentials",
    body: list = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update one or more recipients.**  The body of an
    API call to this endpoint must include an array of one or more recipient
    objects.  It is of note that you can add custom field data as parameters on
    recipient objects. We have provided an example using some of the default
    custom fields SendGrid provides.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | '' : 'Returned if request body is not valid json'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/recipients"  # noqa

    responses = {
        400: "'' : 'Returned if request body is not valid json'.",  # noqa
    }

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
async def delete_contactdb_recipients(
    sendgrid_credentials: "SendGridCredentials",
    body: list = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to deletes one or more recipients.**  The body of an
    API call to this endpoint must include an array of recipient IDs of the
    recipients you want to delete.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | '' : 'Returned if no recipients are deleted' '' : 'Returned if all of the    provided recipient ids are invalid' '' : 'Returned if request body is not    valid json'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/recipients"  # noqa

    responses = {
        400: "'' : 'Returned if no recipients are deleted' '' : 'Returned if all of the    provided recipient ids are invalid' '' : 'Returned if request body is not    valid json'.",  # noqa
    }

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
async def get_contactdb_recipients(
    sendgrid_credentials: "SendGridCredentials",
    page: int = None,
    page_size: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of your Marketing Campaigns
    recipients.**  Batch deletion of a page makes it possible to receive an
    empty page of recipients before reaching the end of the list of recipients.
    To avoid this issue; iterate over pages until a 404 is retrieved.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        page:
            Page index of first recipients to return (must be a positive integer).
        page_size:
            Number of recipients to return at a time (must be a positive integer
            between 1 and 1000).
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients?&page=%s&page_size=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients?&page=%s&page_size=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'page' : 'Returned if page is not a valid integer' 'page' : 'Returned if page is    less than 1' 'page_size' : 'Returned if page_size is not a valid integer'    'page_size' : 'Returned if page_size is less than 1 or greater than 1000'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/recipients"  # noqa

    responses = {
        400: "'page' : 'Returned if page is not a valid integer' 'page' : 'Returned if page is    less than 1' 'page_size' : 'Returned if page_size is not a valid integer'    'page_size' : 'Returned if page_size is less than 1 or greater than 1000'.",  # noqa
    }

    params = {
        "page": page,
        "page_size": page_size,
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
async def get_contactdb_status(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to check the upload status of a Marketing Campaigns
    recipient.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/status?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/status?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/status"  # noqa

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
async def get_contactdb_recipients_recipient_id(
    recipient_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a single recipient by ID from your
    contact database.**.

    Args:
        recipient_id:
            Recipient id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients/{recipient_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients/{recipient_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'recipient_id' : 'Returned if recipient_id is not valid'. |
    | 404 | 'recipient_id' : 'Returned if record for recipient id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/recipients/{recipient_id}"  # noqa
    responses = {
        400: "'recipient_id' : 'Returned if recipient_id is not valid'.",  # noqa
        404: "'recipient_id' : 'Returned if record for recipient id does not exist'.",  # noqa
    }

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
async def delete_contactdb_recipients_recipient_id(
    recipient_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a single recipient with the given ID from
    your contact database.**  > Use this to permanently delete your recipients
    from all of your contact lists and all segments if required by applicable
    law.

    Args:
        recipient_id:
            Recipient id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients/{recipient_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients/{recipient_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'recipient_id' : 'Returned if recipient_id is not valid'. |
    | 404 | 'recipient_id' : 'Returned if record for recipient id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/recipients/{recipient_id}"  # noqa
    responses = {
        400: "'recipient_id' : 'Returned if recipient_id is not valid'.",  # noqa
        404: "'recipient_id' : 'Returned if record for recipient id does not exist'.",  # noqa
    }

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
async def get_contactdb_recipients_recipient_id_lists(
    recipient_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the lists that a given recipient belongs
    to.**  Each recipient can be on many lists. This endpoint gives you all of
    the lists that any one recipient has been added to.

    Args:
        recipient_id:
            Recipient id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients/{recipient_id}/lists?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients/{recipient_id}/lists?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'recipient_id' : 'Returned if recipient_id is not valid'. |
    | 404 | 'recipient_id' : 'Returned if record for the recipient id does not exist'. |
    """  # noqa
    url = (
        f"http://api.sendgrid.com/v3/contactdb/recipients/{recipient_id}/lists"  # noqa
    )
    responses = {
        400: "'recipient_id' : 'Returned if recipient_id is not valid'.",  # noqa
        404: "'recipient_id' : 'Returned if record for the recipient id does not exist'.",  # noqa
    }

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
async def get_contactdb_recipients_billable_count(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the number of Marketing Campaigns
    recipients that you will be billed for.**  You are billed for marketing
    campaigns based on the highest number of recipients you have had in your
    account at one time. This endpoint will allow you to know the current
    billable count value.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients/billable_count?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients/billable_count?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/recipients/billable_count"  # noqa

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
async def get_contactdb_recipients_count(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the total number of Marketing Campaigns
    recipients.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients/count?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients/count?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/recipients/count"  # noqa

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
async def get_contactdb_recipients_search(
    sendgrid_credentials: "SendGridCredentials",
    _field_name: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to perform a search on all of your Marketing
    Campaigns recipients.**  field_name:  * is a variable that is substituted
    for your actual custom field name from your recipient. * Text fields must be
    url-encoded. Date fields are searchable only by unix timestamp (e.g.
    2/2/2015 becomes 1422835200) * If field_name is a 'reserved' date field,
    such as created_at or updated_at, the system will internally convert your
    epoch time to a date range encompassing the entire day. For example, an
    epoch time of 1422835600 converts to Mon, 02 Feb 2015 00:06:40 GMT, but
    internally the system will search from Mon, 02 Feb 2015 00:00:00 GMT through
    Mon, 02 Feb 2015 23:59:59 GMT.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        _field_name:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients/search?&_field_name=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/recipients/search?&_field_name=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | '' : 'Returned if no search params are specified' 'field' : 'Returned if the    provided field is invalid or does not exist'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/recipients/search"  # noqa

    responses = {
        400: "'' : 'Returned if no search params are specified' 'field' : 'Returned if the    provided field is invalid or does not exist'.",  # noqa
    }

    params = {
        "_field_name": _field_name,
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
async def post_contactdb_recipients_search(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    <p>   Search using segment conditions without actually creating a segment.
    Body contains a JSON object with <code>conditions</code>, a list of
    conditions as described below, and an optional <code>list_id</code>, which
    is a valid list ID for a list to limit the search on. </p>  <p>   Valid
    operators for create and update depend on the type of the field for which
    you are searching. </p>  <ul>   <li>Dates:     <ul>       <li>'eq', 'ne',
    'lt' (before), 'gt' (after)         <ul>           <li>You may use
    MM/DD/YYYY for day granularity or an epoch for second granularity.</li>
    </ul>       </li>       <li>'empty', 'not_empty'</li>       <li>'is within'
    <ul>           <li>You may use an <a
    href='https://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a> or
    the
    of days.</li>         </ul>       </li>     </ul>   </li>   <li>Text:
    'contains', 'eq' (is - matches the full field), 'ne' (is not - matches any
    field where the entire field is not the condition value), 'empty',
    'not_empty'</li>   <li>Numbers: 'eq', 'lt', 'gt', 'empty', 'not_empty'</li>
    <li>Email Clicks and Opens: 'eq' (opened), 'ne' (not opened)</li> </ul>  <p>
    Field values must all be a string. </p>  <p>   Search conditions using 'eq'
    or 'ne' for email clicks and opens should provide a 'field' of either
    <code>clicks.campaign_identifier</code> or
    <code>opens.campaign_identifier</code>.   The condition value should be a
    string containing the id of a completed campaign. </p>  <p>   Search
    conditions list may contain multiple conditions, joined by an 'and' or 'or'
    in the 'and_or' field.   The first condition in the conditions list must
    have an empty 'and_or', and subsequent conditions must all specify an
    'and_or'. </p>.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/recipients/search?&body=%s](
    http://api.sendgrid.com/v3/contactdb/recipients/search?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/recipients/search"  # noqa

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
async def post_contactdb_custom_fields(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a custom field.**  **You can create up to
    120 custom fields.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/custom_fields?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/custom_fields?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | '' : 'Returned if request body is invalid JSON' 'type' : 'Returned if custom    field type is invalid or not provided' 'name' : 'Returned if custom field    name is not provided'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/custom_fields"  # noqa

    responses = {
        400: "'' : 'Returned if request body is invalid JSON' 'type' : 'Returned if custom    field type is invalid or not provided' 'name' : 'Returned if custom field    name is not provided'.",  # noqa
    }

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
async def get_contactdb_custom_fields(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all custom fields.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/custom_fields?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/custom_fields?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/custom_fields"  # noqa

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
async def get_contactdb_custom_fields_custom_field_id(
    custom_field_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a custom field by ID.**.

    Args:
        custom_field_id:
            Custom field id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/custom_fields/{custom_field_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/custom_fields/{custom_field_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 404 | 'custom_field_id' : 'Returned if custom_field_id does not exist'. |
    """  # noqa
    url = (
        f"http://api.sendgrid.com/v3/contactdb/custom_fields/{custom_field_id}"  # noqa
    )
    responses = {
        404: "'custom_field_id' : 'Returned if custom_field_id does not exist'.",  # noqa
    }

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
async def delete_contactdb_custom_fields_custom_field_id(
    custom_field_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a custom field by ID.**.

    Args:
        custom_field_id:
            Custom field id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/custom_fields/{custom_field_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/custom_fields/{custom_field_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'id' : 'Returned if custom_field_id is not valid'. |
    | 404 | 'custom_field_id' : 'Returned if custom_field_id does not exist'. |
    """  # noqa
    url = (
        f"http://api.sendgrid.com/v3/contactdb/custom_fields/{custom_field_id}"  # noqa
    )
    responses = {
        400: "'id' : 'Returned if custom_field_id is not valid'.",  # noqa
        404: "'custom_field_id' : 'Returned if custom_field_id does not exist'.",  # noqa
    }

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
async def get_contactdb_reserved_fields(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to list all fields that are reserved and can't be
    used for custom field names.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/reserved_fields?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/reserved_fields?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/reserved_fields"  # noqa

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
async def post_contactdb_segments(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new segment.**     Valid operators for
    create and update depend on the type of the field for which you are
    searching.  **Dates** - 'eq', 'ne', 'lt' (before), 'gt' (after)     - You
    may use MM/DD/YYYY for day granularity or an epoch for second granularity. -
    'empty', 'not_empty' - 'is within'     - You may use an [ISO 8601 date
    format](https://en.wikipedia.org/wiki/ISO_8601) or the
    of days.  **Text** - 'contains' - 'eq' (is/equals - matches the full field)
    - 'ne' (is not/not equals - matches any field where the entire field is not
    the condition value) - 'empty' - 'not_empty'  **Numbers** - 'eq' (is/equals)
    - 'lt' (is less than) - 'gt' (is greater than) - 'empty' - 'not_empty'
    **Email Clicks and Opens** - 'eq' (opened) - 'ne' (not opened)  All field
    values must be a string.   Conditions using 'eq' or 'ne' for email clicks
    and opens should provide a 'field' of either `clicks.campaign_identifier` or
    `opens.campaign_identifier`. The condition value should be a string
    containing the id of a completed campaign.   The conditions list may contain
    multiple conditions, joined by an 'and' or 'or' in the 'and_or' field.  The
    first condition in the conditions list must have an empty 'and_or', and
    subsequent conditions must all specify an 'and_or'.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/segments?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/segments?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'name' : 'Returned if the name is not valid' 'list_id' : 'Returned if the    list_id is not valid' 'and_or' : 'Returned if and_or and set value is not    passed into the request body' 'and_or' : 'Returned if and_or is set on the    only condition passed' 'and_or' : 'Returned if and_or is set on all    conditions' 'and_or' : 'Returned if and_or is not set on more than one    condition and less than all conditions' 'operator' : 'Returned if operator    and set value is not passed into the request body' 'value' : 'Returned if    value and set value is not passed into the request body' 'field' : 'Returned    if field and set value is not passed into the request body' '' : 'Returned    if request body is not valid json' '' : 'Returned if invalid value is passed    into one of the request body parameters'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/segments"  # noqa

    responses = {
        400: "'name' : 'Returned if the name is not valid' 'list_id' : 'Returned if the    list_id is not valid' 'and_or' : 'Returned if and_or and set value is not    passed into the request body' 'and_or' : 'Returned if and_or is set on the    only condition passed' 'and_or' : 'Returned if and_or is set on all    conditions' 'and_or' : 'Returned if and_or is not set on more than one    condition and less than all conditions' 'operator' : 'Returned if operator    and set value is not passed into the request body' 'value' : 'Returned if    value and set value is not passed into the request body' 'field' : 'Returned    if field and set value is not passed into the request body' '' : 'Returned    if request body is not valid json' '' : 'Returned if invalid value is passed    into one of the request body parameters'.",  # noqa
    }

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
async def get_contactdb_segments(
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of your segments.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/segments?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/segments?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/contactdb/segments"  # noqa

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
async def get_contactdb_segments_segment_id(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a single segment with the given ID.**.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/segments/{segment_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/segments/{segment_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'segment_id' : 'Returned if segment_id is not valid'. |
    | 404 | 'segment_id' : 'Returned if segment_id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/segments/{segment_id}"  # noqa
    responses = {
        400: "'segment_id' : 'Returned if segment_id is not valid'.",  # noqa
        404: "'segment_id' : 'Returned if segment_id does not exist'.",  # noqa
    }

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
async def patch_contactdb_segments_segment_id(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update a segment.**.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/segments/{segment_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/segments/{segment_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/segments/{segment_id}"  # noqa
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
async def delete_contactdb_segments_segment_id(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
    delete_contacts: bool = None,
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a segment from your recipients database.**
    You also have the option to delete all the contacts from your Marketing
    Campaigns recipient database who were in this segment.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        delete_contacts:
            True to delete all contacts matching the segment in addition to deleting
            the segment.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/segments/{segment_id}?&delete_contacts=%s&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/segments/{segment_id}?&delete_contacts=%s&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'segment_id' : 'Returned if segment_id is not valid' 'delete_contacts' :    'Returned if delete_contacts is not a valid boolean'. |
    | 404 | 'segment_id' : 'Returned if segment_id does not exist'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/contactdb/segments/{segment_id}"  # noqa
    responses = {
        400: "'segment_id' : 'Returned if segment_id is not valid' 'delete_contacts' :    'Returned if delete_contacts is not a valid boolean'.",  # noqa
        404: "'segment_id' : 'Returned if segment_id does not exist'.",  # noqa
    }

    params = {
        "delete_contacts": delete_contacts,
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
async def get_contactdb_segments_segment_id_recipients(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
    page: int = None,
    page_size: int = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all of the recipients in a segment with
    the given ID.**.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        page:

        page_size:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/contactdb/segments/{segment_id}/recipients?&page=%s&page_size=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/contactdb/segments/{segment_id}/recipients?&page=%s&page_size=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'page' : 'Returned if page is not a valid integer' 'page' : 'Returned if page is    less than 1' 'page_size' : 'Returned if page_size is not a valid integer'. |
    | 404 | 'segment_id' : 'Returned if segment_id is not valid' 'segment_id' : 'Returned if    segment_id does not exist'. |
    """  # noqa
    url = (
        f"http://api.sendgrid.com/v3/contactdb/segments/{segment_id}/recipients"  # noqa
    )
    responses = {
        400: "'page' : 'Returned if page is not a valid integer' 'page' : 'Returned if page is    less than 1' 'page_size' : 'Returned if page_size is not a valid integer'.",  # noqa
        404: "'segment_id' : 'Returned if segment_id is not valid' 'segment_id' : 'Returned if    segment_id does not exist'.",  # noqa
    }

    params = {
        "page": page,
        "page_size": page_size,
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
