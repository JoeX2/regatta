from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.logger import Logger


class RegattaTimeTable(Widget):
    label_text = StringProperty( "Text to change" )

    def buttonCallback(self):
        self.label_text = str( "Text changed" )
        Logger.info("Hello5")


class RegattaApp(App):
    def build(self):
        r = RegattaTimeTable()
        return r


if __name__ == '__main__':
    RegattaApp().run()
