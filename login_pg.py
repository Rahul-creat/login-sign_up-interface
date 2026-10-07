from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import signup_pg as sp
import forget_pass as fp


user_details = []


def load_credentials():

    global user_details

    try:
        file = open("user_details.txt", "r")
        data = file.read().strip()
        file.close()

        if data != "":
            user_details = eval(data)
        else:
            user_details = []

    except FileNotFoundError:

        messagebox.showerror(
            "New User",
            "Kindly register first"
        )

        user_details = []


def login_click(username, password):

    global user_details

    if username == "" or password == "":
        messagebox.showwarning(
            "Blank Detected!!!",
            "Kindly Fill All Details"
        )
        return
    load_credentials()

    if user_details == []:
        return

    for user in user_details:

        if (
            user["username"] == username and user["password"] == password):
            messagebox.showinfo(
                "Login Successful",
                "Welcome to Project"
            )

            return

    messagebox.showwarning(
        "Login Failed",
        "Check your username and password"
    )


def show_hide_password():

    if pass_entry.cget("show") == "*":

        pass_entry.config(show="")
        show_pass_btn.config(text="Hide")

    else:

        pass_entry.config(show="*")
        show_pass_btn.config(text="Show")



def signup_click():

    root.destroy()

    sp.signup_page()



def forget_password_click():

    root.destroy()

    fp.forget()



def login_page():

    global root
    global user_entry
    global pass_entry
    global show_pass_btn

    root = Tk()

    root.geometry("1920x1080")
    root.config(bg="#1D7EDF")
    root.title("Login Page")


    img = Image.open(
        "C:/Users/panka/OneDrive/Desktop/code/LOGIN_SCREEN/LOGIN_SCREEN/login_logo.jpg"
    )

    img = img.resize((200, 200))

    final_img = ImageTk.PhotoImage(image=img)

    logo_label = Label(
        root,
        compound=TOP,
        image=final_img,
        text="Login Here",
        bg="#0ebb1c",
        fg="white",
        font=("Arial", 30, "bold")
    )

    logo_label.pack()

    user_frame = Frame(
        root,
        bg="black"
    )

    user_frame.pack(pady=20)

    user_label = Label(
        user_frame,
        text="Username",
        bg="cyan",
        fg="red",
        font=("Arial", 20, "bold"),
        width=10
    )

    user_label.pack(side=LEFT)

    user_entry = Entry(
        user_frame,
        bg="black",
        fg="white",
        width=20,
        font=("Arial", 20, "bold")
    )

    user_entry.pack(side=LEFT)


    pass_frame = Frame(
        root,
        bg="black"
    )

    pass_frame.pack(pady=20)

    pass_label = Label(
        pass_frame,
        text="Password",
        bg="cyan",
        fg="red",
        width=10,
        font=("Arial", 20, "bold")
    )

    pass_label.pack(side=LEFT)

    pass_entry = Entry(
        pass_frame,
        bg="black",
        fg="white",
        width=20,
        font=("Arial", 20, "bold"),
        show="*"
    )

    pass_entry.pack(side=LEFT)


    show_pass_btn = Button(
        pass_frame,
        text="Show",
        command=show_hide_password,
        bg="black",
        fg="cyan",
        font=("Arial", 12, "bold"),
        bd=0
    )

    show_pass_btn.pack(side=LEFT, padx=5)


    btn_frame = Frame(
        root,
        bg="black"
    )

    btn_frame.pack(pady=20)

    login_btn = Button(
        btn_frame,
        command=lambda: login_click(
            user_entry.get(),
            pass_entry.get()
        ),
        bg="green",
        fg="white",
        text="Login",
        font=("Arial", 20, "bold"),
        width=10,
        bd=5,
        relief="raised"
    )

    login_btn.pack(side=LEFT)

    signup_btn = Button(
        btn_frame,
        command=signup_click,
        bg="red",
        fg="white",
        text="Sign Up",
        font=("Arial", 20, "bold"),
        width=10,
        bd=5,
        relief="raised"
    )

    signup_btn.pack(side=LEFT, padx=10)

  

    forget_frame = Frame(
        root,
        bg="black"
    )

    forget_frame.pack(pady=5)

    forget_btn = Button(
        forget_frame,
        text="Forgot Password?",
        command=forget_password_click,
        fg="cyan",
        bg = "skyblue",
        font=("Arial", 15, "bold"),
        bd=1,
        width=20,
        relief="ridge"
    )

    forget_btn.pack()

    root.mainloop()



if __name__ == "__main__":

    login_page()