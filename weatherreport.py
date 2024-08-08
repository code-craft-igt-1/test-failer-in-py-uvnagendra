"""
This module contains a stub for a weather sensor and a function to generate weather reports.
The WeatherSensorStub class simulates weather data for testing purposes.
The report function generates a weather report based on the sensor data.
"""

class WeatherSensorStub:
    """
    A stub class to simulate weather sensor data for testing purposes.
    """

    def __init__(self, humidity=0, precipitation=0, temperature_in_celsius=0, windspeed_in_kmph=0):
        self.humidity = humidity
        self.precipitation = precipitation
        self.temperature_in_celsius = temperature_in_celsius
        self.windspeed_in_kmph = windspeed_in_kmph

    def get_temperature(self):
        """
        Get the current temperature in Celsius.

        Returns:
            int: The temperature in Celsius.
        """
        return self.temperature_in_celsius

    def get_precipitation(self):
        """
        Get the current precipitation level.

        Returns:
            int: The precipitation level.
        """
        return self.precipitation

    def get_humidity(self):
        """
        Get the current humidity level.

        Returns:
            int: The humidity level.
        """
        return self.humidity

    def get_wind_speed(self):
        """
        Get the current wind speed in km/h.

        Returns:
            int: The wind speed in km/h.
        """
        return self.windspeed_in_kmph

def report(sensor):
    """
    Generate a weather report based on the sensor data.

    Args:
        sensor (WeatherSensorStub): The weather sensor stub instance.

    Returns:
        str: The weather report.
    """
    report_out = 'Sunny day'
    if sensor.temperature_in_celsius > 25:
        if 20 < sensor.precipitation < 60:
            report_out = 'Partly cloudy'
        elif sensor.windspeed_in_kmph > 50:
            report_out = 'Alert: Stormy with heavy rain'
    return report_out
