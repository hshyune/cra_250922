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
    
    def scoring(attended: list):
        return 0