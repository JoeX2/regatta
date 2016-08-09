from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty

class RegattaTimeTable(Widget):
    pass

class RegattaApp(App):
    def build(self):
        r = RegattaTimeTable()
        
        return r

if __name__ == '__main__':
    RegattaApp().run()


