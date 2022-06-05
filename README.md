# MIEM Project: Aggregation System

Repository for aggregation system in python with use Django framework.

# Configure system

There is requirements.txt with all library versions in the project.

Virtualenv environment is been used in project.

## Create env:

You shoule use the command for creating environment:
source venv/bin/activate 
Next step: pip install -r <file_name>

# Work pipeline:

Before each commit you must perform: `pre-commit run`

All users must create they branch from `develop`. When code is ready to go to develop you
should create merge request `your_branch -> develop` and check comments with another users

# Clone ERROR

When you clone repo and have error like:
`fatal: unable to access 'https://git.miem.hse.ru/980/aggregation_system.git/': server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none`

Use this: `export GIT_SSL_NO_VERIFY=1`. To use this export on terminal start append this
to `.bashrc`/`.zshrc` file.
