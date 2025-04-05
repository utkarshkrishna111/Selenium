#scope = class makes sure the yield statements runs only once after class is initialized and once after all test cases are completed

import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]

@pytest.fixture(params=["Chrome","IE","Firefox"])
def crossbrowser(request):
    return request.param