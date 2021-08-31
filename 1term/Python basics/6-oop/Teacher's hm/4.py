class Car:
    """Автомобиииль !!!"""

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Новая машина: {self.name} (Цвет {self.color}) машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала")

    def stop(self):
        print(f"{self.name}: Машина остановилась")

    def turn(self, direction):
        print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f"{self.name}: Скорость автомобиля - {self.speed}")

class WorkCar(Car):

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}" # super().show_speed()


class SportCar(Car):
    """Спортивный автомобилб"""

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar('ДПС', 'Белый', 80)
police_car.go()
