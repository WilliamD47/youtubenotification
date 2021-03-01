## Welcome to my Showcase!

By using YouTubeNotification, you can get a notification whenever a specified channel of your choice uploads! No need to keep checking sub counts.

## How does it work?
Every 10 seconds, the Python script sends a request to Google's YouTube API. It searches for the specified channel. You will need an API key for this however so go get one [here](https://developers.google.com/maps/documentation/embed/get-api-key) to use this. The notification system is a bit more complicated as every operating system seems to need to use a different libary! Here is a snipped of the code below (darwin means macOS. I don't know why either).


```py
def notify(title, message):
    if platform == "darwin":
        t = '-title {!r}'.format(title)
        m = '-message {!r}'.format(message)
        os.system('terminal-notifier {}'.format(' '.join([m, t])))
    elif platform == "win32":
        notification.notify(title, message)
    elif platform == "linux" or platform == "linux2":
        subprocess.Popen(['notify-send', message])
```

For more details see the Git Repo.
