# prefect-sendgrid

## Welcome!

Prefect tasks and subflows for interacting with SendGrid.

The tasks within this collection were created by a code generator using the service's OpenAPI spec.

The service's REST API documentation can be found [here](replace_this_with_link_to_api_docs).

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-sendgrid` with `pip`:

```bash
pip install prefect-sendgrid
```

### Write and run a flow

```python
from prefect import flow
from prefect_sendgrid.tasks import (
    goodbye_prefect_sendgrid,
    hello_prefect_sendgrid,
)


@flow
def example_flow():
    hello_prefect_sendgrid
    goodbye_prefect_sendgrid

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-sendgrid`, feel free to open an issue in the [prefect-sendgrid](https://github.com/PrefectHQ/prefect-sendgrid) repository.

If you have any questions or issues while using `prefect-sendgrid`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-sendgrid` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-sendgrid.git

cd prefect-sendgrid/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
