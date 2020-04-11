# navigation between multiple screens

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


class MainWindow(Screen):  #dictate screens and screen manager  #main window
    pass


class SecondWindow(Screen):  #page we go to next
    pass


class WindowManager(ScreenManager):  #transitions between windows
    pass


kv = Builder.load_file("lang.kv")

class LangApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    LangApp().run()