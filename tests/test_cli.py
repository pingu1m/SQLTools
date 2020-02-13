import pytest
from sqltools import cli


purl = "postgres://user@localhost:5432/sampledb"
murl = "mysql://user@localhost:3306/sampledb"


@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_without_url(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args(["--type", "postgres", "--driver", "local", "backups"])


def test_parser_without_type(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([purl, "--driver", "local", "backups"])


def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([purl, "--type", "postgres", "backups"])


def test_parser_without_destination(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([purl,   "--type", "postgres", "--driver", "local"])

def test_parser_complete(parser):
    """
    The parser will not exit if it receives all arguments
    """
    args = parser.parse_args( [purl, "--type","postgres", "--driver","local", "backups"])

    assert args.driver == 'local'
    assert args.url == purl
    assert args.type == 'postgres'
    assert args.destination == 'backups'


def test_parser_with_unknown_driver(parser):
    """
    The parser with exit if the driver name is unknown.
    """

    with pytest.raises(SystemExit):
        parser.parse_args([purl, "--type", "postgres", "--driver","azure", "destination"])

def test_parser_with_known_drivers(parser):
    """
    The parser will not exit if the driver name is known.
    """

    for driver in ['local', 's3']:
        assert parser.parse_args([purl, "--type", "postgres", "--driver",
                                  driver, 'destination'])


