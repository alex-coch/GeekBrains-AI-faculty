class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        print('Car starts driving')

    @staticmethod
    def stop():
        print('Car stopped')

    @staticmethod
    def turn(direction):
        print('Car turns', direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Speed limit exceeded')
        else:
            print(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Speed limit exceeded')
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


tcar = TownCar(100, 'red', 'lada', False)
tcar.show_speed()

scar = SportCar(200, 'green', 'f1', False)
scar.go()
scar.show_speed()

wcar = WorkCar(50, 'black', 'man', False)
wcar.show_speed()

pcar = PoliceCar(60, 'white', 'niva', True)
pcar.turn('left')
pcar.stop()
