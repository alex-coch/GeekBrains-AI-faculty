import time


class TrafficLight:
    __color = 'Red'

    @classmethod
    def running(cls):
        print(cls.__color)
        if cls.__color == 'Red':
            cls.__color = 'Yellow'
        elif cls.__color == 'Yellow':
            cls.__color = 'Green'


obj = TrafficLight()

obj.running()
time.sleep(7)
obj.running()
time.sleep(2)
obj.running()
