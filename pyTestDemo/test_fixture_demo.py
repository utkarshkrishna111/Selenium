#fixtures are used as setup and teardown methods for test cases - conftest file to generalize
#fixture and make it available for all tests
#@pytest.mark.usefixtures("setup") this automatically applies to all tests
import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute this step in fixture demo")

    def test_fixtureDemo1(self):
        print("I will execute this step in fixture demo1")

    def test_fixtureDemo2(self):
        print("I will execute this step in fixture demo2")

    def test_fixtureDemo3(self):
        print("I will execute this step in fixture demo3")

    def test_fixtureDemo4(self):
        print("I will execute this step in fixture demo4")

    def test_fixtureDemo5(self):
        print("I will execute this step in fixture demo5")