from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    initial_data = pd.read_csv("data/german_words.csv")
    to_learn = initial_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card() -> None:
    global current_card, change_timer
    window.after_cancel(change_card)
    current_card = random.choice(to_learn)
    # need to check if a Noun has to be capitalized in a future version
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"].capitalize(), fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    change_timer = window.after(2200, func=change_card)


def change_card() -> None:
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known() -> None:
    to_learn.remove(current_card)
    to_learn_df = pd.DataFrame(to_learn)
    to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img, anchor="center")
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(
    image=wrong_img,
    highlightthickness=0,
    command=next_card,
)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_img,
    highlightthickness=0,
    command=is_known,
)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
