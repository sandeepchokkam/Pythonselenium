# any pytest file should start with test_ or end with _test
# what ever code that we write in pytest, we have to write in functions and that function name should start with test_
# Any code should be wrapped in method only

# test method
import pytest


@pytest.mark.smoke
def test_firstprog():
    print("hello")


def test_secondprog():
    msg = "sandeep"
    assert msg == "sandeep", "failed because string is not matching"
