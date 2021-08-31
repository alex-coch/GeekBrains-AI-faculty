from time import sleep


# class TrafficLight:
#     __color = "Черный"
#
#     def running(self):
#         while True:
#             print('Красный')
#             sleep(7)
#             print('Желтый')
#             sleep(2)
#             print('Зеленый')
#             sleep(7)
#             print('Желтый')
#             sleep(2)
#
#
# trafficlight = TrafficLight()
# trafficlight.running()




#------------------------------------------------------------------------------

import time
import itertools

class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])


trafficlight = TrafficLight()
trafficlight.running()