#!/usr/bin/env python
import argparse

__all__ = ["Arguments"]


class Arguments:
    def __init__(self, *args, **kwargs):

        # Parser
        self.parser = argparse.ArgumentParser(
                description="""This program uses Philips Hue API to change settings on your lights.""")

        # Lights
        self.parser.add_argument(
                "-l", "--lights", nargs="*", help="Turns off specified lights.")

        # Indicates all lights.
        self.parser.add_argument(
                "-a", "--all", action="store_true", help="Indicates changes will be made to all lights. Currently not working.")

        # Turn lights on
        self.parser.add_argument(
                "-on", "--on", action="store_true", help="Turns on specified lights.")

        # Turn lights off
        self.parser.add_argument(
                "-off", "--off", action="store_true", help="Turns off specified lights.")
        
        # Switch on/off lights
        self.parser.add_argument(
                "-s", "--switch", action="store_true", help="Switches on/off given light. Nice for macros/keybinds.")
        
        # Dim lights
        self.parser.add_argument(
                "-d", "--dim", type=int, help="""
        Dim specified lights. 
        Requires an integer indicating how much the light should be dimmed.""")
        
        # Increase brightness.
        self.parser.add_argument(
                "-i", "--increase", type=int, help="""
        Increase brightness of specified lights. 
        Requires an integer indicating how much the light should be increased.""")
        
        # Set color temperature of lights.
        self.parser.add_argument(
                "-c", "--color", help="""
        Color temperature between 153 and 454 for white lights. 
        Also accepts configured colors by names in settings.json.""")
        
        # Returns listed lights and their group.
        self.parser.add_argument(
                "-L", "--list", action="store_true", help="""
        Lists the groups your lights belongs in. 
        These can be changed in settings.json""")
        
        self.args = self.parser.parse_args()

        self.data = dict(
            lights = self.args.lights,
            on = self.args.on,
            off = self.args.off,
            switch = self.args.switch,
            dim = self.args.dim,
            increase = self.args.increase,
            color = self.args.color,
            list = self.args.list,
            all = self.args.all
        )
