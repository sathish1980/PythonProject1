import pytest


@pytest.fixture
def fixture1():
    print(10)
    print(20)
    print(30)
    yield
    print("Post execution")

@pytest.fixture
def PrintMyAge():
    print("My age is : ", 30)
    yield
    print("Post execution")

@pytest.fixture
def GetUsername():
    return["sathish","kumar","R"]

@pytest.fixture(params=[("sathish","Password"),("kumar","pass"),("R","P")])
def GetUsername_New(request):
    return request.param

