import pytest
from lesson1.api_tests.services.case.models import Case, Priority


@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:8000"


@pytest.fixture()
def path():
    return "testcases"


@pytest.fixture()
def case_data():
    return Case(
        id=1,
        name="Auto Test Case",
        description="This is a sample test case",
        priority=Priority.high,
        steps=["Step 1", "Step 2", "Step 3"],
        expected_result="Expected result of the test case"
    )
