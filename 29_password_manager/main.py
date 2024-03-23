from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# website_label.config(padx=2, pady=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
# email_label.config(padx=2, pady=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# password_label.config(padx=2, pady=2)

# Entries
website_entry = Entry(width=35)
website_entry.insert(END, string="0")
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(END, string="0")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=18)
password_entry.insert(END, string="0")
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", width=18, command=generate_password)
generate_button.grid(column=2, row=3)

generate_button = Button(text="Add", width=36, command=save_password)
generate_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
