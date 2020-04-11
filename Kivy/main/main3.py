# creating buttons and triggering events

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):  #initialize with self and infinite keywords
        super(MyGrid, self).__init__(**kwargs)  #call GridLayout constructor to setup
        self.cols = 2
        self.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False, halign="center")  #only want one line
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False, halign="center")  # only want one line
        self.add_widget(self.lastname)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False, halign="center")  # only want one line
        self.add_widget(self.email)

        self.submit = Button(text="Submit", font_size=40)
        self.add_widget(self.submit)

class MyApp(App):
    def build(self):
        return MyGrid()  #draw widgets/etc rfrom MyGrid

if __name__ == "__main__":
    MyApp().run()