class DivisionError(Exception):
    def __str__(self):
        return "Нельзя делить большее на меньшее"
file = open("numbers.txt")
first_string = file.readline()
value_1 = float(first_string[0])
value_2 = float(first_string[1])
if value_1 < value_2:
    raise DivisionError
else:
    print(value_1/value_2)

