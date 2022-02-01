from ast import Pass
from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def calculate():
    miles = float(miles_entry.get())
    kms = round(miles * 1.609)
    km_label.config(text=f"{kms}")

miles_entry = Entry(width=10)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equals_label = Label(text="is equal to")
equals_label.grid(row=1, column=0)

km_label = Label(text="0")
km_label.grid(row=1, column=1)

kilometers_label = Label(text="Kilometers")
kilometers_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()