# PhilipsHue
CLI tool for controlling Philips Hue


# Installation

## Prerequisites
The software requires Python3 to be installed (might work on 2.7, but not tested).
It's also recommended to use `pip` to install `phue`, otherwise you can find it here: https://github.com/studioimaginaire/phue

## Recommendations
I've personally saved my files inside `~/.local/bin/` which is part of `$PATH`, allowing `hue` to become an executable command on Mac or Linux.
I will however probably create a proper installation for this later.

## Sun cycle simulation
Executing the `hue` file will by default make calculations which linearly increases brightness from the morning with blue light, which will turn more and more orange during the night. 
The settings for when they turn on, and when during the day the peak brightness should be can be configured in `./PhilipsHue/checktime.py` in the `TimeRules` class. 

For systemd users, this can be automated by moving `phue.service` and `phue.timer` to `/etc/systemd/system/`.
You will need to configure `phue.service` first to contain correct username and path to the executable file `hue`.
After this, you can execute `systemctl daemon-reload` and start the service with `systemctl enable --now phue.timer`.
By default, the update interval is set to every 60 seconds, but this can easily be configured differently in `phue.timer`.

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
