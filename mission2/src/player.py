from abc import ABC, abstractmethod
from ..src.player_manager import PlayerManager

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.number = 0
        self.attended = [0, 0, 0, 0, 0, 0, 0]
        self.score = 0
        self.grade = None

    def set_score(self, score: int):
        self.score = score

    def attend(self, weekday: str):
        if weekday == "monday":
            self.attended[MONDAY] += 1
        elif weekday == "tuesday":
            self.attended[TUESDAY] += 1
        elif weekday == "wednesday":
            self.attended[WEDNESDAY] += 1
        elif weekday == "thursday":
            self.attended[THURSDAY] += 1
        elif weekday == "friday":
            self.attended[FRIDAY] += 1
        elif weekday == "saturday":
            self.attended[SATURDAY] += 1
        elif weekday == "sunday":
            self.attended[SUNDAY] += 1


class GoldPlayer(Player):
    def __init__(self, name, number, attended, score):
        self.name = name
        self.number = number
        self.attended = attended
        self.score = score
        self.grade = "Gold"


class SilverPlayer(Player):
    def __init__(self, name, number, attended, score):
        self.name = name
        self.number = number
        self.attended = attended
        self.score = score
        self.grade = "Silver"


class NormalPlayer(Player):
    def __init__(self, name, number, attended, score):
        self.name = name
        self.number = number
        self.attended = attended
        self.score = score
        self.grade = "Normal"


class PlayerFactory:
    def classifyPlayer(self, player: Player):
        if player.score >= 50:
            gold_player = GoldPlayer(
                player.name, player.number, player.attended, player.score
            )
            return gold_player
        elif player.score >= 30:
            silver_player = SilverPlayer(
                player.name, player.number, player.attended, player.score
            )
            return silver_player
        else:
            normal_player = NormalPlayer(
                player.name, player.number, player.attended, player.score
            )
            return normal_player
