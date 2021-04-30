import tkinter as tk
import pandas as pd
import random
import time
import os

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError as error_message:
    df = pd.read_csv("data/translations.csv")

words_to_learn = df.to_dict(orient='records')
current_card = {}

flip_timer = None

def next_pressed():
    global flip_timer, current_card

    window.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image=front_image)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(word_text, text=current_card['nl'], fill="black")
    canvas.itemconfig(language_text, text="Nederlands", fill="black")
    flip_timer = window.after(3000, flip_card)

def known_pressed():
    global flip_timer
    global current_card

    words_to_learn.remove(current_card)

    data = pd.DataFrame(words_to_learn)

    data.to_csv("data/words_to_learn.csv", index=False)

    next_pressed()


def flip_card():
    global current_card

    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(word_text, text=current_card['en'], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")
    window.after_cancel(flip_timer)




# for elem in df['nl']:
#     print(elem)

window = tk.Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# flip_timer = window.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = tk.PhotoImage(file="images/card_front.png")
back_image = tk.PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_pressed)
right_button.grid(row=1, column=1)

wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_pressed)
wrong_button.grid(row=1, column=0)

flip_timer = window.after(3000, next_pressed)

window.mainloop()

