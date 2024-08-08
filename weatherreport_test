"""
Unit tests for the weather report functionality.
"""

import unittest
from weatherreport import (
    WeatherSensorStub,
    report
)

class TestWeatherReport(unittest.TestCase):
    """Unit tests for the weather report functionality."""
    def test_rainy(self):
        """Test the weather report for a rainy day."""
        sensor_stub = WeatherSensorStub(
            temperature_in_celsius=26,
            precipitation=70,
            windspeed_in_kmph=52
        )
        weather_report = report(sensor_stub)
        self.assertIn('rain', weather_report)

    def test_high_precipitation_and_low_windspeed(self):
        """Test the weather report for high precipitation and low windspeed."""
        sensor_stub = WeatherSensorStub(
            temperature_in_celsius=26,
            precipitation=70,
            windspeed_in_kmph=48
        )
        weather_report = report(sensor_stub)
        self.assertTrue(len(weather_report) > 0 and 'rain' in weather_report)

if __name__ == '__main__':
    unittest.main()
