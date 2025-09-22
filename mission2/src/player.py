from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.number = 0
        self.attended = [0, 0, 0, 0, 0, 0, 0]
        self.score = 0
        self.grade = None

    @abstractmethod
    def estimate(self):
        pass

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