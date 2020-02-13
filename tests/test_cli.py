import pytest
from sqltools import cli


@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_without_type(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args(
            ["-H", "localhost", "-U", "user", "-P" "5432", "--driver", "local", "backups"])


def test_parser_without_host(parser):
    """
    Without a host specified
    """
    with pytest.raises(SystemExit):
        parser.parse_args(["-T", "postgres", "-U", "user", "-P" "5432", "--driver", "local", "backups"])


def test_parser_without_user(parser):
    """
    Without a host specified
    """
    with pytest.raises(SystemExit):
        parser.parse_args(["-T", "postgres", "-H", "localhost","-P" "5432", "--driver", "local", "backups"])


def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args(["-T", "postgres", "-H", "localhost", "-U", "user", "-P" "5432", "backups"])


def test_parser_without_destination(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args(
        ["-T", "postgres", "-H", "localhost", "-U", "user", "-p", "password", "-P" "5432", "-db", "sampledb",
         "--driver", "local"])

def test_parser_complete(parser):
    """
    The parser will not exit if it receives all arguments
    """
    args = parser.parse_args(
        ["-T", "postgres", "-H", "localhost", "-U", "user", "-p", "password", "-P" "5432", "-db", "sampledb",
         "--driver", "local", "backups"])

    assert args.type == 'postgres'
    assert args.host == 'localhost'
    assert args.user == 'user'
    assert args.password == 'password'
    assert args.port == '5432'
    assert args.db == 'sampledb'
    assert args.driver == 'local'
    assert args.destination == 'backups'


def test_parser_with_unknown_driver(parser):
    """
    The parser with exit if the driver name is unknown.
    """

    with pytest.raises(SystemExit):
        parser.parse_args(["-T", "postgres", "-H", "localhost", "-U", "user","-p","password", "-P" "5432", "-db", "sampledb", "--driver", "azure", "backups"])

def test_parser_with_known_drivers(parser):
    """
    The parser will not exit if the driver name is known.
    """

    for driver in ['local', 's3']:
        assert parser.parse_args(["-T", "postgres", "-H", "localhost", "-U", "user","-p","password", "-P" "5432", "-db", "sampledb", "--driver", driver, "backups"])


