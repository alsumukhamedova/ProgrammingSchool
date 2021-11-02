# MIEM Project: Aggregation System

Repository for aggregation system in python with use Django framework.

# Configure system

In project we use dependency managment [Poetry](https://python-poetry.org/docs/)

Poetry provides a [installer](https://python-poetry.org/docs/#installation) that will
install poetry isolated from the rest of your system by vendorizing its dependencies. This
is the recommended way of installing poetry.

In project using venv a miniconda. To install they download from
[site](https://docs.conda.io/en/latest/miniconda.html) miniconda Python version 3.8 to
your system (Linux/Windows)

Create env:

To stop `poetry` from creating new virtualenvs run
`poetry config virtualenvs.create false` (because we use `conda`, so poetry will use
currently activated environment instead of creating its own).

Next step create env: `conda env create -f environment.yml`

Install dependecies: `poetry install`

Configure pre-commit hooks: `pre-commit install`

TODO: create docker image to use they in gitlab-ci and run test

# Work pipeline:

Before each commit you must perform: `pre-commit run`

All user must create they branch from `develop`. When code ready to go to develop you
create merge request `your_branch -> develop` and check comments with another users

# Clone ERROR

If when you clone repo you have error like:
`fatal: unable to access 'https://git.miem.hse.ru/980/aggregation_system.git/': server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none`

Use this: `export GIT_SSL_NO_VERIFY=1`. To use this export when start terminal append this
to `.bashrc`/`.zshrc` file.
