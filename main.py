from tkinter import *
from tkinter import messagebox
from random import shuffle, randint
from secrets import choice
import json

FONT_NAME = "Verdana"
FONT_SIZE = 10


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


def save():
    site_name = site_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()

    new_data = {
        site_name: {
            "email": email,
            "password": password
        }
    }

    if len(site_name) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Whoa!", message="Do not leave any fields empty."
        )

    else:
        is_ok = messagebox.askokcancel(
            title=site_name, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")

        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=2)

            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=2)

            finally:
                site_entry.delete(0, END)
                password_entry.delete(0, END)
                site_entry.focus()


def search():
    user_input = site_entry.get().title()

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="No Data file found.")

    else:
        if user_input in data:
            email = data[user_input]["email"]
            password = data[user_input]["password"]
            messagebox.showinfo(
                title=user_input,
                message=f"Email: {email}\nPassword: {password}"
            )
            window.clipboard_clear()
            window.clipboard_append(password)

        else:
            messagebox.showerror(
                title="No matches", message=f"There were no matches to the entry: '{user_input}'")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(
    width=200,
    height=200,
    highlightthickness=0
)

my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

gen_password_button = Button(
    text="Generate Password",
    justify="left",
    font=(FONT_NAME, FONT_SIZE),
    command=generate_password
)
gen_password_button.grid(
    column=2,
    row=3,
    padx=5,
    sticky="EW"
)

add_button = Button(
    text="Add",
    width=36,
    justify="left",
    font=(FONT_NAME, FONT_SIZE),
    command=save
)
add_button.grid(
    column=1,
    row=4,
    columnspan=2,
    sticky="EW"
)

search_button = Button(
    text="Search",
    justify="left",
    font=(FONT_NAME, FONT_SIZE),
    command=search
)
search_button.grid(
    column=2,
    row=1,
    padx=5,
    sticky="EW"
)

site_entry = Entry(width=21, justify="left")
site_entry.grid(
    column=1,
    row=1,
    sticky="EW"
)
site_entry.focus()

username_entry = Entry(width=35, justify="left")
username_entry.insert(END, string="dummyemail@email.com")
username_entry.grid(
    column=1,
    row=2,
    columnspan=2,
    sticky="EW"
)

password_entry = Entry(width=21, justify="left")
password_entry.grid(
    column=1,
    row=3,
    sticky="EW"
)

website_label = Label(
    text="Website:",
    justify="right",
    font=(FONT_NAME, FONT_SIZE)
)
website_label.grid(column=0, row=1)

username_label = Label(
    text="Email/Username:",
    justify="right",
    font=(FONT_NAME, FONT_SIZE)
)
username_label.grid(column=0, row=2)

password_label = Label(
    text="Password:",
    justify="right",
    font=(FONT_NAME, FONT_SIZE)
)
password_label.grid(column=0, row=3)


window.mainloop()
