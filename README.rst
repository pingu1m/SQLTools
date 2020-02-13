SQLTools
=======

CLI for backup remote SQL databases either locally or to a S3 like destination.

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone https://github.com/pingu1m/SQLTools``
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in the type of the database to backup, the host, the user, the password or set an environment variable called ``SQL_USER_PASSWORD``, the port (optional), the database name and finally the storage driver ['s3', 'local']

S3 Example w/ bucket name:

::

    $ sqltools --type postgres --host 127.0.0.1 --user user --password password --port 5432 --db sampledb --driver s3 backups
    $ sqltools --type mysql    --host 127.0.0.1 --user user --password password --port 3306 --db sampledb --driver s3 backups

Local Example w/ local path:

::

    $ sqltools --type postgres --host 127.0.0.1 --user user --password password --port 5432 --db sampledb --driver s3 local dump.sql
    $ sqltools --type mysql    --host 127.0.0.1 --user user --password password --port 3306 --db sampledb --driver s3 local dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make


