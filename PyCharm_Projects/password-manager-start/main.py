import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
from json.decoder import JSONDecodeError


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    entry_password.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(index=tk.END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_to_file(file_name, data_to_write):
    with open(file_name, "w") as data_file:
        json.dump(data_to_write, data_file, indent=4)

def save_password():
    website_name = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if not len(website_name) or not len(password):
        messagebox.showinfo(title="Missing Info", message="You need to fill in the fields")
    else:
        # is_ok = messagebox.askokcancel(title=website_name, message=f"Details entered:\nEmail: {email}\nPassword: {password}"
        #                                                    "\nIs it ok to save?")

        # if is_ok:
        new_data_dict = {
            website_name: {
                "email": email,
                "password": password}
                         }

        try:
            with open("data.json", "r") as data_file:
                current_data = json.load(data_file)
        except FileNotFoundError as err:
            print("File is empty")
            write_to_file("data.json", new_data_dict)
        else:
            current_data.update(new_data_dict)
            write_to_file("data.json", current_data)

        finally:
            clear_entries()


def clear_entries():
    entry_website.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_website.focus()


def search_website():
    website_name = entry_website.get()

    try:
        with open("data.json", "r") as data_file:
            data_dict = json.load(data_file)
    except FileNotFoundError as error_message:
        messagebox.showinfo(title=f"{website_name}", message="No data file found")
    else:
        if website_name in data_dict:
            website_password = data_dict[website_name]["password"]
            messagebox.showinfo(title=f"{website_name}", message="Password copied to clip board")
            pyperclip.copy(website_password)
        else:
            messagebox.showinfo(title=f"Error", message=f"No website password for {website_name}")




# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200, bg="white")
logo_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

label_website = tk.Label(text="Website:")
label_website.grid(row=1, column=0)

entry_website = tk.Entry(width=21)
entry_website.grid(row=1, column=1, columnspan=1)
entry_website.focus()

button_search = tk.Button(text="Search", command=search_website, width=14)
button_search.grid(row=1, column=2)

label_email = tk.Label(text="Email/Username:")
label_email.grid(row=2, column=0)

entry_email = tk.Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(index=tk.END, string="ondererens@gmail.com")

label_password = tk.Label(text="Password:")
label_password.grid(row=3, column=0)

entry_password = tk.Entry(width=21)
entry_password.grid(row=3, column=1)

button_password = tk.Button(text="Generate Password", command=generate_password)
button_password.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
