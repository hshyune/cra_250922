MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class PlayerManager:
    id = 0
    def get_number(self):
        self.id += 1
        return self.id
    def init(self):
        self.id = 0
    
    def scoring(self, attended: list):
        score = 0
        # scoring attended
        score += attended[MONDAY] * 1
        score += attended[TUESDAY] * 1
        score += attended[WEDNESDAY] * 3
        score += attended[THURSDAY] * 1
        score += attended[FRIDAY] * 1
        score += attended[SATURDAY] * 2
        score += attended[SUNDAY] * 2

        # bonus scoring
        if(attended[WEDNESDAY] >= 10):
            score += 10
        if(attended[SATURDAY] + attended[SUNDAY] >= 10):
            score += 10
        return score

    def is_falling(self, grade, attended):
        if(grade == "Normal"):
            if(attended[WEDNESDAY] == 0) or (attended[SATURDAY] + attended[SUNDAY] == 0):
                return True
        return False