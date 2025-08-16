import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

import uiautomator2 as u2
from behave import given, when, then
import app_controllers
from logger_utils import logger
import utils


@given("the app is running")
def step_app_running(context):
    logger.info(f"Start application: {utils.EMULATOR_NAME}:{utils.APP_NAME}")
    handler = u2.connect(utils.EMULATOR_NAME)
    handler.app_install(utils.APP_PATH.as_posix())
    handler.app_start(utils.APP_NAME)

    context.handler = handler


@when("I read the text of the first input field")
def step_read_input_field(context):
    context.read_text = context.handler(resourceId=app_controllers.INPUT_FIELD_1).get_text()
    logger.info(f"Read first input field text: {context.read_text}")


@then("the text should be 'Enter the first number'")
def step_check_text(context):
    expected_text = "Enter the first number"
    assert context.read_text == expected_text, \
        f"Init value in input field 1 should be: {expected_text}; got: {context.read_text}"
