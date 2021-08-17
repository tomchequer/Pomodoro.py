from tkinter import *
#CONSTANTS ------------- #
INDIGO = "#261C2C"
PURPLE = "#3E2C41"
LIGHTERPURPLE = "#5C527F"
ALMOSTGRAY = "#6E85B2"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.minsize(height=400, width=500)
window.config(padx=100, pady=50, bg=ALMOSTGRAY)

canvas = Canvas(width=200, height=220, bg=ALMOSTGRAY, highlightthickness=0)
tomato_image = PhotoImage(file='darktomato.png')
canvas.create_image(100, 108, image=tomato_image)
canvas.create_text(100, 130, text='00:00', fill=INDIGO , font=(FONT_NAME, 36, "bold"))
canvas.grid(row=2, column=2)

timer = Label(text='Timer', fg=INDIGO, bg=ALMOSTGRAY, font=(FONT_NAME, 36, "bold"))
timer.grid(row=1, column=2)

start = Button(text='Start')
reset = Button(text='Reset')

window.mainloop()
