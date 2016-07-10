from kivy.app import App
from kivy.uix.widget import Widget

class RegattaTimeTable(Widget):
    pass

class RegattaApp(App):
    def build(self):
        return RegattaTimeTable();

if __name__ == '__main__':
    RegattaApp().run()


