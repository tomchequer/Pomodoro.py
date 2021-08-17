from tkinter import *
import math

#CONSTANTS#

INDIGO = "#261C2C"
PURPLE = "#3E2C41"
LIGHTERPURPLE = "#5C527F"
ALMOSTGRAY = "#6E85B2"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer1 = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer1)
    canvas.itemconfig(timer, text="00:00")
    title.config(text='Timer', fg=INDIGO)
    check_marks.config(text='')
    global reps
    reps = 0
# ------------------- TIMER MECHANISM ------------------------ # 

def start_timer():
    global reps
    reps += 1
    
    work_in_sec = WORK_MIN * 60
    short_in_sec = SHORT_BREAK_MIN * 60
    long_in_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countdown(long_in_sec)
        title.config(text='BREAK', fg=LIGHTERPURPLE)
    elif reps % 2 == 0:
        countdown(short_in_sec)
        title.config(text='BREAK', fg=LIGHTERPURPLE)
    else: 
        countdown(work_in_sec)
        title.config(text='WORK', fg=INDIGO)
        

# ----------------- COUNTDOWN MECHANISM -------------- # 
def countdown(count):
    count_in_min = math.floor(count / 60)
    count_in_seconds = count % 60
    if count_in_seconds < 10:
        count_in_seconds = f"0{count_in_seconds}"
    
    canvas.itemconfig(timer, text=f"{count_in_min}:{count_in_seconds}")
    if count > 0: 
        global timer1
        timer1 = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        for i in range(math.floor(reps/2)):
            marks += '✔'
        check_marks.config(text=marks) 
# ---------------------------- UI SETUP ------------------------------- #
#-- windows --#

window = Tk()
window.title('Pomodoro')
window.minsize(height=400, width=500)
window.config(padx=65, pady=52, bg=ALMOSTGRAY)


#-- canvas --# 
canvas = Canvas(width=200, height=220, bg=ALMOSTGRAY, highlightthickness=0)

darktomato = PhotoImage(file='darktomato.png')

setup = canvas.create_image(100, 108, image=darktomato)
timer = canvas.create_text(100, 130, text='00:00', fill=INDIGO , font=(FONT_NAME, 36, "bold"))
canvas.grid(row=2, column=3)

#-- labels --#
title = Label(text='Timer', fg=INDIGO, bg=ALMOSTGRAY, font=(FONT_NAME, 36, "bold"))
title.grid(row=1, column=3)

#-- buttons --#
start = Button(text='Start', fg=INDIGO, bg=LIGHTERPURPLE, command=start_timer)
start.grid(row=3, column=2)

reset = Button(text='Reset', fg=INDIGO, bg=LIGHTERPURPLE, command=reset_timer)
reset.grid(row=3, column=4)

#-- check marks -- #

check_marks = Label(text='', bg=ALMOSTGRAY, font=(FONT_NAME, 32))
check_marks.grid(column=1, row=5)

window.mainloop()
