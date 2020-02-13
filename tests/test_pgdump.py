import pytest
import subprocess

from sqltools import pgdump

purl = "postgres://user@127.0.0.1:5432/sampledb"
murl = "mysql://user@localhost:3306/sampledb"
pg_docker = ['docker','run', '-it', '-e','PGPASSWORD=password', '--network', 'host', 'postgres:12-alpine', 'pg_dump' ]


def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen')
    pg_docker = ['docker','run', '-it', '-e','PGPASSWORD=password', '--network', 'host', 'postgres:12-alpine', 'pg_dump' ]
    assert pgdump.dump(purl)
    subprocess.Popen.assert_called_with(
        ['docker','run', '-it', '-e','PGPASSWORD=password', '--network',
         'host', 'postgres:12-alpine', 'pg_dump' , purl], stdout=subprocess.PIPE
    )


def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError('no such file'))
    with pytest.raises(SystemExit):
        pgdump.dump(purl)


def test_dump_file_name_without_timestamp():
    """
    Take db url and create a nice filename
    """
    assert pgdump.dump_file_name(purl) == 'sampledb.sql'


def test_dump_file_name_with_timestamp():
    """
    Take db url and create a nice filename with timestamp
    """
    timestamp = '2020-02-03T13:12:10'
    assert pgdump.dump_file_name(purl, timestamp) == f"sampledb-{timestamp}.sql"
