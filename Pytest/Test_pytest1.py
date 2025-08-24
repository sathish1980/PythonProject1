import pytest

@pytest.mark.usefixtures("fixture1")
class Test_pytest1():

    @pytest.mark.Sanity
    def test_testcase1(self):
        print("Testcase1")

    @pytest.mark.Sanity
    @pytest.mark.run(order=1)
    def test_testcase2(self):
        print("Testcase2")

