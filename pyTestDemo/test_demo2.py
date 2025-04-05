#Any pyTest file will start with test_
#Pytest method name should start with test
#any code should be wrapped in method only
#py.test -v -s :V stands for verbose and s helps in printing all console logs
#py.test -k CreditCard -v -s: To run selected methods having creditcard name identified through regex by keyword -k
#-k stands for method names execution, -s stands for logs in output, -v stands for more info
#Run specific file name using py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip test with @pytest.mark.skip
#fixture is used to initialize the test set up. It can initialize as well execute last step after the test completes
#the last step is determined by keyword yield
#fixtures are used as setup and teardown methods for test cases - conftest file to generalize
#fixture and make it available for all tests
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg="Hello"
    assert msg == "Hi", "Test Failed because strings do not match"

def test_second_CreditCard(setup):
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

