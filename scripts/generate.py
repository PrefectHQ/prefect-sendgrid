"""
Used for generating the repository from scratch.
"""
# from cookiecutter.main import cookiecutter
from prefect_collection_generator.rest import populate_collection_repo

# USE THIS IF NEED TO REGENERATE FROM SCRATCH; IF NOT SKIP TO NEXT SECTION
# extra_context = {
#     "full_name":  "Prefect Technologies, Inc.",  # e.g. "Prefect Technologies, Inc.",
#     "email": "help@prefect.io",  # e.g. "help@prefect.io",
#     "github_organization": "PrefectHQ",  # e.g. "PrefectHQ",
#     "collection_name": "prefect-sendgrid",
#     "collection_short_description": "Prefect integrations interacting with prefect-sendgrid",  # noqa
# }

# collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
# cookiecutter(
#     collection_template_url,
#     no_input=True,
#     checkout="generated_rest",
#     extra_context=extra_context,
#     overwrite_if_exists=True
# )

# UPDATE THESE AS DESIRED
service_name = "SendGrid"
urls = ["https://raw.githubusercontent.com/sendgrid/sendgrid-oai/main/oai.json"]
routes = None
overwrite = True

populate_collection_repo(
    service_name,
    urls,
    ref_base_route="parameters",
    routes=routes,
    overwrite=overwrite,
    repo_directory="..",
)
