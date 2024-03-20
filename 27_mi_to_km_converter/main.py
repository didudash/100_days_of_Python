from tkinter import *

MILES_TO_KM_CONV_FACTOR = 1.60934


def miles_to_km(miles_value: str) -> str:
    return str(round(float(miles_value) * MILES_TO_KM_CONV_FACTOR, 1))


def button_clicked() -> None:
    miles_value = entry.get()
    km_value = miles_to_km(miles_value)
    result_label.config(text=km_value)


# Window
window = Tk()
window.title("Mi to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)


# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=2, pady=2)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=2, pady=2)

# result has to change according to the calculation
result_label = Label(text="0")
result_label.grid(column=1, row=1)
equal_label.config(padx=2, pady=2)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=2, pady=2)

# Buttons
calc_buttom = Button(text="Calculate", command=button_clicked)
calc_buttom.grid(column=1, row=2)
calc_buttom.config(padx=2, pady=2)


window.mainloop()
