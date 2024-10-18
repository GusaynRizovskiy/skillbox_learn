class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self,value_x):
        if value_x == int:
            self.__x = value_x
        else:
            raise TypeError("Ошибка типа данных, переменная должна быть int")

    def set_Y(self,value_y):
        if value_y == int:
            self.__y == value_y
        else:
            raise TypeError("Ошибка типа данных, переменная должна быть int")

    def __str__(self):
        return f"X = {self.get_x()} Y = {self.get_y()};"

p1 = Point(5,10)
p2 = Point(10,20)
print(p1,p2)
p3 = Point(5,20)
p3.set_Y('t')
print(p3)