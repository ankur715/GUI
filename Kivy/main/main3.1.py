import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):  #initialize with self and infinite keywords
        super(MyGrid, self).__init__(**kwargs)  #call GridLayout constructor to setup
        self.cols = 1  #main widget columns=1

        self.inside = GridLayout()  #add layout inside another layout
        self.inside.cols = 2  #inside widget 2 columns

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False, halign="center")  #only want one line
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False, halign="center")  # only want one line
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False, halign="center")  # only want one line
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)  #pressed function called when pressed
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):  #called when Button pressed
        name = self.name.text
        last = self.lastname.text
        email = self.email.text
        print("Name:", name, "\nLast Name: ", last, "\nEmail: ", email)
        self.name.text = ""
        self.lastname.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()  #draw widgets/etc rfrom MyGrid

if __name__ == "__main__":
    MyApp().run()