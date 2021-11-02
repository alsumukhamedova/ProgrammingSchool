# MIEM Project: Aggregation System

Repository for aggregation system in python with use Django framework.

# Configure system

In project we use dependency managment [Poetry](https://python-poetry.org/docs/)

Poetry provides an [installer](https://python-poetry.org/docs/#installation) that will
install poetry isolated from the rest of your system by vendorizing its dependencies. This
is the recommended way of installing poetry.

Miniconda venv is been used in project. To install they download from
[site](https://docs.conda.io/en/latest/miniconda.html) miniconda Python version 3.8 to
your system (Linux/Windows)

## Create env:

To stop `poetry` from creating new virtualenvs run
`poetry config virtualenvs.create false` (because we use `conda`, so poetry will use
currently activated environment instead of creating its own).

Next step create env: `conda env create -f environment.yml`

Install dependecies: `poetry install`

Configure pre-commit hooks: `pre-commit install`

TODO: create docker image to use they in gitlab-ci and run test

# Work pipeline:

Before each commit you must perform: `pre-commit run`

All users must create they branch from `develop`. When code is ready to go to develop you
should create merge request `your_branch -> develop` and check comments with another users

# Clone ERROR

When you clone repo and have error like:
`fatal: unable to access 'https://git.miem.hse.ru/980/aggregation_system.git/': server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none`

Use this: `export GIT_SSL_NO_VERIFY=1`. To use this export on terminal start append this
to `.bashrc`/`.zshrc` file.
