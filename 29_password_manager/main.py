from tkinter import *

# This one is a module
from tkinter import messagebox
import random
import string
import pyperclip

# Layout alingment can be improved and it is optimized for Ubuntu

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Includes both lowercase and uppercase letters
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    # Ensure at least one uppercase letter and mix of other characters
    password_list = [random.choice(string.ascii_uppercase)]
    password_list += [random.choice(letters + digits + symbols) for _ in range(10)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    # to have password already on the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


# save on data.txt
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0:
        messagebox.showinfo(
            title="Oops!", message="Please make sure you don't leave any fields empthy"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the deatils entered: \nEmail: {email} "
            f"\nPassword: {password} \nIs it ok to save?",
        )

        if is_ok:

            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            # Clear the entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.config(padx=10, pady=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_label.config(padx=10, pady=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(padx=10, pady=2)

# Entries
website_entry = Entry(width=42)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=42)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "my_email@gmail.com")

password_entry = Entry(width=20)
# Adjusted for expansion and alignment
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
generate_button = Button(text="Generate Password", width=14, command=generate_password)
# Adjust to ensure alignment without extra padding
generate_button.grid(column=2, row=3, sticky="w")

generate_button = Button(text="Add", width=39, command=save_password)
generate_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
