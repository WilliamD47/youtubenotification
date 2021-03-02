**YouTube Notification by WilliamD47**

This Python script sends a notification to your macOS, Linux or Windows PC every time an inputted channel gains a subscriber.
I am currently working on making a system where it will save the link you put in on the first time, so you don't have to go to the channel each time.
Here are the libaries I use:

```py
import os
import urllib.request
import json
import time
from sys import platform
from plyer import notification
import subprocess
from mcstatus import MinecraftServer
```

If you have any questions please put them in issues or DM me on Discord WilliamD47#6710.
