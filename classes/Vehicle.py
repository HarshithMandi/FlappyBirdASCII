from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed
    @abstractmethod
    def Start(self):
        pass