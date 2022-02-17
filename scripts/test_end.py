import pytest

from utils import UtilsDriver


@pytest.mark.run(order=1999)
class TestEnd:
    def test_end(self):
        UtilsDriver.set_quit_driver(True)
        UtilsDriver.quit_steam_driver()
