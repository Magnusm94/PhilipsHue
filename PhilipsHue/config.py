#!/usr/bin/env python
from connect import Connect

__all__ = ["ListApiGroups"]

class ListApiGroups(Connect):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.groups = self.api.keys()

if __name__ == "__main__":
    pass


