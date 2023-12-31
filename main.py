import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark_text = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global check_mark_text
        start_timer()
        if reps % 2 == 0:
            check_mark_text += "✔"
            check_marks_label.config(text=check_mark_text)


def start_timer():
    global reps
    reps += 1
    minute = 60
    work = WORK_MIN * minute
    short_break = SHORT_BREAK_MIN * minute
    long_break = LONG_BREAK_MIN * 60

    # if it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break)
        timer_title_label.config(text="Long Break", fg= RED)

    # If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break)
        timer_title_label.config(text="Break", fg=PINK)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work)
        timer_title_label.config(text="Work", fg=GREEN)

def reset_timer():

    global reps
    global check_mark_text
    reps = 0
    window.after_cancel(timer)
    check_mark_text = ""
    check_marks_label.config(text=check_mark_text)
    timer_title_label.config(text = "Timer")
    canvas.itemconfig(timer_text, text="00:00")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_title_label = Label(text="Timer", font=(FONT_NAME, 54, "bold"), bg=YELLOW, fg=GREEN)
timer_title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks_label = Label(text="", font=(FONT_NAME, 14, "bold"), bg=YELLOW, fg=GREEN)
check_marks_label.grid(row=3, column=1)

window.mainloop()
