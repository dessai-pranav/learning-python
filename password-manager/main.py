import json
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import random
import pyperclip
window = tk.Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20)
canvas = tk.Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image( 100,100,image=photo)
canvas.grid(row=0,column=1)

def generate_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)



def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please enter all fields")
    else:
            try:
              with open("data.json", "r") as file:
                  data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
            messagebox.showinfo("Success", "Password has been saved")


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise TypeError("No Data File Found.")
    else:

            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title= website,message=f"website name is {website} and password is {password}")
            else:
                print("no details for website found")




website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)

email_label = tk.Label(text="Email / Username:")
email_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)


website_entry = tk.Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=10, pady=5)
website_entry.focus()

email_entry = tk.Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=10, pady=5)
email_entry.insert(0,"pranav@gmail.com")

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)



generate_password = tk.Button(text="Generate Password",command=generate_passwords)
generate_password.grid(row=3, column=2, padx=10, pady=5)

add_button = tk.Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

search = tk.Button(text="search",command=find_password,width=10 )
search.grid(row=1,column=2,sticky="w", padx=10, pady=10)




window.mainloop()