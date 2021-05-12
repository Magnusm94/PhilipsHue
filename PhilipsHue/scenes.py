#!/usr/bin/env python
from connect import *

__all__ = ["Scenes"]

class Scenes(Connect):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.scenes = self.api["scenes"]


if __name__ == "__main__":
    pass


