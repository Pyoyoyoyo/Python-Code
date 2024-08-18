from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24))
# my_label.pack()
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"
my_label.config(text="New Text", pady=50, padx=50)


# New button

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Button

def button_clicked():
    string = input.get()
    my_label.config(text=string)


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()



# import turtle
#
# tim = turtle.Turtle()
# tim.write()
