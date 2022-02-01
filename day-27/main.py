from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)

# Relative to others
my_label.grid(column=0, row=0)


# Update properties of a component
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=20, pady=20)

# Button
def first_button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")

first_button = Button(text="Click Me", command=first_button_clicked)
first_button.grid(column=1, row=1)

def second_button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)

second_button = Button(text="Change text", command=second_button_clicked)
second_button.grid(column=2, row=0)


# Entry component (input)
user_input = Entry(width=10)
user_input.grid(column=3, row=2)


# Keeps the window on the screen, has to be at the end
window.mainloop()