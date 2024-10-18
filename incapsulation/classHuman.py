class Human:
    __count = 0
    def __init__(self,name,age):
        self.__name = " "
        self.__age = 0
        self.set_name(name)
        self.set_age(age)
        Human.__count += 1

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self,value_name):
        if isinstance(value_name,str) and value_name.isalpha():
            self.__name = value_name
        else:
            raise TypeError("Need another data type:Name must be string ")

    def set_age(self,value_age):
        if isinstance(value_age,(int,float)) and 1<value_age<100:
            self.__age = value_age
        else:
            raise Exception("Error in set_age.Be carefully")

    def __str__(self):
        return f"Name: {self.get_name()}, Age: {self.get_age()};"

h1 = Human("Jack",23)
print(h1)
h1.set_age(55)
print(h1)
h1._Human__age = 98
print(h1)
