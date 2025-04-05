#Any pyTest file will start with test_
#Pytest method name should start with test
#any code should be wrapped in method only
#py.test -v -s :V stands for verbose and s helps in printing all console logs
#py.test -k CreditCard -v -s: To run selected methods having creditcard name identified through regex by keyword -k
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#-k stands for method names execution, -s stands for logs in output, -v stands for more info
#Run specific file name using py.test <filename>
#@pytest.mark.xfail runs the method but does not show this in report
#fixture is used to initialize the test set up. It can initialize as well execute last step after the test completes
#the last step is determined by keyword yield
#you can skip test with @pytest.mark.skip
#fixtures are used as setup and teardown methods for test cases - conftest file to generalize
#fixture and make it available for all tests
#data driven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class in initiated and at the end

import pytest

@pytest.mark.smoke
def test_firstprogram():
    print("Hello")

@pytest.mark.xfail
def test_greetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossbrowser):
    print(crossbrowser)




