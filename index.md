## Welcome to my Showcase!

By using YouTubeNotification, you can get a notification whenever a specified channel of your choice uploads! No need to keep checking sub counts.

## How does it work?
Every 10 seconds, the Python script sends a request to Google's YouTube API. It searches for the specified channel. You will need an API key for this however so go get one [here](https://developers.google.com/maps/documentation/embed/get-api-key)


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

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/WilliamD47/youtubenotification/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
