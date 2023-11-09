class Person:
    def __init__(self, name):
        self.name = name    # устанавливаем имя
        self.age = 1        # устанавливаем возраст

    def display_info(self):
        print(f"Имя: {self.name}\tВозраст: {self.age}")


petr = Person("Петр")
petr.name = "Катя"       # изменяем атрибут name
petr.age = -129          # изменяем атрибут age
petr.display_info()

class Person:
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1  # устанавливаем возраст

    def set_age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


petr = Person("Петр")
petr.display_info()
petr.set_age(-3486)  # Недопустимый возраст
petr.set_age(25)
petr.display_info()

petr.__age = 23

print(petr.__age)

def get_age(self):
    return self.__age
    
def set_age(self, age):
    if 1 < age < 110:
        self.__age = age
    else:
        print("Недопустимый возраст")
        
class Person:
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1  # устанавливаем возраст

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


petr = Person("Петр")

petr.display_info()
petr.age = -3486  # Недопустимый возраст
print(petr.age)
petr.age = 36
petr.display_info()