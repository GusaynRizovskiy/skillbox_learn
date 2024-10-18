class Robot:
    def __init__(self,model):
        self.__model = " "
        self.set_model(model)
    def get_model(self):
        return self.__model
    def set_model(self,value_model):
        if isinstance(value_model,str):
            self.__model = value_model
        else:
            raise ValueError("Model should be str")
    def operate(self):
        print("I am a Robot and I do what you say")

class Robot_Pylesos(Robot):
    def __init__(self,model):
        super().__init__(model)
        self.__bag = 0
    def operate(self):
        self.__bag +=1
        print(f"I am vacuuming and fullness of bag is {self.__bag}")

class Robot_Security(Robot):
    def __init__(self,model):
        super().__init__(model)
    def operate(self):
        print("I'm patrolling your home right now")

class Robot_For_Pool(Robot_Security):
    def __init__(self,model):
        super().__init__(model)
    def operate(self):
        print(f"I'm patrolling your home and pool right now")

r1 = Robot("Bibi")
print(r1.get_model())
r1.operate()
r2 = Robot_Pylesos("Jaki")
print(r2.get_model())
r2.operate()
r3 = Robot_Security("Fantom")
print(r3.get_model())
r3.operate()
r4= Robot_For_Pool("Ihtiandor")
print(r4.get_model())
r4.operate()
