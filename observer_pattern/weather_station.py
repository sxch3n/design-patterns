from weather_data import WeatherData
from current_condition_display_element import CurrentConditionDisplayElement


wd = WeatherData(67,23,30)
cd = CurrentConditionDisplayElement()
wd.registerObserver(cd)
cd.display()
wd.setData(70,23,30)
cd.display()
wd.removeObserver(cd)
wd.setData(70,39,41)
cd.display()