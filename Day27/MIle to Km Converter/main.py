from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=50)
window.config(padx=20, pady=20)
label_is_equal = Label(text="is equal to")
label_is_equal.grid(column=0, row=1)
input_miles = Entry()
input_miles.config(width=10)
input_miles.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_convert_km = Label()
label_convert_km.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.config(padx=20)
label_km.grid(column=2, row=1)


def calculate_mile_to_km():
    mile = int(input_miles.get())
    km = round(mile * 1.609)
    label_convert_km.config(text=km)


button_calculate = Button(text="Calculate", command=calculate_mile_to_km)
button_calculate.grid(column=1, row=2)

window.mainloop()
