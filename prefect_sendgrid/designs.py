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
async def post_designs_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to duplicate one of your existing designs**.
    Modifying an existing design is often the easiest way to create something
    new.  You are not required to pass any data in the body of a request to this
    endpoint. If you choose to leave the `name` field blank, your duplicate will
    be assigned the name of the design it was copied from with the text
    'Duplicate: ' prepended to it. This name change is only a convenience, as
    the duplicate will be assigned a unique ID that differentiates it from your
    other designs.  You can modify your duplicate’s name at the time of creation
    by passing an updated value to the `name` field when making the initial
    request. More on retrieving design IDs can be found below.

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
    [http://api.sendgrid.com/v3/designs/{id}?&body=%s](
    http://api.sendgrid.com/v3/designs/{id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/designs/{id}"  # noqa
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
async def get_designs_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a single design**.  A GET request to
    `/designs/{id}` will retrieve details about a specific design in your Design
    Library.  This endpoint is valuable when retrieving information stored in a
    field that you wish to update using a PATCH request.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/designs/{id}?](
    http://api.sendgrid.com/v3/designs/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/designs/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def patch_designs_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to edit a design**.  The Design API supports PATCH
    requests, which allow you to make partial updates to a single design.
    Passing data to a specific field will update only the data stored in that
    field; all other fields will be unaltered.  For example, updating a design's
    name requires that you make a PATCH request to this endpoint with data
    specified for the `name` field only.  ``` {     'name': '<Updated Name>' }
    ```.

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
    [http://api.sendgrid.com/v3/designs/{id}?&body=%s](
    http://api.sendgrid.com/v3/designs/{id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/designs/{id}"  # noqa
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
async def delete_designs_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a single design**.  Be sure to check the ID
    of the design you intend to delete before making this request; deleting a
    design is a permanent action.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/designs/{id}?](
    http://api.sendgrid.com/v3/designs/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/designs/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_designs(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new design**.  You can add a new design
    by passing data, including a string of HTML email content, to `/designs`.
    When creating designs from scratch, be aware of the styling constraints
    inherent to many email clients. For a list of best practices, see our guide
    to [Cross-Platform Email Design](https://sendgrid.com/docs/ui/sending-
    email/cross-platform-html-design/).  The Design Library can also convert
    your design’s HTML elements into drag and drop modules that are editable in
    the Designs Library user interface. For more, visit the [Design and Code
    Editor documentation](https://sendgrid.com/docs/ui/sending-email/editor/
    drag--drop-markup).  Because the `/designs` endpoint makes it easy to add
    designs, you can create a design with your preferred tooling or migrate
    designs you already own without relying on the Design Library UI.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/designs?&body=%s](
    http://api.sendgrid.com/v3/designs?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/designs"  # noqa

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
async def get_designs(
    sendgrid_credentials: "SendGridCredentials",
    page_size: int = 100,
    page_token: str = None,
    summary: bool = True,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of designs already stored in your
    Design Library**.  A GET request to `/designs` will return a list of your
    existing designs. This endpoint will not return the pre-built Twilio
    SendGrid designs. Pre-built designs can be retrieved using the
    `/designs/pre-builts` endpoint, which is detailed below.  By default, you
    will receive 100 results per request; however, you can modify the number of
    results returned by passing an integer to the `page_size` query parameter.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        page_size:
            number of results to return.
        page_token:
            token corresponding to a specific page of results, as provided by
            metadata.
        summary:
            set to false to return all fields.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/designs?&page_size=%s&page_token=%s&summary=%s](
    http://api.sendgrid.com/v3/designs?&page_size=%s&page_token=%s&summary=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/designs"  # noqa

    responses = {}

    params = {
        "page_size": page_size,
        "page_token": page_token,
        "summary": summary,
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
async def post_designs_pre_builts_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to duplicate one of the pre-built Twilio SendGrid
    designs**.  Like duplicating one of your existing designs, you are not
    required to pass any data in the body of a request to this endpoint. If you
    choose to leave the `name` field blank, your duplicate will be assigned the
    name of the design it was copied from with the text 'Duplicate: ' prepended
    to it. This name change is only a convenience, as the duplicate design will
    be assigned a unique ID that differentiates it from your other designs. You
    can retrieve the IDs for Twilio SendGrid pre-built designs using the 'List
    SendGrid Pre-built Designs' endpoint.  You can modify your duplicate’s name
    at the time of creation by passing an updated value to the `name` field when
    making the initial request. More on retrieving design IDs can be found
    above.

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
    [http://api.sendgrid.com/v3/designs/pre-builts/{id}?&body=%s](
    http://api.sendgrid.com/v3/designs/pre-builts/{id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/designs/pre-builts/{id}"  # noqa
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
async def get_designs_pre_builts_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a single pre-built design**.  A GET
    request to `/designs/pre-builts/{id}` will retrieve details about a specific
    pre-built design.  This endpoint is valuable when retrieving details about a
    pre-built design that you wish to duplicate and modify.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/designs/pre-builts/{id}?](
    http://api.sendgrid.com/v3/designs/pre-builts/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/designs/pre-builts/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_designs_pre_builts(
    sendgrid_credentials: "SendGridCredentials",
    page_size: int = 100,
    page_token: str = None,
    summary: bool = True,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of pre-built designs provided by
    Twilio SendGrid**.  Unlike the `/designs` endpoint where *your* designs are
    stored, a GET request made to `designs/pre-builts` will retrieve a list of
    the pre-built Twilio SendGrid designs. This endpoint will not return the
    designs stored in your Design Library.  By default, you will receive 100
    results per request; however, you can modify the number of results returned
    by passing an integer to the `page_size` query parameter.  This endpoint is
    useful for retrieving the IDs of Twilio SendGrid designs that you want to
    duplicate and modify.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        page_size:
            number of results to return.
        page_token:
            token corresponding to a specific page of results, as provided by
            metadata.
        summary:
            set to false to return all fields.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/designs/pre-builts?&page_size=%s&page_token=%s&summary=%s](
    http://api.sendgrid.com/v3/designs/pre-builts?&page_size=%s&page_token=%s&summary=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/designs/pre-builts"  # noqa

    responses = {}

    params = {
        "page_size": page_size,
        "page_token": page_token,
        "summary": summary,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
