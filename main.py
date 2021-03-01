import os

os.system("pip3 install plyer")

import urllib.request
import json
import time
from sys import platform
from plyer import notification
import subprocess





try:
    channelink = input("Please enter your YouTube channel link. Do NOT input a URL like https://www.youtube.com/williamd47 Instead, input the URL you get by going to your profile picture, then 'Your Channel'. \n")
except Exception:
    print("Error. Please re run the program and try again.")
    exit()


try:
    ytId = channelink.rsplit('/',1)[1]
except Exception:
    print("You have inputted an incorrect YouTube ID. Please read the above information to find it.")
    exit()

print(ytId + " is your YouTube ID. Sending a test notification.")
def getSubs(ytId):
    key = ""
    ytId = "UCgx3cwTPCFWEe7GAe_X8-1Q"
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + ytId + "&fields=items/statistics/subscriberCount&key=" + key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    return subs


def notify(title, message):
    if platform == "darwin":
        t = '-title {!r}'.format(title)
        m = '-message {!r}'.format(message)
        os.system('terminal-notifier {}'.format(' '.join([m, t])))
    elif platform == "win32":
        notification.notify(title, message)
    elif platform == "linux" or platform == "linux2":
        subprocess.Popen(['notify-send', message])

notify("test","testnotif")


while True:
    oldsubs = getSubs(ytId)
    time.sleep(10)
    subs = getSubs(ytId)
    print(f"old {oldsubs} new {subs}")
    try:
        if subs > oldsubs:
            notify(title="New Subscriber",message="User, you have a new subscriber! Your subscriber count is now on "+str(subs))
    except Exception as e:
        pass
