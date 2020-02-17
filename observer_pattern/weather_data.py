from typing import List
from interfaces.observer import Observer 
from interfaces.subject import Subject


class WeatherData(Subject):
    def __init__(self, temperature=None, humidity=None, pressure=None):
        self.observers = list() 
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure

    def registerObserver(self, observer: Observer):
        self.observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.observers.remove(observer)

    def _notify(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def setData(
        self,
        temperature,
        humidity,
        pressure
    ):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self._notify()
