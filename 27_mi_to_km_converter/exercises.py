from tkinter import *

# TK written in C


def first_gui() -> None:
    window = Tk()
    window.title("My first GUI Program")
    window.minsize(width=500, height=300)

    # Label
    my_label = Label(text="I am a Label", font=("Courier", 20, "italic"))
    # placed and centered
    my_label.pack(expand=True)
    my_label.pack()

    window.mainloop()


def add(*args) -> None:
    # args is a tuple
    print(sum([n for n in args]))


def students_passed(**kwargs):
    # kwargs is a dictionary
    passing_threshold = 60
    passed = {
        student: grade
        for (student, grade) in kwargs.items()
        if grade >= passing_threshold
    }
    print(passed)


class Car:

    def __init__(self, **kw) -> None:
        self.make = kw["make"]
        # if the key doesn't exist get outputs None
        # instead of KeyError with the other method
        self.model = kw.get("model")


def widget_examples() -> None:
    """Examples provided by the course"""
    # Creating a new window and configurations
    window = Tk()
    window.title("Widget Examples")
    window.minsize(width=500, height=500)

    # Labels
    label = Label(text="This is old text")
    label.config(text="This is new text")
    label.pack()

    # Buttons
    def action() -> None:
        print("Do something")

    # calls action() when pressed
    button = Button(text="Click Me!", command=action)
    button.pack()

    # Entries
    entry = Entry(width=30)
    # Add some text to begin with
    entry.insert(END, string="Some text to begin with.")
    # Gets text in entry
    print(entry.get())
    entry.pack()

    # Text
    text = Text(height=5, width=30)
    # Puts cursor in textbox.
    text.focus()
    # Adds some text to begin with.
    text.insert(END, "Example of multi-line text entry.")
    # Get's current value in textbox at line 1, character 0
    print(text.get("1.0", END))
    text.pack()

    # Spinbox
    def spinbox_used() -> None:
        # gets the current value in spinbox.
        print(spinbox.get())

    spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
    spinbox.pack()

    # Scale
    # Called with current scale value.
    def scale_used(value) -> None:
        print(value)

    scale = Scale(from_=0, to=100, command=scale_used)
    scale.pack()

    # Checkbutton
    def checkbutton_used() -> None:
        # Prints 1 if On button checked, otherwise 0.
        print(checked_state.get())

    # variable to hold on to checked state, 0 is off, 1 is on.
    checked_state = IntVar()
    checkbutton = Checkbutton(
        text="Is On?", variable=checked_state, command=checkbutton_used
    )
    checked_state.get()
    checkbutton.pack()

    # Radiobutton
    def radio_used() -> None:
        print(radio_state.get())

    # Variable to hold on to which radio button value is checked.
    radio_state = IntVar()
    radiobutton1 = Radiobutton(
        text="Option1", value=1, variable=radio_state, command=radio_used
    )
    radiobutton2 = Radiobutton(
        text="Option2", value=2, variable=radio_state, command=radio_used
    )
    radiobutton1.pack()
    radiobutton2.pack()

    # Listbox
    def listbox_used(event) -> None:
        # Gets current selection from listbox
        print(listbox.get(listbox.curselection()))

    listbox = Listbox(height=4)
    fruits = ["Apple", "Pear", "Orange", "Banana"]
    for item in fruits:
        listbox.insert(fruits.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack()
    window.mainloop()


# first_gui()
# add(3, 5, 6)
# students_passed(Diana=70, Olga=80, Ana=50)
# my_car = Car(make="Nissan")
# print(my_car.model)
widget_examples()
