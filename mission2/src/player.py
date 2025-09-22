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
        self.number = PlayerManager().get_number()
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
    pass


class SilverPlayer(Player):
    pass


class NormalPlayer(Player):
    pass


class PlayerFactory:
    def classifyPlayer(self, player: Player):
        if player.score >= 50:
            gold_player = GoldPlayer(player.name)
            gold_player.grade = "Gold"
            return gold_player
        elif player.score >= 30:
            silver_player = SilverPlayer(player.name)
            silver_player.grade = "Silver"
            return silver_player
        else:
            normal_player = NormalPlayer(player.name)
            normal_player.grade = "Normal"
            return normal_player
