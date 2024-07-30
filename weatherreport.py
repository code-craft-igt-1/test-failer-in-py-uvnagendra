
# This is a stub for a weather sensor. For the sake of testing 
# we create a stub that generates weather data and allows us to
# test the other parts of this application in isolation
# without needing the actual Sensor during development

class WeatherSensorStub:
    
    def humidity(self):
        return 72

    def precipitation(self):
        return 70

    def temperature_in_celsius(self):
        return 26

    def windspeed_in_kmph(self):
        return 52


def report(sensor):
    precipitation = sensor.precipitation()
    report_out = 'Sunny day'
    if sensor.temperature_in_celsius() > 25:
        if precipitation > 20 and precipitation < 60:
            report_out = 'Partly cloudy'
        elif sensor.windspeed_in_kmph() > 50:
            report_out = 'Alert: Stormy with heavy rain'
    return report_out


# Test a rainy day

def test_rainy():
    sensor_stub = WeatherSensorStub()
    weather_report = report(sensor_stub)
    print(weather_report)
    assert('rain' in weather_report)


# Test another rainy day

def test_high_precipitation_and_low_windspeed():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)
    sensor_stub = WeatherSensorStub()
    weather_report = report(sensor_stub)
    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert(len(weather_report) > 0)


if __name__ == '__main__':
    test_rainy()
    test_high_precipitation_and_low_windspeed()
    print('All is well (maybe)')
