# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import END
from tkinter import messagebox
import tkinter
import pyperclip
import random


def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v",
               "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    if len(email) < 1 or len(password) < 1 or len(website) < 1:
        messagebox.showwarning(title="Warning", message="Enter Some Data To Proceed")

    else:
        is_ok = messagebox.askokcancel(title="Alert", message=f"These are your credentials :- \n Email :- {email} \n "
                                                              f"Password :- {password} \n Website :- {website}\n"
                                                              f"Do You want to save these data ?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {password} \n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=1)
# Labels
website_label = tkinter.Label(text="Website :")
website_label.grid(column=0, row=2)
email_label = tkinter.Label(text="Email / Username :")
email_label.grid(column=0, row=3)
password_label = tkinter.Label(text="Password :")
password_label.grid(row=4, column=0)
generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=4)
add_button = tkinter.Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=5, columnspan=2)

# Entry
website_entry = tkinter.Entry(width=35)
website_entry.grid(columnspan=2, column=1, row=2)
email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=3, columnspan=2)
password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=4)

window.mainloop()
