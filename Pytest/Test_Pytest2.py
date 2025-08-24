import pytest

@pytest.mark.usefixtures("PrintMyAge")
class Test_Pytest2():

    @pytest.mark.Sanity
    def test_Testcase3(self,fixture1):
        print("Testcase 3")

    @pytest.mark.SIT
    def test_Testcase4(self):
        print("Testcase 4")

    def test_Testcase6(self,GetUsername_New):
        #print(GetUsername[0])
        #print(GetUsername[1])
        #print(GetUsername[2])
        for eachvalue in GetUsername_New:
            print(eachvalue)