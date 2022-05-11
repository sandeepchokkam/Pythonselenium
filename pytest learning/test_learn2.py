# any pytest file should start with test_ or end with _test what ever code that we write in pytest, we have to write
# in functions and that function name should start with test_ Any code should be wrapped in method only -k is to
# select specific test methods or test cases which is having that particular name ex:- py.test -k second -v is
# verbose, to display cachedir, rootdir (more info like metadata) -s is to display the passed or failed status
# clearly (logs in output) we can run specific files by passing that file name after py.test. EX:- py.test
# test_learn2.py -v -s we can mark (tag) tests @pytest.mark.smoke and then run with -m EX:- py.test -m smoke we can
# skip tests with the tag @pytest.mark.skip we can run the tests even though it is passing or failing it will be not
# reported in report(logs) by using command @pytest.mark.xfail

# test method
import pytest


@pytest.mark.xfail
def test_secondprog():
    print("this one executed")
    msg = "sandeep"
    assert msg == "sandee", "failed because string is not matching"


@pytest.mark.smoke
@pytest.mark.skip
def test_checkadd():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition does not match"

