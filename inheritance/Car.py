class Car:
    def __init__(self,model):
        self.__model = " "
        self.set_model(model)
    def get_model(self):
        return self.__model

    def set_model(self,value_model):
        if isinstance(value_model,str):
            self.__model = value_model
        else:
            raise ValueError("Model should be string")
    def drive(self):
        print("Our car drive")
    def inform_model(self):
        print(f"Car has the following model: {self.get_model()}")

class Truck(Car):
    def __init__(self,model,fullness):
        super().__init__(model)
        self.__fullness = 0
        self.set_fullness(fullness)
    def get_fullness(self):
        return self.__fullness
    def set_fullness(self,value_fullness):
        if isinstance(value_fullness,(int,float)):
            self.__fullness = value_fullness
        else:
            raise ValueError("Fullness should be int or float")
    def load_trunk(self):
        print("Load the car's trunk")
    def unload_trunk(self):
        print("Unreload the car's trunk")

class Passenger_Car(Car):
    def __init__(self,model,navigation_system):
        super().__init__(model)
        self.__navigation_system = ' '
        self.set_navigation_system(navigation_system)

    def get_navigation_system(self):
        return self.__navigation_system
    def set_navigation_system(self,value_system):
        if isinstance(value_system,str) and value_system.isalpha():
            self.__navigation_system = value_system
        else:
            raise ValueError("Navigation system should be str")
    def switch_of_navigation_system(self):
        print("Navigation system is working")

c1 = Car("Reno")
c1.inform_model()
c2 = Truck("Kamaz",23)
c2.inform_model()
c2.load_trunk()
c2.unload_trunk()
c3 = Passenger_Car("Kia Rio",'GPS')
c3.inform_model()
c3.set_model("BMW")
c3.inform_model()
c3.switch_of_navigation_system()