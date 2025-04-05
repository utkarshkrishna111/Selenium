#if your fixture is returing, the the fixture name must be passed into method: def test_editProfile(self,dataload)

import pytest

@pytest.mark.usefixtures("dataload")
class TestExample4:

    def test_editProfile(self,dataload):
        print(dataload)
