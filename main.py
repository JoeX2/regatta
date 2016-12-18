from kivy.app import App
from kivy.uix.widget import Widget
from kivy.logger import Logger


class RegattaTimeTable(Widget):
    def buttonCallback(self):
        Logger.info("Hello5")


class RegattaApp(App):
    def build(self):
        r = RegattaTimeTable()
        return r


if __name__ == '__main__':
    RegattaApp().run()
