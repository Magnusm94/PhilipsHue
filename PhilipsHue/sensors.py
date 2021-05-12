#!/usr/bin/env python
from connect import Connect

__all__ = ["Sensors"]

class Sensors(Connect):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.sensors = self.api["sensors"]


if __name__ == "__main__":
    pass

