# Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed
# some data to the tests such as database connections, URLs to test and some sort of input data. Therefore,
# instead of running the same code for every test, we can attach fixture function to the tests and it will run and
# return the data to the test before executing each test Tear down is nothing but, executing the statements at last
# of every test where this fixture is applied. we can achieve this by giving statements after yield

# Fixtures are used as setup and teardown methods for test cases- conftest file to generalize fixture and make it available to all test cases
import pytest


@pytest.fixture(scope="class")
def browsersetup():
    print("I will be launching the browser")
    yield
    print("I will close the browser once work is done")
    print("I am sandeep")


@pytest.fixture()
def dataload():
    print("I am loading the data")
    return [1, 2, 3, 4]

# Parameterization
@pytest.fixture(params=[('chrome', 'sandeep', 'chokkam'), ('edge', 'chokkam', 'sandeep'), ('IE', 'sandeep', 'chokkam')])
def senddata(request):
    print('I am sending browser types')
    return request.param
