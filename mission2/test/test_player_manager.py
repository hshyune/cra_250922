import pytest
from ..src.player_manager import PlayerManager
from ..src.player import Player

@pytest.mark.parametrize("id", [1, 3, 5, 7, 100, 5000])
def test_player_number(id: int):
    player_mgr = PlayerManager()
    player_mgr.init()

    for i in range(id - 1):
        player_mgr.get_number()
    assert id == player_mgr.get_number()



@pytest.mark.parametrize(
    "attended, expected_score",
    [
        ([9, 1, 6, 2, 4, 4, 3], 48),
        ([4, 7, 2, 5, 5, 3, 6], 45),
        ([8, 8, 7, 7, 1, 5, 3], 61),
        ([10, 9, 5, 5, 8, 13, 4], 91),
        ([1, 2, 3, 0, 3, 1, 3], 23),
        ([3, 10, 10, 12, 10, 12, 9], 127),
        ([6, 3, 4, 7, 4, 2, 4], 44),
        ([0, 2, 2, 0, 2, 4, 2], 22),
        ([4, 5, 5, 6, 8, 6, 2], 54),
        ([5, 6, 6, 7, 6, 3, 5], 58),
    ],
)
def test_scoring(attended: list, expected_score: int):
    player_mgr = PlayerManager()

    assert player_mgr.scoring(attended) == expected_score