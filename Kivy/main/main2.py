# labels, input, GUI layout

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):  #initialize with self and infinite keywords
        super(MyGrid, self).__init__(**kwargs)  #call GridLayout constructor to setup
        self.cols = 2
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)  #only want one line
        self.add_widget(self.name)



class MyApp(App):
    def build(self):
        return MyGrid()  #draw widgets/etc rfrom MyGrid

if __name__ == "__main__":
    MyApp().run()