from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img, anchor="center")
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)


window.mainloop()
