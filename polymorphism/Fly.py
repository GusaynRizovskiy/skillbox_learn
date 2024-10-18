class CanFly:
    def __init__(self,high,speed):
        self.__high = 0
        self.__speed = 0
        self.set_high(high)
        self.set_speed(speed)
    def get_high(self):
        return self.__high
    def get_speed(self):
        return self.__speed
    def set_high(self,value_high):
        self.__high = value_high
    def set_speed(self,value_speed):
        self.__speed = value_speed
    def take_off(self):
        pass
    def fly(self):
        pass
    def to_land(self):
        self.set_high(0)
        self.set_speed(0)
    def __str__(self):
        return f"High = {self.get_high()}, Speed = {self.get_speed()};"

class Butterfly(CanFly):
    def __init__(self,high,speed):
        super().__init__(high,speed)
    def take_off(self):
        self.set_high(1)
    def fly(self):
        self.set_speed(0.5)
class Racket(CanFly):
    def __init__(self,high,speed):
        self.__init__(high,speed)
    def take_off(self):
        self.set_speed(500)
    def to_land(self):
        self.set_high(0)
        print("Взрыв")
    def exposion(self):
        self.set_high(10000)
        self.set_speed(43442)

