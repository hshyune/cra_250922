from abc import ABC, abstractmethod

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6


class Player(ABC):
    def __init__(self, name):
        self.id = 0
        self.name = name
        self.number = 0
        self.attended = [0, 0, 0, 0, 0, 0, 0]
        self.score = 0
        self.grade = None

    @abstractmethod
    def estimate(self):
        pass

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
    def estimate(self):
        self.grade = "Gold"
        return super().estimate()


class SilverPlayer(Player):
    def estimate(self):
        self.grade = "Silver"
        return super().estimate()


class NormalPlayer(Player):
    def estimate(self):
        self.grade = "Normal"
        return super().estimate()

class PlayerFactory:
    def classifyPlayer(self, player: Player):
        if player.score >= 50:
            return GoldPlayer()
        elif player.score >= 30:
            return SilverPlayer()
        else:
            return NormalPlayer()
    