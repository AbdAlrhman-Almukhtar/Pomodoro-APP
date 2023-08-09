from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
reps = 0
flag = False
timer = None
# TIMER RESET#
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timeText, text="00:00")
    timeLabel.config(text="Timer")
    ticksLabel.config(text="")
    global reps
    reps = 0
    global flag
    flag = False
# TIMER MECHANISM #


def startTimer():
    global reps
    global flag
    if flag==False:
        reps += 1
        if reps % 8 == 0:
            countDown(LONG_BREAK_MIN * 60)
            timeLabel.config(text="Break", fg=GREEN)
        elif reps % 2 == 0:
            countDown(SHORT_BREAK_MIN * 60)
            timeLabel.config(text="Break", fg=GREEN)
        else:
            countDown(WORK_MIN * 60)
            timeLabel.config(text="Work", fg=RED)
        flag = True


# COUNTDOWN  #


def countDown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes == 0:
        minutes = "00"

    if seconds <= 9:
      seconds = f"0{seconds}"

    if minutes <= 9:
        minutes = f"0{minutes}"
    canvas.itemconfig(timeText, text=f"{minutes}:{seconds}")
    if count > 0:
     global timer
     timer = window.after(
            1000,
            countDown,
            count-1
        )
    else:
        startTimer()
        ticks = ""
        for i in range(math.floor(reps/2)):
            ticks += TICK
        ticksLabel.config(text=ticks)
# UI SETUP #


window = Tk()
window.title("Pomodoro")
window.config(
    padx=100,
    pady=50,
    bg=YELLOW
)
canvas = Canvas(
    width=203,
    height=224,
    bg=YELLOW,
    #TO REMOVE THE BORDER#
    highlightthickness=0
)

tomatoPNG = PhotoImage(
    file="tomato.png")
canvas.create_image(
    102,
    112,
    image=tomatoPNG
)
canvas.grid(
    row=1,
    column=1
)
timeText = canvas.create_text(
    104,
    120,
    text="00:00",
    fill="white",
    font=(
        FONT_NAME,
        30,
        "bold"
    )
    )
timeLabel = Label(
    text="Timer",
    font=(FONT_NAME,
          50,
          "bold"
          ),
    highlightthickness=0,
    bg=YELLOW,
    fg=GREEN
)
timeLabel.grid(
    row=0,
    column=1
)

ticksLabel = Label(
    text=TICK,
    font=(FONT_NAME,
          15,
          "bold"
          ),
    highlightthickness=0,
    bg=YELLOW,
    fg=GREEN
)

ticksLabel.grid(
    row=3,
    column=1
)
startbtn = Button(
    text="Start",
    bg=YELLOW,
    highlightthickness=4,
    command=startTimer
)
startbtn.grid(
    row=2,
    column=0
)

resetbtn = Button(
    text="Reset",
    bg=YELLOW,
    highlightthickness=4,
    command=reset

)
resetbtn.grid(
    row=2,
    column=2
)

window.mainloop()
