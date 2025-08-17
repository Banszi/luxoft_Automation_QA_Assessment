import requests
import json

from http import HTTPStatus
from utils import SERVER_ADDRESS, ApiEndpoints

from logger_utils import logger


def test_get_users(init_users_list):
    """Check result of GET USERS request"""
    endpoint = f"{SERVER_ADDRESS}/{ApiEndpoints.GET_USERS_ENDPOINT}"
    logger.info(f"Get users using request endpoint: {endpoint}")
    response = requests.get(endpoint)

    if response.status_code != HTTPStatus.OK:
        raise f"Get users request response status code: {response.status_code}"

    payload = json.loads(response.text)
    logger.info(f"Read users list: {payload}")
    assert payload == init_users_list, "Initial users list does not match to got one!"


def test_get_user_valid_id(init_users_list):
    """Check result of GET USER with valid ID request"""
    valid_user_id = 1
    endpoint = f"{SERVER_ADDRESS}/{ApiEndpoints.GET_USER_ENDPOINT % valid_user_id}"
    logger.info(f"Get user using request endpoint: {endpoint}")
    response = requests.get(endpoint)

    if response.status_code != HTTPStatus.OK:
        raise f"Get user request response status code: {response.status_code}"

    payload = json.loads(response.text)
    logger.info(f"Read user entry: {payload}")

    if not payload:
        raise "Get user request response is empty! There should be an user entry!"
    if len(payload) != 3:
        raise f"Get user request response has wrong length! Expected length is 3 (id, name, email), got: {len(payload)}"
    if "name" not in payload:
        raise "No 'name' field in request response!"
    if "email" not in payload:
        raise "No 'email' field in request response!"
    if "id" not in payload:
        raise "No 'id' field in request response!"

    assert payload in init_users_list, \
        f"Obtained user entry with id {valid_user_id} does not match to users list!"


def test_get_user_invalid_id():
    """Check result of GET USER with invalid ID request"""
    invalid_id = 1000
    endpoint = f"{SERVER_ADDRESS}/{ApiEndpoints.GET_USER_ENDPOINT % invalid_id}"
    logger.info(f"Get user with invalid id <{invalid_id}> using request endpoint: {endpoint}")
    response = requests.get(endpoint)

    if response.status_code != HTTPStatus.NOT_FOUND:
        raise f"Get user request response status code: {response.status_code}; expected: {HTTPStatus.NOT_FOUND}"

    invalid_id = 999
    endpoint = f"{SERVER_ADDRESS}/{ApiEndpoints.GET_USER_ENDPOINT % invalid_id}"
    logger.info(f"Get user with invalid id <{invalid_id}> using request endpoint: {endpoint}")
    response = requests.get(endpoint)

    if response.status_code != HTTPStatus.INTERNAL_SERVER_ERROR:
        raise f"Get user request response status code: {response.status_code}; expected: {HTTPStatus.INTERNAL_SERVER_ERROR}"


def test_add_user_valid_data():
    """Check result of ADD USER with valid data request"""
    user_data = {"name": "Sebastian Stach", "email": "stachseb24@gmail.com"}
    endpoint = f"{SERVER_ADDRESS}/{ApiEndpoints.ADD_USER_ENDPOINT}"
    logger.info(f"Add user: {user_data} using request endpoint: {endpoint}")
    response = requests.post(endpoint, json=user_data)

    if response.status_code != HTTPStatus.CREATED:
        raise f"Add user request response status code: {response.status_code}"

    endpoint = f"{SERVER_ADDRESS}/{ApiEndpoints.GET_USERS_ENDPOINT}"
    logger.info(f"Get users using request endpoint: {endpoint}")
    response = requests.get(endpoint)

    if response.status_code != HTTPStatus.OK:
        raise f"Get users request response status code: {response.status_code}"

    payload = json.loads(response.text)
    logger.info(f"Read users list: {payload}")

    user_id = len(payload)
    user_data["id"] = user_id

    assert user_data in payload, \
        f"Used with data: {user_data} does not appear in user list!"


def test_add_user_invalid_data():
    """Check result of ADD USER with invalid data request"""
    user_data = {"name": "Sebastian Stach"}
    endpoint = f"{SERVER_ADDRESS}/{ApiEndpoints.ADD_USER_ENDPOINT}"
    logger.info(f"Add invalid user: {user_data} using request endpoint: {endpoint}")
    response = requests.post(endpoint, json=user_data)

    if response.status_code != HTTPStatus.BAD_REQUEST:
        raise f"Add user request response status code: {response.status_code}"

    user_data = {"email": "stachseb24@gmail.com"}
    endpoint = f"{SERVER_ADDRESS}/{ApiEndpoints.ADD_USER_ENDPOINT}"
    logger.info(f"Add invalid user: {user_data} using request endpoint: {endpoint}")
    response = requests.post(endpoint, json=user_data)

    if response.status_code != HTTPStatus.BAD_REQUEST:
        raise f"Add user request response status code: {response.status_code}"
