from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#68B984"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# GUI programs are event driven check window.after and window.after_cancel


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clicked() -> None:
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer() -> None:
    global reps

    if reps % 2 == 0:
        # Work time
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    elif reps == 7:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Work", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Work", fg=PINK)
    reps += 1


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        # In ms the first attr
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # End of a work - rest cycle + 1 because it is 0 indexed
        marks = ""
        work_sessions = int((reps + 1) / 2)
        marks += "✔" * work_sessions
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
# Values from size in pixels of picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# Half of the width and half of the height and move x to center
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 137, text="00:00", fill="beige", font=(FONT_NAME, 35, "bold")
)
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
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 35, "bold"),
    highlightthickness=0,
)
checkmark_label.grid(column=1, row=3)

# Buttons
start_button = Button(
    text="Start",
    bg=YELLOW,
    fg=GREEN,
    font=(FONT_NAME, 17, "bold"),
    highlightthickness=0,
    command=start_timer,
)
start_button.grid(column=0, row=2)

reset_button = Button(
    text="Reset",
    bg=YELLOW,
    fg=RED,
    font=(FONT_NAME, 17, "bold"),
    highlightthickness=0,
    command=reset_clicked,
)
reset_button.grid(column=2, row=2)

window.mainloop()
