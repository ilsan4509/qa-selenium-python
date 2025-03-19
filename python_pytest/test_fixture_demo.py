import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fisxture_demo_01(self):
        print("I will execute steps in fixture_demo_01 method")

    def test_fisxture_demo_02(self):
        print("I will execute steps in fixture_demo_02 method")

    def test_fisxture_demo_03(self):
        print("I will execute steps in fixture_demo_03 method")

    def test_fisxture_demo_04(self):
        print("I will execute steps in fixture_demo_04 method")