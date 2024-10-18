class Unit:
    def __init__(self,health):
        self.__damage = 0
        self.__health = 100
        self.set_health(health)

    def get_health(self):
        return self.__health
    def set_health(self,value_health):
        self.__health = value_health
    def get_damage(self, damage):
        self.set_health({self.get_health() - 0})

class Soldier(Unit):
    def __init__(self,health):
        super().__init__(health)
    def get_damage(self, damage):
        self.set_health(self.get_health()-damage)
class Civilian(Unit):
    def __init__(self,health):
        super().__init__(health)
    def get_damage(self, damage):
        self.set_health(self.get_health() - damage * 2)
u1 = Unit(100)
u1.get_damage(5)
print(u1.get_health())
s1 = Soldier(80)
print(s1.get_health())
s1.get_damage(50)
print(s1.get_health())
c1 = Civilian(80)
print(c1.get_health())
c1.get_damage(15)
print(c1.get_health())