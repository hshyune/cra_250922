import pytest
from ..src.player_manager import IdManager

@pytest.mark.parametrize("id", [1, 3, 5, 7, 100, 5000])
def test_player_number(id: int):
    id_mgr = IdManager()
    id_mgr.init()

    for i in range(id - 1):
        id_mgr.get_number()
    assert id == id_mgr.get_number()
