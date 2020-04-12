# define a button which, when clicked, calls a function and creates a new label text GUI with Tkinter!.

import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.geometry("400x300") #Width x Height
window.title("GUI")

# creating a function called DataCamp_Tutorial()
def click():
    tkinter.Label(window, text="Thanks for clicking!").pack()

tkinter.Button(window, text="Click Me!", command=click).pack()
window.mainloop()