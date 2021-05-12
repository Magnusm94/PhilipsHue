#!/usr/bin/env python
from connect import *

__all__ = ["Groups"]

class Groups(Connect):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.groups = self.api["groups"]

    def Group_Search_By_Name(self, groupname):
        for key, value in self.groups.items():
            if value["name"] == groupname:
                yield key

    def SetGroup(self, groupname, *args):
        for i in self.__Group_Search_By_Name(groupname):
            if self.groups[i]["lights"] == list(args):
                return
            else:
                self.DeleteGroup(groupname)
        self.conn.create_group(groupname, list(args))

    def GetGroup(self, *args):
        group_keys = set()
        data = {}
        for arg in args:
            for key in self.__Group_Search_By_Name(arg):
                group_keys.add(key)
        for key in group_keys:
            data.__setitem__(key, self.groups[str(key)])
        return

    def DeleteGroup(self, *args):
        for arg in args:
            for i in self.__Group_Search_By_Name(arg):
                self.conn.delete_group(str(i))

    def SwitchGroup(self, *args):
        for arg in args:
            for key in self.Group_Search_By_Name(arg):
                if self.groups[key]["state"]["any_on"]:
                    self.LightsOff(arg)
                else:
                    self.LightsOn(arg)


if __name__ == "__main__":
    pass

