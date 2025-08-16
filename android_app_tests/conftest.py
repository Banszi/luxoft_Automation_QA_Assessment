import pytest
import uiautomator2 as u2

import utils
import app_controllers
from logger_utils import logger


@pytest.fixture(scope="session")
def app_handler():
    """
    Fixture that install, runs and prepares handler to Android application.
    Fixture closes application after test session.
    """
    logger.info(f"Start application: {utils.EMULATOR_NAME}:{utils.APP_NAME}")
    handler = u2.connect(utils.EMULATOR_NAME)
    handler.app_install(utils.APP_PATH.as_posix())
    handler.app_start(utils.APP_NAME)

    yield handler

    logger.info(f"Shut down the application after test session: {utils.EMULATOR_NAME}:{utils.APP_NAME}")
    handler.app_stop(utils.APP_NAME)


@pytest.fixture(autouse=True)
def clean_all_values_in_app(app_handler):
    """
    Fixture clear all input fields in application before and after the test.
    """
    logger.info("Clear all input fields before the test")
    app_handler(resourceId=app_controllers.INPUT_FIELD_1).set_text("")
    app_handler(resourceId=app_controllers.INPUT_FIELD_2).set_text("")
    yield
    logger.info("Clear all input fields after the test")
    app_handler(resourceId=app_controllers.INPUT_FIELD_1).set_text("")
    app_handler(resourceId=app_controllers.INPUT_FIELD_2).set_text("")
