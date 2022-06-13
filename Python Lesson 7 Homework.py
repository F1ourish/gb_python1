class Transport:
    def __init__(self, color, model, wheels, weight, velocity):
        self.__color = color
        self.__model = model
        self.__wheels = wheels
        self.__weight = weight
        self.__velocity = velocity

    def drive(self):
        return print("wroom-wroom")

    def info(self):
        return self.__color + ' ' + self.__model + ' ' + self.__wheels + ' ' + self.__weight + ' ' + self.__velocity

    def __str__(self):
        return 'Color: ' + self.__color + '\nModel: ' + self.__model + '\nWheels: ' + self.__wheels + '\nWeight: '\
               + self.__weight + '\nTop speed: ' + self.__velocity


class Automobile(Transport):
    def __init__(self, color, model, wheels, weight, velocity):
        super().__init__(color, model, wheels, weight, velocity)

    def drive(self):
        return print("wroom-wroom")

    def __str__(self):
        return super(Automobile, self).__str__()


class Motorcycle(Transport):
    def __init__(self, color, model, wheels, weight, velocity):
        super().__init__(color, model, wheels, weight, velocity)

    def drive(self):
        return print("wroom-wroom")

    def __str__(self):
        return super(Motorcycle, self).__str__()


class Truck(Transport):
    def __init__(self, color, model, wheels, weight, velocity):
        super().__init__(color, model, wheels, weight, velocity)

    def drive(self):
        return print("wroom-wroom")

    def __str__(self):
        return super(Truck, self).__str__()


class Bicycle(Transport):
    def __init__(self, color, model, wheels, weight, velocity):
        super().__init__(color, model, wheels, weight, velocity)

    def drive(self):
        return print("wroom-wroom")

    def __str__(self):
        return super(Bicycle, self).__str__()


class Program:
    automobile = Automobile('Red', 'Mazda RX7', '4', '1 134 kg', '255 km/h')
    motorcycle = Motorcycle('Blue', 'Kawasaki Ninja 400', '2', '167 kg', '315 km/h')
    truck = Truck('Black', 'Volvo FH16', '6', '167 kg', '315 km/h')
    bicycle = Bicycle('Green', 'Montague Allston', '2', '13.6 kg', '80 km/h')
    print(automobile)
    automobile.drive()
    print()
    print(motorcycle)
    motorcycle.drive()
    print()
    print(truck)
    truck.drive()
    print()
    print(bicycle)
    bicycle.drive()

