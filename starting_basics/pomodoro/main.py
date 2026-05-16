import tkinter as tk
from tkinter import PhotoImage
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Break",bg=YELLOW,fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break",bg=YELLOW,fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work",bg=YELLOW,fg=GREEN)
        count_down(work_sec)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",bg=YELLOW,fg=GREEN)
    check_marks.config(text="")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✅"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)
canvas = tk.Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img,)
timer_text = canvas.create_text(103, 130,text= "00:00",fill="white",font= (FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1,padx=10,pady=10)
timer_label = tk.Label(text="Timer",bg=YELLOW,fg=GREEN,font= (FONT_NAME,50,"bold"))
timer_label.grid(row=0,column=1,padx=10,pady=10)



button_start = tk.Button(text="Start",bg="white",fg="black",font=(FONT_NAME,12,"bold"),command=start_timer)
button_reset = tk.Button(text="reset",bg="white",fg="black",font=(FONT_NAME,12,"bold"),command=reset_timer)
button_start.grid(row=2,column=0,)
button_reset.grid(row=2,column=2,)

check_marks = tk.Label(text="", bg=YELLOW, fg=GREEN)
check_marks.grid(row=3,column=1,)











window.mainloop()
