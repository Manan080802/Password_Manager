from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)
###########################################
label1 = Label(text="Website:")
label1.grid(row=1,column=0)
edit1 = Entry(width=36)
edit1.focus()
edit1.grid(row=1,column=1,columnspan=2)

##########################################
label2 = Label(text="Email/Username:")
label2.grid(row=2,column=0)
edit2 = Entry(width=36)
edit2.insert(0,"man@gmail.com")
edit2.grid(row=2,column=1,columnspan=2)

##########################################
label3 = Label(text="Password")
label3.grid(row=3,column=0)
edit3 = Entry(width=18)
edit3.grid(row=3,column=1)
def genrate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    edit3.insert(0, password)
    pyperclip.copy(password)


btn = Button(text="Generate Password",command=genrate_password)
btn.grid(row=3,column=2)

################################### #######

def save_data():
    website_name = edit1.get()
    email = edit2.get()
    password = edit3.get()
    print(len(website_name))
    if len(website_name)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Error Message", message="Please enter the all data")


    else:
        ans = messagebox.askokcancel(title=website_name,
                                     message=f"These are the details entered:\n Email: {email} \n Password: {password}")
        if ans:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_name} | {email} | {password} \n")
                data_file.close()
                edit1.delete(0, END)
                edit2.delete(0, END)
                edit2.insert(0, "man@gmail.com")
                edit3.delete(0, END)



btn1 = Button(text="Add",width=30,command=save_data)
btn1.grid(row=4,column=1,columnspan=2)

window.mainloop()