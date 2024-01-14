import pytest


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get("https://www.delta.com/")
        assert self.driver.title == "Delta Air Lines | Flights & Plane Tickets + Hotels & Rental Cars"
    
    def test_title_blog(self):
        self.driver.get('https://www.delta.com/')
        print(self.driver.title)
        