from interfaces.display_element import DisplayElement
from interfaces.observer import Observer


class CurrentConditionDisplayElement(DisplayElement, Observer):
    def __init__(self):        
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def display(self):
        if self.temperature:
            print(
                """
            Temperature : {0.temperature}F
            Humidity: {0.humidity}%
            Pressure: {0.pressure}Pa
            """.format(
                    self
                )
            )
        else:
            print(
                """
            Temperature : N/A
            Humidity: N/A
            Pressure: N/A
            """
            )
            

