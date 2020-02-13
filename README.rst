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

Pass in a full database URL, the database type, the storage driver, and the destination

S3 Example w/ bucket name:

::

    $ sqltools postgres://bob@example.com:5432/db_one --engine postres --driver s3 backups

Local Example w/ local path:

::

    $ sqltools postgres://bob@example.com:5432/db_one --engine postgres --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make


