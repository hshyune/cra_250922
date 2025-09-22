import pytest
from ..src.score import Score
from ..src.player import Player


@pytest.mark.parametrize(
    "attended, expected_score",
    [
        ([9, 1, 18, 2, 4, 8, 6], 68),
        ([4, 7, 6, 5, 5, 6, 12], 55),
        ([8, 8, 21, 7, 1, 10, 6], 81),
        ([10, 9, 15, 5, 8, 26, 8], 101),
        ([1, 2, 9, 0, 3, 2, 6], 23),
        ([3, 10, 30, 12, 10, 24, 18], 127),
        ([6, 3, 12, 7, 4, 4, 8], 64),
        ([0, 2, 6, 0, 2, 8, 4], 32),
        ([4, 5, 15, 6, 8, 12, 4], 74),
        ([5, 6, 18, 7, 6, 6, 10], 78),
    ],
)
def test_scoring(attended: list, expected_score: int):
    result = Score.estimate(attended)
    assert result == expected_score
