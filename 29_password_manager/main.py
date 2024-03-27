from tkinter import *

# This one is a module
from tkinter import messagebox
import random
import string
import pyperclip
import json

# Layout alingment can be improved and it is optimized for Windows
# Make it closspattform

# ---------------------------- SEARCH  -------------------------------------- #


def find_password() -> None:
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Read
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(
                title="Info :)",
                message=f"Email: {data[website]['email']} "
                f"\nPassword:  {data[website]['password']}",
            )
        else:
            messagebox.showinfo(
                title="Error!", message="No details for the website exist"
            )


# ---------------------------- GENERATE PASSWORD ---------------------------- #


def generate_password() -> None:
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
    # To have password already on the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


# save on data.txt
def save_password() -> None:
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(email) == 0:
        messagebox.showinfo(
            title="Oops!", message="Please make sure you don't leave any fields empthy"
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read
                data = json.load(data_file)  # Have it as a dict
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Save
                json.dump(data, data_file, indent=4)  # Indent to make it more readable
        finally:
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

# Labels
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
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "my_email@gmail.com")

password_entry = Entry(width=20)
# Adjusted for expansion and alignment
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, sticky="w")

generate_button = Button(text="Generate Password", width=14, command=generate_password)
# Adjust to ensure alignment without extra padding
generate_button.grid(column=2, row=3, sticky="w")

generate_button = Button(text="Add", width=43, command=save_password)
generate_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
