import pytest
import subprocess
from sqltools import mysql

from sqltools import postgres

def test_when_missing_port_arg():
    """
    If port args is missing it should use default port
    """
    pass

def test_when_missing_password_arg():
    """
    If port args is missing it should use an environment variable called SQL_USER_PASSWORD
    """
    pass
