
import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text='French',fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(lang_text, text='English',fill='white')
    canvas.itemconfig(word_text, text=current_card['English'],fill='white')
    canvas.itemconfig(card_background, image=card_image_back)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

window = tk.Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR,width=800,height=600,padx=50,pady=50 )


flip_timer = window.after(3000,flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = tk.PhotoImage(file="images/card_front.png")
card_image_back = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_image)
canvas.grid(row=0,column=0,columnspan=2)

correct_image = tk.PhotoImage(file="images/right.png")
wrong_image = tk.PhotoImage(file="images/wrong.png")

correct_button = tk.Button(window,image=correct_image,highlightthickness=0,command=next_card)
correct_button.grid(row=1,column=0)
wrong_button = tk.Button(window,image=wrong_image,highlightthickness=0,command=is_known)
wrong_button.grid(row=1,column=1)

lang_text = canvas.create_text(400,150,text="",font="Ariel 40 italic")
word_text = canvas.create_text(400,263,text="",font="Ariel 60 bold")

next_card()


















window.mainloop()