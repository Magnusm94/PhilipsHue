#!/usr/bin/env python
from connect import Connect

__all__ = ["Resourcelinks"]

class Resourcelinks(Connect):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resourcelinks = self.api["resourcelinks"]

if __name__ == "__main__":
    pass

