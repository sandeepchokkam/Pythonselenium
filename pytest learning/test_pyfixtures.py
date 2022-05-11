import pytest

# when we define fixture scope to class only, it will once before class is initiated and ata the end
@pytest.mark.usefixtures("browsersetup")
class Testing:
    def test_pressbutton(self):
        print("I will press button after browser is launched")
    def test_pressbutton1(self):
        print("I will press button after browser1 is launched")
    def test_pressbutton2(self):
        print("I will press button after browser2 is launched")
    def test_pressbutton3(self):
        print("I will press button after browser3 is launched")