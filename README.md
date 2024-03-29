#Python Library for Mocking SQL Queries with Dictionary Inputs

The primary purpose of this library is to simplify the testing of SQL data models and queries by allowing users to mock input data and create tests for various scenarios. It provides a consistent and convenient way to test the execution of your query without the need to process a massive amount of data.


The library currently supports the following databases.
* BigQuery
* Clickhouse
* Redshift
* Snowflake

## Installation

The library can be installed from [PyPI](https://pypi.org/project/sql-mock/) using pip:

```shell
# BigQuery
pip install --upgrade "sql-mock[bigquery]"

# Clickhouse
pip install --upgrade "sql-mock[clickhouse]"

# Redshift
pip install --upgrade "sql-mock[redshift]"

# Snowflake
pip install --upgrade "sql-mock[snowflake]"
```

If you need to modify this source code, install the dependencies using poetry:

```shell
poetry install --all-extras
```

## Contributing

We welcome contributions to improve and enhance this open-source project. Whether you want to report issues, suggest new features, or directly contribute to the codebase, your input is valuable. To ensure a smooth and collaborative experience for both contributors and maintainers, please follow these guidelines:

### Reporting Issues

If you encounter a bug, have a feature request, or face any issues with the project, we encourage you to report them using the project's issue tracker. When creating an issue, please include the following information:

- A clear and descriptive title.
- A detailed description of the problem or suggestion.
- Steps to reproduce the issue (if applicable).
- Any error messages or screenshots that help clarify the problem.

### Feature Requests

If you have ideas for new features or improvements, please use the project's issue tracker to submit a feature request. We appreciate well-documented feature requests that explain the motivation and potential use cases.

## Experimental

### SQL Mock Buddy - A custom (Chat) GPT to support you

SQL Mock Buddy should help you to get started quickly with SQL Mock.

It is still in beta mode and you should definitely double-check its output!
