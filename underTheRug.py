#!/usr/bin/python3

import rumps
import subprocess


class UnderTheRug(rumps.App):

    def __init__(self):
        super(UnderTheRug, self).__init__(name="Under the Rug")
        self.template = True
        self.icon = "rug.png"

    @rumps.clicked("Hide Desktop")
    def onoff(self, sender):
        if sender.state:
            subprocess.call(['sh', './Hide.sh'])
            sender.title = "Hide Desktop"
        elif not sender.state:
            subprocess.call(['sh', './Show.sh'])
            sender.title = "Hidden"

        sender.state = not sender.state


if __name__ == "__main__":
    UnderTheRug().run()
