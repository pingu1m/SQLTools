import pytest
from sqltools import docker

def test_run_tool_calls(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen')
    pg_docker = ['docker','run', '-it', '-e','PGPASSWORD=password', '--network', 'host', 'postgres:12-alpine', 'pg_dump' ]
    assert docker.run_tool('localhost','user','password','5432','sampledb')
    # exec_string = postgres.get_exec_string('localhost','user','password','5432','sampledb')
    # subprocess.Popen.assert_called_with(
    #     exec_string, stdout=subprocess.PIPE
    # )

