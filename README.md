# PhilipsHue
CLI tool for controlling Philips Hue


# Installation

## Prerequisites
The software requires Python3 to be installed (might work on 2.7, but not tested).
It's also recommended to use `pip` to install `phue`, otherwise you can find it here: https://github.com/studioimaginaire/phue

## Recommendations
I've personally saved my files inside `~/.local/bin/` which is part of `$PATH`, allowing `hue` to become an executable command on Mac or Linux.
I will however probably create a proper installation for this later.


# Configuration
Add the IP of your Philips Hue bridge in `settings.json`. It would be recommended to set it up so your bridge has a static IP address.
When you run the program the first time, you will have to associate it with the bridge. You can do this simply by pressing the button on top of the bridge. This only needs to be done once.

In `settings.json` you should insert the ID's giving them the names you want, in the same format as th default one.


# Usage
If moved to `$PATH`, you can simply call commands like `hue --lights kitchen --dim 50`. 
`hue --help` will list all available commands.


# Note
This program is still under development, and any feedback are greatly appreciated!
Once I get more gear myself, I'll start adding more features like different colors, routines, etc.

Thanks for downloading, and thanks for feedback!
