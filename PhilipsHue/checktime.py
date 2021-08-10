#!/usr/bin/env python
from datetime import datetime

__all__ = ["TimeRules"]

class TimeRules:
    """
    A first attempt to create rules for Philips Hue simulating daylight.
    Attempts to set brightness and color temperature to blue increasing as sunrise, and orange decreasing sunset.
    """
    start = 7  # Clock when lights turn on
    end = 22  # Clock when lights turn off. Doesn't understand if clock is after midnight.
    peak_brightness_time = 14  # Clock during the day when brightness is at max.
    peak_brightness = 0.6  # Maximum brightness during day representing percentage of max. 0.6 = 60%

    def __init__(self, *args, **kwargs):
        self.on_time = (self.end - self.start) * 60
        self()

    def __call__(self):
        self.GetTime()
        self.GetColor()
        self.GetBrightness()

    def GetTime(self):
        self.hour = datetime.now().hour
        self.minute = datetime.now().minute
        self.minutes_since_start = (self.hour - self.start) * 60 + self.minute

    def GetColor(self):
        """
        Checks time, and calculates color temperature.
        """
        through_day = self.minutes_since_start / self.on_time
        self.temperature = int((454 - 153) * through_day + 153)
        return self.temperature

    def GetBrightness(self):
        """
        Calculates brightness based on current time and when during the day the brightness should peak.
        """
        self.brightness_peak_minutes = (self.peak_brightness - self.start) * 60
        if self.minutes_since_start < self.brightness_peak_minutes:
            self.brightness = self.peak_brightness * (self.minutes_since_start / self.brightness_peak_minutes)
        else:
            total_minutes = (self.end - self.peak_brightness_time) * 60
            minutes_since_peak = (self.hour - self.peak_brightness_time) * 60 + self.minute
            brightness_percent = self.peak_brightness - self.peak_brightness * (minutes_since_peak / total_minutes)
            self.brightness = int(brightness_percent * 254)
        if self.brightness <= 0:
            self.brightness = 0

if __name__ == "__main__":
    t = TimeRules()
    print(t.brightness)
    print(t.temperature)
