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
async def post_campaigns(
    sendgrid_credentials: "SendGridCredentials",
    body: str = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to create a campaign.**  In order to send or schedule
    the campaign, you will be required to provide a subject, sender ID, content
    (we suggest both html and plain text), and at least one list or segment ID.
    This information is not required when you create a campaign.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'title': 'title can't be blank' 'title': 'title is too long (maximum is 100    characters)' 'categories': 'categories exceeds 10 category limit'    'html_content': 'html_content exceeds the 1MB limit' 'plain_content':    'plain_content exceeds the 1MB limit' 'sender_id': 'sender_id does not    exist' 'sender_id': 'sender_id is not a verified sender identity'    'list_ids': 'list_ids do not all exist' 'segment_ids': 'segment_ids do not    all exist' 'ip_pool': 'The ip pool you provided is invalid'    'suppression_group_id': 'suppression_group_id does not exist'    'unsubscribes': 'Either suppression_group_id or custom_unsubscribe_url may    be set/used, but not both. Please remove one before setting the other.' '':    'The JSON you have submitted cannot be parsed.' '': 'You've reached your    limit of 250 campaigns. Please delete one or more and try again.'. |
    """  # noqa
    url = "http://api.sendgrid.com/v3/campaigns"  # noqa

    responses = {
        400: "'title': 'title can't be blank' 'title': 'title is too long (maximum is 100    characters)' 'categories': 'categories exceeds 10 category limit'    'html_content': 'html_content exceeds the 1MB limit' 'plain_content':    'plain_content exceeds the 1MB limit' 'sender_id': 'sender_id does not    exist' 'sender_id': 'sender_id is not a verified sender identity'    'list_ids': 'list_ids do not all exist' 'segment_ids': 'segment_ids do not    all exist' 'ip_pool': 'The ip pool you provided is invalid'    'suppression_group_id': 'suppression_group_id does not exist'    'unsubscribes': 'Either suppression_group_id or custom_unsubscribe_url may    be set/used, but not both. Please remove one before setting the other.' '':    'The JSON you have submitted cannot be parsed.' '': 'You've reached your    limit of 250 campaigns. Please delete one or more and try again.'.",  # noqa
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
async def get_campaigns(
    sendgrid_credentials: "SendGridCredentials",
    limit: int = 10,
    offset: int = 0,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a list of all of your campaigns.**
    Returns campaigns in reverse order they were created (newest first).
    Returns an empty array if no campaigns exist.

    Args:
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        limit:
            The number of results you would like to receive at a time.
        offset:
            The index of the first campaign to return, where 0 is the first
            campaign.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns?&limit=%s&offset=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns?&limit=%s&offset=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = "http://api.sendgrid.com/v3/campaigns"  # noqa

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
async def get_campaigns_campaign_id(
    campaign_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve a specific campaign.**.

    Args:
        campaign_id:
            Campaign id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns/{campaign_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns/{campaign_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 404 | '': 'not found'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/campaigns/{campaign_id}"  # noqa
    responses = {
        404: "'': 'not found'.",  # noqa
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
async def delete_campaigns_campaign_id(
    campaign_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to delete a specific campaign.**.

    Args:
        campaign_id:
            Campaign id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns/{campaign_id}?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns/{campaign_id}?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 404 | '': 'not found'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/campaigns/{campaign_id}"  # noqa
    responses = {
        404: "'': 'not found'.",  # noqa
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
async def patch_campaigns_campaign_id(
    campaign_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to update a specific campaign.**  This is especially
    useful if you only set up the campaign using POST /campaigns, but didn't set
    many of the parameters.

    Args:
        campaign_id:
            Campaign id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns/{campaign_id}?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns/{campaign_id}?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'title': 'title can't be blank' 'title': 'title is too long (maximum is 100    characters)' 'categories': 'categories exceeds 10 category limit'    'html_content': 'html_content exceeds the 1MB limit' 'plain_content':    'plain_content exceeds the 1MB limit' 'sender_id': 'sender_id does not    exist' 'sender_id': 'sender_id is not a verified sender identity'    'list_ids': 'list_ids do not all exist' 'segment_ids': 'segment_ids do not    all exist' 'ip_pool': 'The ip pool you provided is invalid'    'suppression_group_id': 'suppression_group_id does not exist'    'unsubscribes': 'Either suppression_group_id or custom_unsubscribe_url may    be set/used, but not both. Please remove one before setting the other.' '':    'The JSON you have submitted cannot be parsed.'. |
    | 403 | '': 'You may only update a campaign when it is in draft mode.'. |
    | 404 | '': 'not found'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/campaigns/{campaign_id}"  # noqa
    responses = {
        400: "'title': 'title can't be blank' 'title': 'title is too long (maximum is 100    characters)' 'categories': 'categories exceeds 10 category limit'    'html_content': 'html_content exceeds the 1MB limit' 'plain_content':    'plain_content exceeds the 1MB limit' 'sender_id': 'sender_id does not    exist' 'sender_id': 'sender_id is not a verified sender identity'    'list_ids': 'list_ids do not all exist' 'segment_ids': 'segment_ids do not    all exist' 'ip_pool': 'The ip pool you provided is invalid'    'suppression_group_id': 'suppression_group_id does not exist'    'unsubscribes': 'Either suppression_group_id or custom_unsubscribe_url may    be set/used, but not both. Please remove one before setting the other.' '':    'The JSON you have submitted cannot be parsed.'.",  # noqa
        403: "'': 'You may only update a campaign when it is in draft mode.'.",  # noqa
        404: "'': 'not found'.",  # noqa
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
async def post_campaigns_campaign_id_schedules_now(
    campaign_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to immediately send an existing campaign.**  Normally
    a POST request would have a body, but since this endpoint is telling us to
    send a resource that is already created, a request body is not needed.

    Args:
        campaign_id:
            Campaign id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules/now?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules/now?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'subject': 'subject can't be blank' 'sender_id': 'sender_id can't be blank'    'plain_content': 'plain_content can't be blank, please provide plain text or    html content' 'list_ids': 'You must select at least 1 segment or 1 list to    send to.' 'unsubscribe_tag': 'An [unsubscribe] tag in both your html and    plain content is required to send a campaign.' 'suppression_group_id':    'Either a suppression_group_id or custom_unsubscribe_url is required to send    a campaign.' '': 'You do not have enough credits to send this campaign.    Upgrade your plan to send more: https://app.sendgrid.com/settings/billing'. |
    | 403 | '': 'You may only send a campaign when it is in draft mode.'. |
    | 404 | '': 'not found'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules/now"  # noqa
    responses = {
        400: "'subject': 'subject can't be blank' 'sender_id': 'sender_id can't be blank'    'plain_content': 'plain_content can't be blank, please provide plain text or    html content' 'list_ids': 'You must select at least 1 segment or 1 list to    send to.' 'unsubscribe_tag': 'An [unsubscribe] tag in both your html and    plain content is required to send a campaign.' 'suppression_group_id':    'Either a suppression_group_id or custom_unsubscribe_url is required to send    a campaign.' '': 'You do not have enough credits to send this campaign.    Upgrade your plan to send more: https://app.sendgrid.com/settings/billing'.",  # noqa
        403: "'': 'You may only send a campaign when it is in draft mode.'.",  # noqa
        404: "'': 'not found'.",  # noqa
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
async def post_campaigns_campaign_id_schedules(
    campaign_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to schedule a specific date and time for your
    campaign to be sent.**  If you have the flexibility, it's better to schedule
    mail for off-peak times. Most emails are scheduled and sent at the top of
    the hour or half hour. Scheduling email to avoid those times (for example,
    scheduling at 10:53) can result in lower deferral rates because it won't be
    going through our servers at the same times as everyone else's mail.

    Args:
        campaign_id:
            Campaign id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | 'subject': 'subject can't be blank' 'sender_id': 'sender_id can't be blank'    'plain_content': 'plain_content can't be blank, please provide plain text or    html content' 'list_ids': 'You must select at least 1 segment or 1 list to    send to.' 'send_at': 'Please choose a future time for sending your    campaign.' 'unsubscribe_tag': 'An [unsubscribe] tag in both your html and    plain content is required to send a campaign.' 'suppression_group_id':    'Either a suppression_group_id or custom_unsubscribe_url is required to send    a campaign.' '': 'The JSON you have submitted cannot be parsed.' '':'You do    not have enough credits to send this campaign. Upgrade your plan to send    more: https://app.sendgrid.com/settings/billing'. |
    | 403 | '': 'You cannot POST to a campaign that has already sent or scheduled. However    you can update a scheduled campaign with a PATCH.'. |
    | 404 | '': 'not found'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules"  # noqa
    responses = {
        400: "'subject': 'subject can't be blank' 'sender_id': 'sender_id can't be blank'    'plain_content': 'plain_content can't be blank, please provide plain text or    html content' 'list_ids': 'You must select at least 1 segment or 1 list to    send to.' 'send_at': 'Please choose a future time for sending your    campaign.' 'unsubscribe_tag': 'An [unsubscribe] tag in both your html and    plain content is required to send a campaign.' 'suppression_group_id':    'Either a suppression_group_id or custom_unsubscribe_url is required to send    a campaign.' '': 'The JSON you have submitted cannot be parsed.' '':'You do    not have enough credits to send this campaign. Upgrade your plan to send    more: https://app.sendgrid.com/settings/billing'.",  # noqa
        403: "'': 'You cannot POST to a campaign that has already sent or scheduled. However    you can update a scheduled campaign with a PATCH.'.",  # noqa
        404: "'': 'not found'.",  # noqa
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
async def patch_campaigns_campaign_id_schedules(
    campaign_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows to you change the scheduled time and date for a campaign
    to be sent.**.

    Args:
        campaign_id:
            Campaign id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | '': 'The JSON you have submitted cannot be parsed.' 'send_at': 'Please choose a    future time for sending your campaign.' '':'You do not have enough credits    to send this campaign. Upgrade your plan to send more:    https://app.sendgrid.com/settings/billing'. |
    | 403 | 'send_at': 'You cannot update the send_at value of non-scheduled campaign.'. |
    | 404 | '': 'not found'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules"  # noqa
    responses = {
        400: "'': 'The JSON you have submitted cannot be parsed.' 'send_at': 'Please choose a    future time for sending your campaign.' '':'You do not have enough credits    to send this campaign. Upgrade your plan to send more:    https://app.sendgrid.com/settings/billing'.",  # noqa
        403: "'send_at': 'You cannot update the send_at value of non-scheduled campaign.'.",  # noqa
        404: "'': 'not found'.",  # noqa
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
async def get_campaigns_campaign_id_schedules(
    campaign_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to retrieve the date and time that a campaign has
    been scheduled to be sent.**.

    Args:
        campaign_id:
            Campaign id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 404 | '': 'not found'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules"  # noqa
    responses = {
        404: "'': 'not found'.",  # noqa
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
async def delete_campaigns_campaign_id_schedules(
    campaign_id: str,
    sendgrid_credentials: "SendGridCredentials",
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to unschedule a campaign that has already been
    scheduled to be sent.**  A successful unschedule will return a 204. If the
    specified campaign is in the process of being sent, the only option is to
    cancel (a different method).

    Args:
        campaign_id:
            Campaign id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules?&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules?&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 403 | '': 'This campaign is already In Progress.' '': 'This campaign is already Sent.'    '': 'This campaign is already Paused.' '': 'This campaign is already    Canceled.'. |
    | 404 | '': 'not found'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules"  # noqa
    responses = {
        403: "'': 'This campaign is already In Progress.' '': 'This campaign is already Sent.'    '': 'This campaign is already Paused.' '': 'This campaign is already    Canceled.'.",  # noqa
        404: "'': 'not found'.",  # noqa
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
async def post_campaigns_campaign_id_schedules_test(
    campaign_id: str,
    sendgrid_credentials: "SendGridCredentials",
    body: dict = None,
    on_behalf_of: str = "The subuser's username. This header generates the API call as if the subuser account was making the call.",  # noqa
) -> Dict[str, Any]:
    """
    **This endpoint allows you to send a test campaign.**  To send to multiple
    addresses, use an array for the JSON 'to' value
    ['one@address','two@address'].

    Args:
        campaign_id:
            Campaign id used in formatting the endpoint URL.
        sendgrid_credentials:
            Credentials to use for authentication with SendGrid.
        body:

        on_behalf_of:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules/test?&body=%s&on_behalf_of=%s](
    http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules/test?&body=%s&on_behalf_of=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 400 | '': 'The JSON you have submitted cannot be parsed.' 'to': 'Please provide an    email address to which the test should be sent.' 'to': 'You can only send    tests to 10 addresses at a time.' 'subject': 'Please add a subject to your    campaign before sending a test.' 'plain_content': 'Plain content and html    content can't both be blank. Please set one of these values before sending a    test.' 'sender_id': 'Please assign a sender identity to your campaign before    sending a test.'. |
    | 404 | '': 'not found'. |
    """  # noqa
    url = f"http://api.sendgrid.com/v3/campaigns/{campaign_id}/schedules/test"  # noqa
    responses = {
        400: "'': 'The JSON you have submitted cannot be parsed.' 'to': 'Please provide an    email address to which the test should be sent.' 'to': 'You can only send    tests to 10 addresses at a time.' 'subject': 'Please add a subject to your    campaign before sending a test.' 'plain_content': 'Plain content and html    content can't both be blank. Please set one of these values before sending a    test.' 'sender_id': 'Please assign a sender identity to your campaign before    sending a test.'.",  # noqa
        404: "'': 'not found'.",  # noqa
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
