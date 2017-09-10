from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.logger import Logger

class RegattaScreenManager(ScreenManager):
    pass

class TimeRecordScreen(Screen):
    label_text = StringProperty( "Text to change" )

    def buttonCallback(self):
        self.label_text = str( "Text changed" )
        Logger.info("HomeScreen buttonCallback")

class RegattaApp(App):
    def build(self):
        return TimeRecordScreen()

def main():
    app = RegattaApp()
    app.run()

if __name__ == '__main__':
    main()
