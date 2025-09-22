import pytest
from ..src.player_manager import PlayerManager
from ..src.player import Player, PlayerFactory, GoldPlayer, SilverPlayer, NormalPlayer


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


@pytest.fixture
def create_10_fixture():
    fixture = Player("test")
    fixture.score = 10
    return fixture

def create_20_fixture():
    fixture = Player("test")
    fixture.score = 20
    return fixture

def create_30_fixture():
    fixture = Player("test")
    fixture.score = 30
    return fixture

def create_40_fixture():
    fixture = Player("test")
    fixture.score = 40
    return fixture

def create_50_fixture():
    fixture = Player("test")
    fixture.score = 50
    return fixture


@pytest.mark.parametrize(
    "player, expected_player",
    [
        (create_10_fixture, "Normal"),
        (create_20_fixture, "Normal"),
        (create_30_fixture, "Silver"),
        (create_40_fixture, "Silver"),
        (create_50_fixture, "Gold"),
    ],
)
def test_grade(player: Player, expected_player: Player):
    player_factory = PlayerFactory()
    
    assert False
