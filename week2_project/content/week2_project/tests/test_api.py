import pytest
from week2_project.api_client import get_data
from week2_project.validators import validate_status, validate_schema
from week2_project.logger import log_result

@pytest.fixture
def valid_response():
    return get_data("/posts")

@pytest.fixture
def invalid_response():
    return get_data("/invalid")

def test_status_code(valid_response):
    status, msg = validate_status(valid_response)
    log_result("Test Status Code", status, msg)
    assert status, msg

def test_schema(valid_response):
    status, msg = validate_schema(valid_response)
    log_result("Test Schema Validation", status, msg)
    assert status, msg

def test_invalid_endpoint(invalid_response):
    status, msg = validate_status(invalid_response)
    log_result("Test Invalid Endpoint", status, msg)
    assert not status, "Expected failure for invalid endpoint"
