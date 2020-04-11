# kv design language
# 4.1 object properties

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name:", self.name.text, "\nEmail:", self.email.text)
        self.name.text = ""
        self.email.text = ""

class MyApp(App):  #save my.kv text file #if class clsApp then cls.kv
    def build(self):
        return MyGrid()  #draw widgets/etc rfrom MyGrid

if __name__ == "__main__":
    MyApp().run()