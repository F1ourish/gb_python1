class Cat:
    __name = "Barsik"
    __height = 21
    __weight = 4.6
    __tail = True
    __color = "Red"

    def __init__(self, name, height, weight, tail, color):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__tail = tail
        self.__color = color

    def do_meow(self):
        print("Meow!")

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_tail(self):
        return self.__tail

    def get_color(self):
        return self.__color

    def set_name(self):
        name = input("Name: ")
        if name != "" and name.isspace() is False:
            self.__name = name
        else:
            print("You're not entered the name.")

    def set_height(self):
        height = int(input("Height: "))
        if height > 0:
            self.__height = height

    def set_weight(self):
        weight = float(input("Weight: "))
        if weight > 0:
            self.__weight = round(float(weight), 2)

    def set_color(self):
        color = input("Color: ")
        if color != "" and color.isspace() is False:
            self.__color = color
        else:
            print("You're not entered the color.")


def print_cat_info(my_cat):
    print("\nCat info:\n", f"Name: {my_cat.get_name()}, height: {my_cat.get_height()}, weight: {my_cat.get_weight()}"
                           f" kg, tail: {my_cat.get_tail()}, color: {my_cat.get_color()}")


my_cat = Cat("Barsik", 21, 4.6, True, "Red")
print_cat_info(my_cat)
my_cat.do_meow()
print("\nEnter your cat's parameters.\n")
my_cat.set_name()
my_cat.set_height()
my_cat.set_weight()
my_cat.set_color()
print_cat_info(my_cat)
my_cat.do_meow()
