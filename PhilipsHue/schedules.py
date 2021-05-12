#!/usr/bin/env python

from connect import *

__all__ = ["Schedules"]

class Schedules(Connect):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.schedules = self.api["schedules"]

if __name__ == "__main__":
    schedules = Schedules()
    print(schedules.schedules)
