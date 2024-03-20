from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#68B984"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
def start_clicked() -> None:
    pass


def reset_clicked() -> None:
    pass


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

checkmark = "✔"

# Canvas
# values from size in pixels of picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# half of the width and half of the height and move x to center
canvas.create_image(100, 112, image=tomato_img)
# move down on y to center on the tomato
canvas.create_text(100, 137, text="00:00", fill="beige", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels
timer_label = Label(
    text="Timer",
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 35, "bold"),
    highlightthickness=0,
)
timer_label.grid(column=1, row=0)
# timer_label.config(padx=2, pady=2)

checkmark_label = Label(
    text="✔",
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 35, "bold"),
    highlightthickness=0,
)
checkmark_label.grid(column=1, row=3)

# buttons
start_button = Button(text="Start", command=start_clicked)
start_button.grid(column=0, row=2)
# start_button.config(padx=2, pady=2)

reset_button = Button(text="Reset", command=reset_clicked)
reset_button.grid(column=2, row=2)
# reset_button.config(padx=2, pady=2)

window.mainloop()
