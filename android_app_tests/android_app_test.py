import app_controllers
from logger_utils import logger


def test_get_app_info_and_hierarchy(app_handler):
    """Check that Android app info and hierarchy are available"""
    logger.info(f"Android application data: {app_handler.info}")
    logger.info(f"Android application tree: {app_handler.dump_hierarchy()}")


def test_first_input_field_init_value(app_handler):
    """Check that first input field contains correct initial prompt"""
    init_text_of_first_field = "Enter the first number"
    read_text = app_handler(resourceId=app_controllers.INPUT_FIELD_1).get_text()
    assert read_text == init_text_of_first_field, \
        f"Init value in input field 1 should be: {init_text_of_first_field}; got: {read_text}"


def test_second_input_field_init_value(app_handler):
    """Check that second input field contains correct initial prompt"""
    init_text_of_second_field = "Enter the second number"
    read_text = app_handler(resourceId=app_controllers.INPUT_FIELD_2).get_text()
    assert read_text == init_text_of_second_field, \
        f"Init value in input field 2 should be: {init_text_of_second_field}; got: {read_text}"


def test_first_input_field_valid_value(app_handler):
    """Check behavior of first input field in case of valid value"""
    valid_value = "1"
    app_handler(resourceId=app_controllers.INPUT_FIELD_1).set_text(valid_value)
    # app_handler(resourceId=app_controllers.INPUT_FIELD_1).wait(timeout=5)
    read_text = app_handler(resourceId=app_controllers.INPUT_FIELD_1).get_text()
    assert read_text == valid_value, \
        f"Input field 1 should contain following value: {valid_value}; got: {read_text}"


def test_second_input_field_valid_value(app_handler):
    """Check behavior of second input field in case of valid value"""
    valid_value = "2"
    app_handler(resourceId=app_controllers.INPUT_FIELD_2).set_text(valid_value)
    # app_handler(resourceId=app_controllers.INPUT_FIELD_1).wait(timeout=5)
    read_text = app_handler(resourceId=app_controllers.INPUT_FIELD_2).get_text()
    assert read_text == valid_value, \
        f"Input field 2 should contain following value: {valid_value}; got: {read_text}"


def test_first_input_field_invalid_value(app_handler):
    """Check behavior of first input field in case of invalid value"""
    invalid_value = "@"
    init_text_of_first_field = "Enter the first number"
    app_handler(resourceId=app_controllers.INPUT_FIELD_1).set_text(invalid_value)
    # app_handler(resourceId=app_controllers.INPUT_FIELD_1).wait(timeout=5)
    read_text = app_handler(resourceId=app_controllers.INPUT_FIELD_1).get_text()
    assert read_text == init_text_of_first_field, \
        f"Input field 1 should contain following value: {init_text_of_first_field}; got: {read_text}"


def test_second_input_field_invalid_value(app_handler):
    """Check behavior of second input field in case of invalid value"""
    invalid_value = "A"
    init_text_of_second_field = "Enter the second number"
    app_handler(resourceId=app_controllers.INPUT_FIELD_2).set_text(invalid_value)
    # app_handler(resourceId=app_controllers.INPUT_FIELD_1).wait(timeout=5)
    read_text = app_handler(resourceId=app_controllers.INPUT_FIELD_2).get_text()
    assert read_text == init_text_of_second_field, \
        f"Input field 2 should contain following value: {init_text_of_second_field}; got: {read_text}"


def test_init_value_of_res_field(app_handler):
    """Check that correct initial value is set in result field"""
    init_value = "0"
    read_text = app_handler(resourceId=app_controllers.RESULT_FIELD).get_text()
    assert read_text == init_value, \
        f"Init value of result field should be an empty string; got: {read_text}"


def test_add_button(app_handler):
    """Check that ADD button works as expected - calculation of two valid values"""
    first_in_field_valid_val = "1"
    second_in_field_valid_val = "2"
    expected_value = str(float(int(first_in_field_valid_val) + int(second_in_field_valid_val)))
    app_handler(resourceId=app_controllers.INPUT_FIELD_1).set_text(first_in_field_valid_val)
    app_handler(resourceId=app_controllers.INPUT_FIELD_2).set_text(second_in_field_valid_val)
    app_handler(resourceId=app_controllers.ADD_BUTTON).click()
    read_text = app_handler(resourceId=app_controllers.RESULT_FIELD).get_text()
    assert expected_value == read_text, \
        f"Add numbers: {first_in_field_valid_val} and {second_in_field_valid_val}. " \
        f"Expected result: {expected_value}; got: {read_text}"


def test_sub_button(app_handler):
    """Check that SUB button works as expected - calculation of two valid values"""
    first_in_field_valid_val = "2"
    second_in_field_valid_val = "1"
    expected_value = str(float(int(first_in_field_valid_val) - int(second_in_field_valid_val)))
    app_handler(resourceId=app_controllers.INPUT_FIELD_1).set_text(first_in_field_valid_val)
    app_handler(resourceId=app_controllers.INPUT_FIELD_2).set_text(second_in_field_valid_val)
    app_handler(resourceId=app_controllers.SUB_BUTTON).click()
    read_text = app_handler(resourceId=app_controllers.RESULT_FIELD).get_text()
    assert expected_value == read_text, \
        f"Sub numbers: {first_in_field_valid_val} and {second_in_field_valid_val}. " \
        f"Expected result: {expected_value}; got: {read_text}"


def test_div_button(app_handler):
    """Check that DIV button works as expected - calculation of two valid values"""
    first_in_field_valid_val = "10"
    second_in_field_valid_val = "5"
    expected_value = str(float(int(first_in_field_valid_val) / int(second_in_field_valid_val)))
    app_handler(resourceId=app_controllers.INPUT_FIELD_1).set_text(first_in_field_valid_val)
    app_handler(resourceId=app_controllers.INPUT_FIELD_2).set_text(second_in_field_valid_val)
    app_handler(resourceId=app_controllers.DIV_BUTTON).click()
    read_text = app_handler(resourceId=app_controllers.RESULT_FIELD).get_text()
    assert expected_value == read_text, \
        f"Div numbers: {first_in_field_valid_val} and {second_in_field_valid_val}. " \
        f"Expected result: {expected_value}; got: {read_text}"


def test_mul_button(app_handler):
    """Check that MUL button works as expected - calculation of two valid values"""
    first_in_field_valid_val = "2"
    second_in_field_valid_val = "5"
    expected_value = str(float(int(first_in_field_valid_val) * int(second_in_field_valid_val)))
    app_handler(resourceId=app_controllers.INPUT_FIELD_1).set_text(first_in_field_valid_val)
    app_handler(resourceId=app_controllers.INPUT_FIELD_2).set_text(second_in_field_valid_val)
    app_handler(resourceId=app_controllers.MUL_BUTTON).click()
    read_text = app_handler(resourceId=app_controllers.RESULT_FIELD).get_text()
    assert expected_value == read_text, \
        f"Mul numbers: {first_in_field_valid_val} and {second_in_field_valid_val}. " \
        f"Expected result: {expected_value}; got: {read_text}"
