from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle 
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters =[choice(letters) for n in range(randint(8, 10))]
    password_symbols =[choice(symbols) for n in range(randint(2, 4))]
    password_numbers =[choice(numbers) for n in range(randint(2, 4))]

    password_list=password_symbols + password_letters + password_numbers
    shuffle(password_list)

    password="".join(password_list)
    pass_input.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
 
    website = web_input.get()
    email = email_input.get()
    pasword = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": pasword,
        }
    }

    try:
        with open("data.json", "r") as data_file:
            #Reading old data
            data = json.load(data_file)
            
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)

    else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
    finally:
        web_input.delete(0, END)
        pass_input.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_input.get()
    try:
        with open("data.json",) as data_file:
            data= json.load(data_file)
            
    except FileNotFoundError:
        messagebox.showinfo(title="Eror", message="No Data File Found")
    else:
        if website in data:
            email= data[website]["email"]
            password= data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}.")
        else:
            messagebox.showinfo(title="Eror", message=f"No Details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#Labels

website_label=Label(text="Website :", font=("Ariel",10))
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username :", font=("Ariel",10))
email_label.grid(column=0,row=2)

password_label=Label(text="Password:", font=("Ariel",10))
password_label.grid(column=0,row=3)

#Entries

web_input=Entry(width=21)
web_input.grid(column=1,row=1)
web_input.focus()


email_input=Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2)
# 0 indexdir,  0. indexi alır.
email_input.insert(0,"babyoda@gmail.com")

pass_input=Entry(width=21)
pass_input.grid(column=1,row=3)



#Buttons

generate_button=Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3)

add_button=Button(text="Add", width=36, command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text="Search", width=13,command=find_password)
search_button.grid(column=2,row=1)


window.mainloop()