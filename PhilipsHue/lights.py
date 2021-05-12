#!/usr/bin/env python

from connect import Connect

__all__ = ["Lights"]

class Lights(Connect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lights = self.api["lights"]
        self.lightid = list(self.lights.keys())

    def UpdateLight(self, ID, **kwargs):
        for key, value in kwargs.items():
            self.conn.set_light(ID, key, value)

    def GetBrightness(self, ID):
        return self.lights[str(ID)]["state"]["bri"]

    def SetBrightness(self, bri, *args):
        for arg in args:
            self.UpdateLight(arg, bri=bri)

    def IncreaseBrightness(self, by, *args):
        for arg in args:
            self.UpdateLight(arg, bri=self.GetBrightness(arg) + by)

    def DimBrightness(self, by, *args):
        for arg in args:
            self.UpdateLight(arg, bri=self.GetBrightness(arg) - by)

    def SetColor(self, ct, *args):
        if isinstance(ct, int):
            for arg in args:
                self.UpdateLight(arg, ct=ct)
            return
        elif ct in colors.keys():
            for arg in args:
                self.UpdateLight(ID, ct=colors[ct])

    def GetLight(self, key):
        return self.lights[str(key)]

    def SwitchLight(self, *args):
        for arg in args:
            if self.lights[str(arg)]["state"]["on"]:
                self.LightsOff(arg)
            else:
                self.LightsOn(arg)

    def LightsOn(self, *args):
        for arg in args:
            self.UpdateLight(arg, on=True)

    def LightsOff(self, *args):
        for arg in args:
            self.UpdateLight(arg, on=False)


if __name__ == "__main__":
    lights = Lights()
