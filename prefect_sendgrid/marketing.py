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
async def put_marketing_contacts(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows the [upsert](https://en.wiktionary.org/wiki/upsert)
    (insert or update) of up to 30,000 contacts, or 6MB of data, whichever is
    lower**.
    Because the creation and update of contacts is an asynchronous process, the
    response will not contain immediate feedback on the processing of your
    upserted contacts. Rather, it will contain an HTTP 202 response indicating
    the contacts are queued for processing or an HTTP 4XX error containing
    validation errors. Should you wish to get the resulting contact's ID or
    confirm your contacts have been updated or added, you can use the 'Get
    Contacts by Emails' endpoint.
    Please note that custom fields need to have been already created if you wish
    to set their values for the contacts being upserted. To do this, please use
    the 'Create Custom Field Definition' endpoint.  You will see a `job_id` in
    the response to your request. This can be used to check the status of your
    upsert job. To do so, please use the 'Import Contacts Status' endpoint.  If
    the contact already exists in the system, any entries submitted via this
    endpoint will update the existing contact. The contact to update will be
    determined only by the `email` field and any fields omitted from the request
    will remain as they were. A contact's ID cannot be used to update the
    contact.  The email field will be changed to all lower-case. If a contact is
    added with an email that exists but contains capital letters, the existing
    contact with the all lower-case email will be updated.  Twilio SendGrid
    recommends exporting your contacts regularly as a backup to avoid issues or
    lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts?&body=%s](
    http://api.sendgrid.com/v3/marketing/contacts?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts"  # noqa

    responses = {}

    params = {
        "body": body,
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
async def delete_marketing_contacts(
    sendgrid_credentials: "SendGridCredentials",
    delete_all_contacts: str = None,
    ids: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint can be used to delete one or more contacts**.  The query
    parameter `ids` must set to a comma-separated list of contact IDs for bulk
    contact deletion.  The query parameter `delete_all_contacts` must be set to
    `'true'` to delete **all** contacts.
    You must set either `ids` or `delete_all_contacts`.  Deletion jobs are
    processed asynchronously.  Twilio SendGrid recommends exporting your
    contacts regularly as a backup to avoid issues or lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        delete_all_contacts:
            Must be set to `'true'` to delete all contacts.
        ids:
            A comma-separated list of contact IDs.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts?&delete_all_contacts=%s&ids=%s](
    http://api.sendgrid.com/v3/marketing/contacts?&delete_all_contacts=%s&ids=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts"  # noqa

    responses = {}

    params = {
        "delete_all_contacts": delete_all_contacts,
        "ids": ids,
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
async def get_marketing_contacts(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint will return up to 50 of the most recent contacts uploaded or
    attached to a list**.
    This list will then be sorted by email address.  The full contact count is
    also returned.  Please note that pagination of the contacts has been
    deprecated.  Twilio SendGrid recommends exporting your contacts regularly as
    a backup to avoid issues or lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts?](
    http://api.sendgrid.com/v3/marketing/contacts?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_marketing_contacts_count(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint returns the total number of contacts you have stored.**   Twilio
    SendGrid recommends exporting your contacts regularly as a backup to avoid
    issues or lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/count?](
    http://api.sendgrid.com/v3/marketing/contacts/count?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts/count"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_marketing_contacts_exports(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **Use this endpoint to export lists or segments of contacts**.  If you would
    just like to have a link to the exported list sent to your email set the
    `notifications.email` option to `true` in the `POST` payload.  If you would
    like to download the list, take the `id` that is returned and use the
    'Export Contacts Status' endpoint to get the `urls`. Once you have the list
    of URLs, make a `GET` request to each URL provided to download your CSV
    file(s).  You specify the segements and or/contact lists you wish to export
    by providing the relevant IDs in, respectively, the `segment_ids` and
    `list_ids` fields in the request body.  The lists will be provided in either
    JSON or CSV files. To specify which of these you would required, set the
    request body `file_type` field to `json` or `csv`.  You can also specify a
    maximum file size (in MB). If the export file is larger than this, it will
    be split into multiple files.  Twilio SendGrid recommends exporting your
    contacts regularly as a backup to avoid issues or lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/exports?&body=%s](
    http://api.sendgrid.com/v3/marketing/contacts/exports?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts/exports"  # noqa

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
async def get_marketing_contacts_exports(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **Use this endpoint to retrieve details of all current exported jobs**.  It will
    return an array of objects, each of which records an export job in flight or
    recently completed.
    Each object's `export_type` field will tell you which kind of export it is
    and its `status` field will indicate what stage of processing it has
    reached. Exports which are `ready` will be accompanied by a `urls` field
    which lists the URLs of the export's downloadable files — there will be more
    than one if you specified a maximum file size in your initial export
    request.  Use this endpoint if you have exports in flight but do not know
    their IDs, which are required for the 'Export Contacts Status' endpoint.
    Twilio SendGrid recommends exporting your contacts regularly as a backup to
    avoid issues or lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/exports?](
    http://api.sendgrid.com/v3/marketing/contacts/exports?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts/exports"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_marketing_contacts_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint returns the full details and all fields for the specified
    contact**.  The 'Get Contacts by Emails' endpoint can be used to get the ID
    of a contact.  Twilio SendGrid recommends exporting your contacts regularly
    as a backup to avoid issues or lost data.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/{id}?](
    http://api.sendgrid.com/v3/marketing/contacts/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/contacts/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_marketing_contacts_search(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **Use this endpoint to locate contacts**.  The request body's `query` field
    accepts valid [SGQL](https://sendgrid.com/docs/for-developers/sending-
    email/segmentation-query-language/) for searching for a contact.  Because
    contact emails are stored in lower case, using SGQL to search by email
    address requires the provided email address to be in lower case. The SGQL
    `lower()` function can be used for this.  Only the first 50 contacts that
    meet the search criteria will be returned.  If the query takes longer than
    20 seconds, a `408 Request Timeout` status will be returned.  Formatting the
    `created_at` and `updated_at` values as Unix timestamps is deprecated.
    Instead they are returned as ISO format as string. Twilio SendGrid
    recommends exporting your contacts regularly as a backup to avoid issues or
    lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/search?&body=%s](
    http://api.sendgrid.com/v3/marketing/contacts/search?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts/search"  # noqa

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
async def put_marketing_contacts_imports(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows a CSV upload containing up to one million contacts or 5GB
    of data, whichever is smaller.**  Imports take place asynchronously: the
    endpoint returns a URL (`upload_uri`) and HTTP headers (`upload_headers`)
    which can subsequently be used to `PUT` a file of contacts to be  imported
    into our system.  Uploaded CSV files may also be [gzip-
    compressed](https://en.wikipedia.org/wiki/Gzip).  In either case, you must
    include the field `file_type` with the value `csv` in your request body.
    The `field_mappings` paramter is a respective list of field definition IDs
    to map the uploaded CSV columns to. It allows you to use CSVs where one or
    more columns are skipped (`null`) or remapped to the contact field.
    For example, if `field_mappings` is set to `[null, 'w1', '_rf1']`, this
    means skip column 0, map column 1 to the custom field with the ID `w1`, and
    map column 2 to the reserved field with the ID `_rf1`. See the 'Get All
    Field Definitions' endpoint to fetch your custom and reserved field IDs to
    use with `field_mappings`.  Once you recieve the response body you can then
    initiate a **second** API call where you use the supplied URL and HTTP
    header to upload your file. For example:  `curl --upload-file
    'file/path.csv' 'URL_GIVEN' -H 'HEADER_GIVEN'`  If you'd like to monitor the
    status of your import job, use the `job_id` and the 'Import Contacts Status'
    endpoint. Twilio SendGrid recommends exporting your contacts regularly as a
    backup to avoid issues or lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/imports?&body=%s](
    http://api.sendgrid.com/v3/marketing/contacts/imports?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts/imports"  # noqa

    responses = {}

    params = {
        "body": body,
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
async def get_marketing_contacts_imports_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint can be used to check the status of a contact import job**.
    Use the `job_id` from the 'Import Contacts,' 'Add or Update a Contact,' or
    'Delete Contacts' endpoints as the `id` in the path parameter.  If there is
    an error with your `PUT` request, download the `errors_url` file and open it
    to view more details.  The job `status` field indicates whether the job is
    `pending`, `completed`, `errored`, or `failed`.
    Pending means not started. Completed means finished without any errors.
    Errored means finished with some errors. Failed means finshed with all
    errors, or the job was entirely unprocessable: for example, if you attempt
    to import file format we do not support.  The `results` object will have
    fields depending on the job type.  Twilio SendGrid recommends exporting your
    contacts regularly as a backup to avoid issues or lost data.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/imports/{id}?](
    http://api.sendgrid.com/v3/marketing/contacts/imports/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/contacts/imports/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_marketing_contacts_exports_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint can be used to check the status of a contact export job**.
    To use this call, you will need the `id` from the 'Export Contacts' call.
    If you would like to download a list, take the `id` that is returned from
    the 'Export Contacts' endpoint and make an API request here to get the
    `urls`. Once you have the list of URLs, make a `GET` request on each URL to
    download your CSV file(s).  Twilio SendGrid recommends exporting your
    contacts regularly as a backup to avoid issues or lost data.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/exports/{id}?](
    http://api.sendgrid.com/v3/marketing/contacts/exports/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/contacts/exports/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_marketing_contacts_batch(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint is used to retrieve a set of contacts identified by their IDs.**
    This can be more efficient endpoint to get contacts than making a series of
    individual `GET` requests to the 'Get a Contact by ID' endpoint.  You can
    supply up to 100 IDs. Pass them into the `ids` field in your request body as
    an array or one or more strings.  Twilio SendGrid recommends exporting your
    contacts regularly as a backup to avoid issues or lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/batch?&body=%s](
    http://api.sendgrid.com/v3/marketing/contacts/batch?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts/batch"  # noqa

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
async def post_marketing_contacts_search_emails(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve up to 100 contacts matching the searched
    `email` address(es), including any `alternate_emails`.**
    Email addresses are unique to a contact, meaning this endpoint can treat an
    email address as a primary key to search by. The contact object associated
    with the address, whether it is their `email` or one of their
    `alternate_emails` will be returned if matched.  Email addresses in the
    search request do not need to match the case in which they're stored, but
    the email addresses in the result will be all lower case. Empty strings are
    excluded from the search and will not be returned.  This endpoint should be
    used in place of the 'Search Contacts' endpoint when you can provide exact
    email addresses and do not need to include other [Segmentation Query
    Language (SGQL)](https://sendgrid.com/docs/for-developers/sending-
    email/segmentation-query-language/) filters when searching.  If you need to
    access a large percentage of your contacts, we recommend exporting your
    contacts with the 'Export Contacts' endpoint and filtering the results
    client side.  This endpoint returns a `200` status code when any contacts
    match the address(es) you supplied. When searching multiple addresses in a
    single request, it is possible that some addresses will match a contact
    while others will not. When a partially successful search like this is made,
    the matching contacts are returned in an object and an error message is
    returned for the email address(es) that are not found.
    This endpoint returns a `404` status code when no contacts are found for the
    provided email address(es).  A `400` status code is returned if any searched
    addresses are invalid.  Twilio SendGrid recommends exporting your contacts
    regularly as a backup to avoid issues or lost data.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/contacts/search/emails?&body=%s](
    http://api.sendgrid.com/v3/marketing/contacts/search/emails?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/contacts/search/emails"  # noqa

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
async def post_marketing_segments_2_0(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **The Segmentation V2 API is currently in private beta. If you'd like to be
    added to the beta, please fill out this
    [form]({https://docs.google.com/forms/d/e/1FAIpQLSd5zwC9dRk8lAp1oTWjdGc-
    aSY69flW_7wnutvKBhpUluSnfQ/viewform)**  Segment `name` has to be unique. A
    user can not create a new segment with an existing segment name.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments/2.0?&body=%s](
    http://api.sendgrid.com/v3/marketing/segments/2.0?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/segments/2.0"  # noqa

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
async def get_marketing_segments_2_0(
    sendgrid_credentials: "SendGridCredentials",
    parent_list_ids: str = None,
    no_parent_list_id: bool = False,
) -> Dict[str, Any]:
    """
    **The Segmentation V2 API is currently in private beta. If you'd like to be
    added to the beta, please fill out this
    [form]({https://docs.google.com/forms/d/e/1FAIpQLSd5zwC9dRk8lAp1oTWjdGc-
    aSY69flW_7wnutvKBhpUluSnfQ/viewform)**  The query param `parent_list_ids` is
    treated as a filter.  Any match will be returned.  0 matches will return a
    response code of 200 with an empty `results` array.  `parent_list_ids` |
    `no_parent_list_id` | `result`
    -----------------:|:--------------------:|:------------- empty | false | all
    segments values | false | segments filtered by list_ids values | true |
    segments filtered by list_ids and segments with no parent list_ids empty |
    true | segments with no parent list_ids.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        parent_list_ids:
            A comma separated list up to 50 in size, to filter segments on.  Only
            segments that have any of these list ids as the parent list
            will be retrieved. This is different from the parameter of
            the same name used when creating a segment.
        no_parent_list_id:
            If set to `true` segments with an empty value of `parent_list_id` will
            be returned in the filter.  If the value is not present it
            defaults to 'false'.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments/2.0?&parent_list_ids=%s&no_parent_list_id=%s](
    http://api.sendgrid.com/v3/marketing/segments/2.0?&parent_list_ids=%s&no_parent_list_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/segments/2.0"  # noqa

    responses = {}

    params = {
        "parent_list_ids": parent_list_ids,
        "no_parent_list_id": no_parent_list_id,
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
async def patch_marketing_segments_2_0_segment_id(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **The Segmentation V2 API is currently in private beta. If you'd like to be
    added to the beta, please fill out this
    [form]({https://docs.google.com/forms/d/e/1FAIpQLSd5zwC9dRk8lAp1oTWjdGc-
    aSY69flW_7wnutvKBhpUluSnfQ/viewform)**  Segment `name` has to be unique. A
    user can not create a new segment with an existing segment name.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments/2.0/{segment_id}?&body=%s](
    http://api.sendgrid.com/v3/marketing/segments/2.0/{segment_id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/segments/2.0/{segment_id}"  # noqa
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
async def get_marketing_segments_2_0_segment_id(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
    contacts_sample: bool = None,
) -> Dict[str, Any]:
    """
    **The Segmentation V2 API is currently in private beta. If you'd like to be
    added to the beta, please fill out this
    [form]({https://docs.google.com/forms/d/e/1FAIpQLSd5zwC9dRk8lAp1oTWjdGc-
    aSY69flW_7wnutvKBhpUluSnfQ/viewform)**.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        contacts_sample:
            Defaults to `true`. Set to `false` to exclude the contacts_sample in the
            response.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments/2.0/{segment_id}?&contacts_sample=%s](
    http://api.sendgrid.com/v3/marketing/segments/2.0/{segment_id}?&contacts_sample=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/segments/2.0/{segment_id}"  # noqa
    responses = {}

    params = {
        "contacts_sample": contacts_sample,
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
async def delete_marketing_segments_2_0_segment_id(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **The Segmentation V2 API is currently in private beta. If you'd like to be
    added to the beta, please fill out this
    [form]({https://docs.google.com/forms/d/e/1FAIpQLSd5zwC9dRk8lAp1oTWjdGc-
    aSY69flW_7wnutvKBhpUluSnfQ/viewform)**.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments/2.0/{segment_id}?](
    http://api.sendgrid.com/v3/marketing/segments/2.0/{segment_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/segments/2.0/{segment_id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_marketing_senders(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new sender identity.**  *You may create
    up to 100 unique sender identities.*  Sender identities are required to be
    verified before use. If your domain has been authenticated, a new sender
    identity will auto verify on creation. Otherwise an email will be sent to
    the `from.email`.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/senders?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/marketing/senders?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/senders"  # noqa

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
async def post_marketing_lists(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint creates a new contacts list.**  Once you create a list, you can
    use the UI to [trigger an automation](https://sendgrid.com/docs/ui/sending-
    email/getting-started-with-automation/
    create-an-automation) every time you add a new contact to the list.  A link
    to the newly created object is in `_metadata`.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/lists?&body=%s](
    http://api.sendgrid.com/v3/marketing/lists?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/lists"  # noqa

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
async def get_marketing_lists(
    sendgrid_credentials: "SendGridCredentials",
    page_size: str = 100,
    page_token: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint returns an array of all of your contact lists.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        page_size:
            Maximum number of elements to return. Defaults to 100, returns 1000 max.
        page_token:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/lists?&page_size=%s&page_token=%s](
    http://api.sendgrid.com/v3/marketing/lists?&page_size=%s&page_token=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/lists"  # noqa

    responses = {}

    params = {
        "page_size": page_size,
        "page_token": page_token,
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
async def get_marketing_lists_id_contacts_count(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint returns the number of contacts on a specific list.**.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/lists/{id}/contacts/count?](
    http://api.sendgrid.com/v3/marketing/lists/{id}/contacts/count?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/lists/{id}/contacts/count"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_marketing_lists_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    contact_sample: bool = False,
) -> Dict[str, Any]:
    """
    **This endpoint returns data about a specific list.**  Setting the optional
    parameter `contact_sample=true` returns the `contact_sample` in the response
    body. Up to fifty of the most recent contacts uploaded or attached to a list
    will be returned, sorted alphabetically, by email address.  The full contact
    count is also returned.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        contact_sample:
            Setting this parameter to the true  will cause the contact_sample to be
            returned.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/lists/{id}?&contact_sample=%s](
    http://api.sendgrid.com/v3/marketing/lists/{id}?&contact_sample=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/lists/{id}"  # noqa
    responses = {}

    params = {
        "contact_sample": contact_sample,
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
async def patch_marketing_lists_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint updates the name of a list.**.

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
    [http://api.sendgrid.com/v3/marketing/lists/{id}?&body=%s](
    http://api.sendgrid.com/v3/marketing/lists/{id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/lists/{id}"  # noqa
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
async def delete_marketing_lists_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    delete_contacts: bool = False,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to deletes a specific list.**  Optionally, you can
    also delete contacts associated to the list. The query parameter,
    `delete_contacts=true`, will delete the list and start an asynchronous job
    to delete associated contacts.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        delete_contacts:
            Flag indicates that all contacts on the list are also to be deleted.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/lists/{id}?&delete_contacts=%s](
    http://api.sendgrid.com/v3/marketing/lists/{id}?&delete_contacts=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/lists/{id}"  # noqa
    responses = {}

    params = {
        "delete_contacts": delete_contacts,
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
async def delete_marketing_lists_id_contacts(
    id: str,
    contact_ids: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to remove contacts from a given list.**  The contacts
    will not be deleted. Only their list membership will be changed.

    Args:
        id:
            Id used in formatting the endpoint URL.
        contact_ids:
            comma separated list of contact ids.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/lists/{id}/contacts?&contact_ids=%s](
    http://api.sendgrid.com/v3/marketing/lists/{id}/contacts?&contact_ids=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/lists/{id}/contacts"  # noqa
    responses = {}

    params = {
        "contact_ids": contact_ids,
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
async def post_marketing_field_definitions(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint creates a new custom field definition.**  Custom field
    definitions are created with the given `name` and `field_type`. Although
    field names are stored in a case-sensitive manner, all field names must be
    case-insensitively unique. This means you may create a field named
    `CamelCase` or `camelcase`, but not both. Additionally, a Custom Field name
    cannot collide with any Reserved Field names. You should save the returned
    `id` value in order to update or delete the field at a later date. You can
    have up to 120 custom fields.  The custom field name should be created using
    only alphanumeric characters (A-Z and 0-9) and underscores (\_). Custom
    fields can only begin with letters  A-Z or underscores (_). The field type
    can be date, text, or number fields. The field type is important for
    creating segments from your contact database.  **Note: Creating a custom
    field that begins with a number will cause issues with sending in Marketing
    Campaigns.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/field_definitions?&body=%s](
    http://api.sendgrid.com/v3/marketing/field_definitions?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/field_definitions"  # noqa

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
async def get_marketing_field_definitions(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint retrieves all defined Custom Fields and Reserved Fields.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/field_definitions?](
    http://api.sendgrid.com/v3/marketing/field_definitions?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/field_definitions"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def patch_marketing_field_definitions_custom_field_id(
    custom_field_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endopoint allows you to update a defined Custom Field.**  Only your
    Custom fields can be modified; Reserved Fields cannot be updated.

    Args:
        custom_field_id:
            Custom field id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/field_definitions/{custom_field_id}?&body=%s](
    http://api.sendgrid.com/v3/marketing/field_definitions/{custom_field_id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/field_definitions/{custom_field_id}"  # noqa
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
async def delete_marketing_field_definitions_custom_field_id(
    custom_field_id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint deletes a defined Custom Field.**  You cand delete only Custom
    Fields; Reserved Fields cannot be deleted.

    Args:
        custom_field_id:
            Custom field id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/field_definitions/{custom_field_id}?](
    http://api.sendgrid.com/v3/marketing/field_definitions/{custom_field_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/field_definitions/{custom_field_id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_marketing_segments(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a segment.**.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments?&body=%s](
    http://api.sendgrid.com/v3/marketing/segments?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/segments"  # noqa

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
async def get_marketing_segments(
    sendgrid_credentials: "SendGridCredentials",
    parent_list_ids: str = None,
    no_parent_list_id: bool = False,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of segments.**  The query param
    `parent_list_ids` is treated as a filter.  Any match will be returned.  0
    matches will return a response code of 200 with an empty `results` array.
    `parent_list_ids` | `no_parent_list_id` | `result`
    -----------------:|:--------------------:|:------------- empty | false | all
    segments values | false | segments filtered by list_ids values | true |
    segments filtered by list_ids and segments with no parent list_ids empty |
    true | segments with no parent list_ids.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        parent_list_ids:
            A comma separated list of list ids to be used when searching for
            segments with the specified parent_list_id, no more than 50
            is allowed.
        no_parent_list_id:
            If set to `true` segments with an empty value of `parent_list_id` will
            be returned in the filter.  If the value is not present it
            defaults to 'false'.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments?&parent_list_ids=%s&no_parent_list_id=%s](
    http://api.sendgrid.com/v3/marketing/segments?&parent_list_ids=%s&no_parent_list_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/segments"  # noqa

    responses = {}

    params = {
        "parent_list_ids": parent_list_ids,
        "no_parent_list_id": no_parent_list_id,
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
async def get_marketing_segments_segment_id(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
    query_json: bool = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a single segment by ID.**.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        query_json:
            Defaults to `false`.  Set to `true` to return the parsed SQL AST as a
            JSON object in the field `query_json`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments/{segment_id}?&query_json=%s](
    http://api.sendgrid.com/v3/marketing/segments/{segment_id}?&query_json=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/segments/{segment_id}"  # noqa
    responses = {}

    params = {
        "query_json": query_json,
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
async def patch_marketing_segments_segment_id(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update a segment.**  Segment `name` needs to be
    unique. A user can not update a segment name to an existing one.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments/{segment_id}?&body=%s](
    http://api.sendgrid.com/v3/marketing/segments/{segment_id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/segments/{segment_id}"  # noqa
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
async def delete_marketing_segments_segment_id(
    segment_id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a segment by `segment_id`.**  Note that
    deleting a segment does not delete the contacts associated with the segment
    by default. Contacts associated with a deleted segment will remain in your
    list of all contacts and any other segments they belong to.

    Args:
        segment_id:
            Segment id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments/{segment_id}?](
    http://api.sendgrid.com/v3/marketing/segments/{segment_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/segments/{segment_id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_marketing_segments_delete(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    This endpoint allows you to delete segments in bulk.  If the segments are used
    by automations or the segments do not exist in the database, the segment IDs
    that could not be deleted along with automation IDs that are associated to
    those segments will be returned.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/segments/delete?&body=%s](
    http://api.sendgrid.com/v3/marketing/segments/delete?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/segments/delete"  # noqa

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
async def post_marketing_singlesends(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a new Single Send.**  Please note that if
    you are migrating from the previous version of Single Sends, you no longer
    need to pass a template ID with your request to this endpoint. Instead, you
    will pass all template data in the `email_config` object.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/singlesends?&body=%s](
    http://api.sendgrid.com/v3/marketing/singlesends?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/singlesends"  # noqa

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
async def get_marketing_singlesends(
    sendgrid_credentials: "SendGridCredentials",
    page_size: int = None,
    page_token: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all your Single Sends.**  Returns all of
    your Single Sends with condensed details about each, including the Single
    Sends' IDs. For more details about an individual Single Send, pass the
    Single Send's ID to the `/marketing/singlesends/{id}` endpoint.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        page_size:

        page_token:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/singlesends?&page_size=%s&page_token=%s](
    http://api.sendgrid.com/v3/marketing/singlesends?&page_size=%s&page_token=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/singlesends"  # noqa

    responses = {}

    params = {
        "page_size": page_size,
        "page_token": page_token,
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
async def delete_marketing_singlesends(
    sendgrid_credentials: "SendGridCredentials",
    ids: list = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete multiple Single Sends using an array of
    Single Sends IDs.**  To first retrieve all your Single Sends' IDs, you can
    make a GET request to the `/marketing/singlensends` endpoint.  Please note
    that a DELETE request is permanent, and your Single Sends will not be
    recoverable after deletion.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        ids:
            Single Send IDs to delete.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/singlesends?&ids=%s](
    http://api.sendgrid.com/v3/marketing/singlesends?&ids=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/singlesends"  # noqa

    responses = {}

    params = {
        "ids": ids,
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
async def post_marketing_singlesends_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to duplicate an existing Single Send using its Single
    Send ID.**  Duplicating a Single Send is useful when you want to create a
    Single Send but don't want to start from scratch. Once duplicated, you can
    update or edit the Single Send by making a PATCH request to the
    `/marketing/singlesends/{id}` endpoint.   If you leave the `name` field
    blank, your duplicate will be assigned the name of the Single Send it was
    copied from with the text “Copy of ” prepended to it. The `name` field
    length is limited to 100 characters, so the end of the new Single Send name,
    including “Copy of ”, will be trimmed if the name exceeds this limit.

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
    [http://api.sendgrid.com/v3/marketing/singlesends/{id}?&body=%s](
    http://api.sendgrid.com/v3/marketing/singlesends/{id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/singlesends/{id}"  # noqa
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
async def patch_marketing_singlesends_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update a Single Send using a Single Send ID.**
    You only need to pass the fields you want to update. Any blank/missing
    fields will remain unaltered.

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
    [http://api.sendgrid.com/v3/marketing/singlesends/{id}?&body=%s](
    http://api.sendgrid.com/v3/marketing/singlesends/{id}?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/singlesends/{id}"  # noqa
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
async def get_marketing_singlesends_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve details about one Single Send using a
    Single Send ID.**  You can retrieve all of your Single Sends by making a GET
    request to the `/marketing/singlesends` endpoint.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/singlesends/{id}?](
    http://api.sendgrid.com/v3/marketing/singlesends/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/singlesends/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def delete_marketing_singlesends_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete one Single Send using a Single Send ID.**
    To first retrieve all your Single Sends' IDs, you can make a GET request to
    the `/marketing/singlensends` endpoint.  Please note that a `DELETE` request
    is permanent, and your Single Send will not be recoverable after deletion.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/singlesends/{id}?](
    http://api.sendgrid.com/v3/marketing/singlesends/{id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/singlesends/{id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_marketing_singlesends_search(
    sendgrid_credentials: "SendGridCredentials",
    page_size: int = None,
    page_token: str = None,
    body: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to search for Single Sends based on specified
    criteria.**  You can search for Single Sends by passing a combination of
    values using the `name`, `status`, and `categories` request body fields.
    For example, if you want to search for all Single Sends that are 'drafts' or
    'scheduled' and also associated with the category 'shoes,' your request body
    may look like the example below.  ```javascript {   'status': [     'draft',
    'scheduled'   ],   'categories': [     'shoes'   ], } ```.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        page_size:

        page_token:

        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/singlesends/search?&page_size=%s&page_token=%s&body=%s](
    http://api.sendgrid.com/v3/marketing/singlesends/search?&page_size=%s&page_token=%s&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/singlesends/search"  # noqa

    responses = {}

    params = {
        "page_size": page_size,
        "page_token": page_token,
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
async def put_marketing_singlesends_id_schedule(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to schedule a Single Send for future delivery using a
    Single Send ID.**  To schedule a Single Send, you must pass a date string in
    ISO 8601 time format (yyyy-MM-ddTHH:mm:ssZ)  using the required `send_at`
    field. For example, the ISO 8601 format for 9:00 AM UTC on May 6, 2020 would
    be `2020-05-06T09:00:00Z`. You may also pass the string `'now'` to send the
    Single Send immediately.

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
    [http://api.sendgrid.com/v3/marketing/singlesends/{id}/schedule?&body=%s](
    http://api.sendgrid.com/v3/marketing/singlesends/{id}/schedule?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/singlesends/{id}/schedule"  # noqa
    responses = {}

    params = {
        "body": body,
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
async def delete_marketing_singlesends_id_schedule(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to cancel a scheduled Single Send using a Single Send
    ID.**  Making a DELETE request to this endpoint will cancel the scheduled
    sending of a Single Send. The request will not delete the Single Send
    itself. Deleting a Single Send can be done by passing a DELETE request to
    `/marketing/singlesends/{id}`.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/singlesends/{id}/schedule?](
    http://api.sendgrid.com/v3/marketing/singlesends/{id}/schedule?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/singlesends/{id}/schedule"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_marketing_singlesends_categories(
    sendgrid_credentials: "SendGridCredentials",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve all the categories associated with your
    Single Sends.**  This endpoint will return your latest 1,000 categories.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/singlesends/categories?](
    http://api.sendgrid.com/v3/marketing/singlesends/categories?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/singlesends/categories"  # noqa

    responses = {}

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_marketing_test_send_email(
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to send a test marketing email to a list of email
    addresses**.  Before sending a marketing message, you can test it using this
    endpoint. You may specify up to **10 contacts** in the `emails` request body
    field. You must also specify a `template_id` and include either a
    `from_address` or `sender_id`. You can manage your templates with the
    [Twilio SendGrid App](https://mc.sendgrid.com/dynamic-templates) or the
    [Transactional Templates API](https://sendgrid.api-
    docs.io/v3.0/transactional-templates).  > Please note that this endpoint
    works with Dynamic Transactional Templates only. Legacy Transactional
    Templates will not be delivered.  For more information about managing
    Dynamic Transactional Templates, see [How to Send Email with Dynamic
    Transactional Templates](https://sendgrid.com/docs/ui/sending-email/how-to-
    send-an-email-with-dynamic-transactional-templates/).  You can also test
    your Single Sends in the [Twilio SendGrid Marketing Campaigns
    UI](https://mc.sendgrid.com/single-sends).

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/test/send_email?&body=%s](
    http://api.sendgrid.com/v3/marketing/test/send_email?&body=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/test/send_email"  # noqa

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
async def get_marketing_stats_automations(
    sendgrid_credentials: "SendGridCredentials",
    automation_ids: list = None,
    page_size: int = 50,
    page_token: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve stats for all your Automations.**  By
    default, all of your Automations will be returned, but you can specify a
    selection by passing in a comma-separated list of Automation IDs as the
    value of the query string parameter `automation_ids`.  Responses are
    paginated. You can limit the number of responses returned per batch using
    the `page_size` query string parameter. The default is 50, but you specify a
    value between 1 and 100.  You can retrieve a specific page of responses with
    the `page_token` query string parameter.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        automation_ids:
            This endpoint returns all automation IDs if no `automation_ids` are
            specified.
        page_size:
            The number of elements you want returned on each page.
        page_token:
            The stats endpoints are paginated. To get the next page, call the passed
            `_metadata.next` URL. If `_metadata.prev` doesn't exist,
            you're at the first page. Similarly, if `_metadata.next` is
            not present, you're at the last page.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/stats/automations?&automation_ids=%s&page_size=%s&page_token=%s](
    http://api.sendgrid.com/v3/marketing/stats/automations?&automation_ids=%s&page_size=%s&page_token=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/stats/automations"  # noqa

    responses = {}

    params = {
        "automation_ids": automation_ids,
        "page_size": page_size,
        "page_token": page_token,
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
async def get_marketing_stats_automations_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    group_by: list = None,
    step_ids: list = None,
    aggregated_by: str = "total",
    start_date: str = None,
    end_date: str = None,
    timezone: str = "UTC",
    page_size: int = 50,
    page_token: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve stats for a single Automation using its
    ID.**  Multiple Automation IDs can be retrieved using the 'Get All
    Automation Stats' endpoint. Once you have an ID, this endpoint will return
    detailed stats for the single automation specified.  You may constrain the
    stats returned using the `start_date` and `end_date` query string
    parameters. You can also use the `group_by` and `aggregated_by` query string
    parameters to further refine the stats returned.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        group_by:
            Automations can have multiple steps. Including `step_id` as a `group_by`
            metric allows further granularity of stats.
        step_ids:
            Comma-separated list of `step_ids` that you want the link stats for.
        aggregated_by:
            Dictates how the stats are time-sliced. Currently, `'total'` and `'day'`
            are supported.
        start_date:
            Format: `YYYY-MM-DD`. If this parameter is included, the stats' start
            date is included in the search.
        end_date:
            Format: `YYYY-MM-DD`.If this parameter is included, the stats' end date
            is included in the search.
        timezone:
            [IANA Area/Region](https://en.wikipedia.org/wiki/Tz_database
            Names_of_time_zones) string representing the timezone in
            which the stats are to be presented, e.g.,
            'America/Chicago'.
        page_size:
            The number of elements you want returned on each page.
        page_token:
            The stats endpoints are paginated. To get the next page, call the passed
            `_metadata.next` URL. If `_metadata.prev` doesn't exist,
            you're at the first page. Similarly, if `_metadata.next` is
            not present, you're at the last page.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/stats/automations/{id}?&group_by=%s&step_ids=%s&aggregated_by=%s&start_date=%s&end_date=%s&timezone=%s&page_size=%s&page_token=%s](
    http://api.sendgrid.com/v3/marketing/stats/automations/{id}?&group_by=%s&step_ids=%s&aggregated_by=%s&start_date=%s&end_date=%s&timezone=%s&page_size=%s&page_token=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/stats/automations/{id}"  # noqa
    responses = {}

    params = {
        "group_by": group_by,
        "step_ids": step_ids,
        "aggregated_by": aggregated_by,
        "start_date": start_date,
        "end_date": end_date,
        "timezone": timezone,
        "page_size": page_size,
        "page_token": page_token,
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
async def get_marketing_stats_singlesends(
    sendgrid_credentials: "SendGridCredentials",
    singlesend_ids: list = None,
    page_size: int = 50,
    page_token: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve stats for all your Single Sends.**  By
    default, all of your Single Sends will be returned, but you can specify a
    selection by passing in a comma-separated list of Single Send IDs as the
    value of the query string parameter `singlesend_ids`.  Responses are
    paginated. You can limit the number of responses returned per batch using
    the `page_size` query string parameter. The default is 50, but you specify a
    value between 1 and 100.  You can retrieve a specific page of responses with
    the `page_token` query string parameter.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        singlesend_ids:
            This endpoint returns all Single Send IDs if no IDs are included in
            `singlesend_ids`.
        page_size:
            The number of elements you want returned on each page.
        page_token:
            The stats endpoints are paginated. To get the next page, call the passed
            `_metadata.next` URL. If `_metadata.prev` doesn't exist,
            you're at the first page. Similarly, if `_metadata.next` is
            not present, you're at the last page.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/stats/singlesends?&singlesend_ids=%s&page_size=%s&page_token=%s](
    http://api.sendgrid.com/v3/marketing/stats/singlesends?&singlesend_ids=%s&page_size=%s&page_token=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/stats/singlesends"  # noqa

    responses = {}

    params = {
        "singlesend_ids": singlesend_ids,
        "page_size": page_size,
        "page_token": page_token,
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
async def get_marketing_stats_singlesends_id(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    aggregated_by: str = "total",
    start_date: str = None,
    end_date: str = None,
    timezone: str = "UTC",
    page_size: int = 50,
    page_token: str = None,
    group_by: list = None,
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve stats for an individual Single Send using
    a Single Send ID.**  Multiple Single Send IDs can be retrieved using the
    'Get All Single Sends Stats' endpoint. Once you have an ID, this endpoint
    will return detailed stats for the Single Send specified.  You may constrain
    the stats returned using the `start_date` and `end_date` query string
    parameters. You can also use the `group_by` and `aggregated_by` query string
    parameters to further refine the stats returned.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        aggregated_by:
            Dictates how the stats are time-sliced. Currently, `'total'` and `'day'`
            are supported.
        start_date:
            Format: `YYYY-MM-DD`. If this parameter is included, the stats' start
            date is included in the search.
        end_date:
            Format: `YYYY-MM-DD`.If this parameter is included, the stats' end date
            is included in the search.
        timezone:
            [IANA Area/Region](https://en.wikipedia.org/wiki/Tz_database
            Names_of_time_zones) string representing the timezone in
            which the stats are to be presented, e.g.,
            'America/Chicago'.
        page_size:
            The number of elements you want returned on each page.
        page_token:
            The stats endpoints are paginated. To get the next page, call the passed
            `_metadata.next` URL. If `_metadata.prev` doesn't exist,
            you're at the first page. Similarly, if `_metadata.next` is
            not present, you're at the last page.
        group_by:
            A/B Single Sends have multiple variation IDs and phase IDs. Including
            these additional fields allows further granularity of stats
            by these fields.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/stats/singlesends/{id}?&aggregated_by=%s&start_date=%s&end_date=%s&timezone=%s&page_size=%s&page_token=%s&group_by=%s](
    http://api.sendgrid.com/v3/marketing/stats/singlesends/{id}?&aggregated_by=%s&start_date=%s&end_date=%s&timezone=%s&page_size=%s&page_token=%s&group_by=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/stats/singlesends/{id}"  # noqa
    responses = {}

    params = {
        "aggregated_by": aggregated_by,
        "start_date": start_date,
        "end_date": end_date,
        "timezone": timezone,
        "page_size": page_size,
        "page_token": page_token,
        "group_by": group_by,
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
async def get_marketing_stats_automations_id_links(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    group_by: list = None,
    step_ids: list = None,
    page_size: int = 50,
    page_token: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint lets you retrieve click-tracking stats for a single
    Automation**.  The stats returned list the URLs embedded in your Automation
    and the number of clicks each one received.  Responses are paginated. You
    can limit the number of responses returned per batch using the `page_size`
    query string parameter. The default is 50, but you specify a value between 1
    and 100.  You can retrieve a specific page of responses with the
    `page_token` query string parameter.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        group_by:
            Automations can have multiple steps. Including `step_id` as a `group_by`
            metric allows further granularity of stats.
        step_ids:
            Comma-separated list of `step_ids` that you want the link stats for.
        page_size:
            The number of elements you want returned on each page.
        page_token:
            The stats endpoints are paginated. To get the next page, call the passed
            `_metadata.next` URL. If `_metadata.prev` doesn't exist,
            you're at the first page. Similarly, if `_metadata.next` is
            not present, you're at the last page.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/stats/automations/{id}/links?&group_by=%s&step_ids=%s&page_size=%s&page_token=%s](
    http://api.sendgrid.com/v3/marketing/stats/automations/{id}/links?&group_by=%s&step_ids=%s&page_size=%s&page_token=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/stats/automations/{id}/links"  # noqa
    responses = {}

    params = {
        "group_by": group_by,
        "step_ids": step_ids,
        "page_size": page_size,
        "page_token": page_token,
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
async def get_marketing_stats_singlesends_id_links(
    id: str,
    sendgrid_credentials: "SendGridCredentials",
    page_size: int = 50,
    page_token: str = None,
    group_by: list = None,
    ab_variation_id: str = None,
    ab_phase_id: str = None,
) -> Dict[str, Any]:
    """
    **This endpoint lets you retrieve click-tracking stats for one Single Send**.
    The stats returned list the URLs embedded in the specified Single Send and
    the number of clicks each one received.  Responses are paginated. You can
    limit the number of responses returned per batch using the `page_size` query
    string parameter. The default is 50, but you specify a value between 1 and
    100.  You can retrieve a specific page of responses with the `page_token`
    query string parameter.

    Args:
        id:
            Id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        page_size:
            The number of elements you want returned on each page.
        page_token:
            The stats endpoints are paginated. To get the next page, call the passed
            `_metadata.next` URL. If `_metadata.prev` doesn't exist,
            you're at the first page. Similarly, if `_metadata.next` is
            not present, you're at the last page.
        group_by:
            A/B Single Sends have multiple variation IDs and phase IDs. Including
            these additional fields allows further granularity of stats
            by these fields.
        ab_variation_id:

        ab_phase_id:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/stats/singlesends/{id}/links?&page_size=%s&page_token=%s&group_by=%s&ab_variation_id=%s&ab_phase_id=%s](
    http://api.sendgrid.com/v3/marketing/stats/singlesends/{id}/links?&page_size=%s&page_token=%s&group_by=%s&ab_variation_id=%s&ab_phase_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/marketing/stats/singlesends/{id}/links"  # noqa
    responses = {}

    params = {
        "page_size": page_size,
        "page_token": page_token,
        "group_by": group_by,
        "ab_variation_id": ab_variation_id,
        "ab_phase_id": ab_phase_id,
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
async def get_marketing_stats_singlesends_export(
    sendgrid_credentials: "SendGridCredentials",
    ids: list = None,
    timezone: str = "UTC",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to export Single Send stats as .CSV data**.  You can
    specify one Single Send or many: include as many Single Send IDs as you
    need, separating them with commas, as the value of the `ids` query string
    paramter.  The data is returned as plain text response but in .CSV format,
    so your application making the call can present the information in whatever
    way is most appropriate, or just save the data as a .csv file.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        ids:
            The IDs of Single Sends for which to export stats.
        timezone:
            The [IANA Area/Region](https://en.wikipedia.org/wiki/Tz_database
            Names_of_time_zones) string representing the timezone in
            which the stats are to be presented; i.e.
            `'America/Chicago'`. This parameter changes the timezone
            format only; it does not alter which stats are returned.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/stats/singlesends/export?&ids=%s&timezone=%s](
    http://api.sendgrid.com/v3/marketing/stats/singlesends/export?&ids=%s&timezone=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/stats/singlesends/export"  # noqa

    responses = {}

    params = {
        "ids": ids,
        "timezone": timezone,
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
async def get_marketing_stats_automations_export(
    sendgrid_credentials: "SendGridCredentials",
    ids: list = None,
    timezone: str = "UTC",
) -> Dict[str, Any]:
    """
    **This endpoint allows you to export Automation stats as CSV data**.  You can
    specify one Automation or many: include as many Automation IDs as you need,
    separating them with commas, as the value of the `ids` query string
    paramter.  The data is returned as plain text response but in CSV format, so
    your application making the call can present the information in whatever way
    is most appropriate, or just save the data as a `.csv` file.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        ids:
            The IDs of Automations for which to export stats.
        timezone:
            The [IANA Area/Region](https://en.wikipedia.org/wiki/Tz_database
            Names_of_time_zones) string representing the timezone in
            which the stats are to be presented; i.e.
            `'America/Chicago'`. This parameter changes the timezone
            format only; it does not alter which stats are returned.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/marketing/stats/automations/export?&ids=%s&timezone=%s](
    http://api.sendgrid.com/v3/marketing/stats/automations/export?&ids=%s&timezone=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/marketing/stats/automations/export"  # noqa

    responses = {}

    params = {
        "ids": ids,
        "timezone": timezone,
    }

    result = await execute_endpoint.fn(
        url,
        sendgrid_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result
