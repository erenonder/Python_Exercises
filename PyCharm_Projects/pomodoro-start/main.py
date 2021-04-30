import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

work_reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_pressed():
    # global timer
    global work_reps
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    # reset_timer = True
    work_reps = 0
    check_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global work_reps
    global reset_timer

    if work_reps % 2 == 0:
        timer_label.config(text="Work", fg=GREEN)
        timer_seconds = WORK_MIN * 60
    elif work_reps == 7:
        timer_label.config(text="Break", fg=RED)
        timer_seconds = LONG_BREAK_MIN * 60
    else:
        timer_label.config(text="Break", fg=PINK)
        timer_seconds = SHORT_BREAK_MIN * 60

    reset_timer = False
    update_timer(timer_seconds)

    work_reps += 1

    check_mark_count = int(work_reps / 2)
    check_label.config(text="✓"*check_mark_count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def update_timer(count):
    global timer

    minutes = int(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer = window.after(1000, update_timer, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()

window.title("Pomodoro")

window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", height=1, width=4, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", height=1, width=4, command=reset_pressed)
reset_button.grid(row=2, column=2)

check_label = tkinter.Label(text="", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)


window.mainloop()