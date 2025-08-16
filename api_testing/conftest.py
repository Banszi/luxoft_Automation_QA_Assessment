import pytest
import sys
from copy import deepcopy
import subprocess

from mock_api import users
from utils import SERVER_SCRIPT_NAME
from logger_utils import logger


@pytest.fixture()
def init_users_list():
    """
    Fixture provides users data stored in HTTP Flask server
    in single test scope.
    """
    users_list = deepcopy(users)
    return users_list


@pytest.fixture(scope="session", autouse=True)
def control_http_server():
    """
    Fixture that controls enabling and disabling HTTP Flask server
    in test scope session.
    """
    logger.info(f"Enabling HTTP Flask server from script: {SERVER_SCRIPT_NAME}")
    process = subprocess.Popen(
        [sys.executable, SERVER_SCRIPT_NAME],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    yield

    logger.info(f"Disabling HTTP Flask server from script: {SERVER_SCRIPT_NAME}")
    process.terminate()
