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


def test_grade_10():
    player = Player("test")
    player.score = 10
    player_factory = PlayerFactory()
    result_player = player_factory.classifyPlayer(player)
    expected_grade = "Normal"

    assert result_player.grade == expected_grade


def test_grade_20():
    player = Player("test")
    player.score = 20
    player_factory = PlayerFactory()
    result_player = player_factory.classifyPlayer(player)
    expected_grade = "Normal"

    assert result_player.grade == expected_grade


def test_grade_30():
    player = Player("test")
    player.score = 30
    player_factory = PlayerFactory()
    result_player = player_factory.classifyPlayer(player)
    expected_grade = "Silver"

    assert result_player.grade == expected_grade


def test_grade_40():
    player = Player("test")
    player.score = 40
    player_factory = PlayerFactory()
    result_player = player_factory.classifyPlayer(player)
    expected_grade = "Silver"

    assert result_player.grade == expected_grade


def test_grade_50():
    player = Player("test")
    player.score = 50
    player_factory = PlayerFactory()
    result_player = player_factory.classifyPlayer(player)
    expected_grade = "Gold"

    assert result_player.grade == expected_grade


@pytest.mark.parametrize(
    "attended, grade, expected",
    [
        ([9, 1, 6, 2, 4, 4, 3], "Silver", False),
        ([4, 7, 2, 5, 5, 3, 6], "Gold", False),
        ([0, 0, 0, 0, 0, 0, 0], "Normal", True),
        ([0, 0, 1, 0, 0, 0, 0], "Normal", True),
        ([0, 0, 0, 0, 0, 1, 0], "Normal", True),
        ([0, 0, 0, 0, 0, 1, 1], "Normal", True),
        ([0, 0, 0, 0, 0, 0, 1], "Normal", True),
        ([0, 0, 1, 0, 0, 0, 1], "Normal", False),
    ],
)
def test_is_falling(attended, grade, expected):
    player_mgr = PlayerManager()
    result = player_mgr.is_falling(grade, attended)
    assert result == expected
