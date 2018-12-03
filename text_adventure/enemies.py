class Enemies(object):
    def __init__(self, name, description, hp, damage, test):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self.test = test
    
class Squatter(Enemies):
    def __init__(self):
        pass