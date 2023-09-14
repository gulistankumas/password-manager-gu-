from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle 


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

    if len(website) ==0 or len(pasword) ==0:
        messagebox.showinfo(title="Oops", message= "PLease make sure you dont havent left any fields empty.")
    else:
        is_ok= messagebox.askokcancel(title=website, message=f"these are the details entered : \nEmail: {email}"
                                    f"\n Password: {pasword}\n is it ok to save? ")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {pasword} \n")
                web_input.delete(0,END)
                pass_input.delete(0,END)



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

web_input=Entry(width=35)
web_input.grid(column=1,row=1,columnspan=2)
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


window.mainloop()