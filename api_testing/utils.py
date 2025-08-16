
SERVER_SCRIPT_NAME = "mock_api.py"
SERVER_URL = "http://localhost"
PORT = 5003
SERVER_ADDRESS = f"{SERVER_URL}:{PORT}"


class ApiEndpoints:
    GET_USERS_ENDPOINT = "/users"
    GET_USER_ENDPOINT = "/users/%s"
    ADD_USER_ENDPOINT = "/users"
