# creating a popup window

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass

class PopupApp(App):
    def build(self):
        return Widgets()

def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None), size=(400,400))
    # can change position, but default of middle

    popupWindow.open()  #open on top of the window

if __name__ == "__main__":
    PopupApp().run()