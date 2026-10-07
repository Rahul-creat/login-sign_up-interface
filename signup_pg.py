from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import os

def register_click(username, password, email, mobile):

    if username!="" and password!="" and email!="" and mobile!="":

        print(username, password, email, mobile)
        global users
        users = []

        if os.path.exists('user_details.txt'):
            file = open("user_details.txt", 'r')
            data = file.read().strip()

            if data != "":
                for i in eval(data):
                    users.append(i)

        print(users)

        # duplicate users

        for user in users:
            if user['username']== username:
                messagebox.showwarning("user already exists", "Kindly use different username")

                return

        users.append({'username':username, 
                    'password':password,
                    'email':email,
                    'mobile':mobile})

        


        file = open("user_details.txt", 'w')
        file.write(str(users))
        file.close()
        messagebox.showinfo("User Registered Successfully!!!","All details are saved")

        signup_root.destroy()

        import login_pg
        login_pg.login_page()
    else:
        messagebox.showwarning("Blank Detected!!!", "Kindly Fill All details to register")
         
def signup_page():
    global signup_root
    signup_root = Tk()
    signup_root.geometry("1920x1080")
    signup_root.config(bg='black')
    signup_root.title("SignUp Page")

    img = Image.open("C:/Users/panka/OneDrive/Desktop/code/LOGIN_SCREEN/LOGIN_SCREEN/signup_logo.jpg")
    img=img.resize((200,200))
    final_img = ImageTk.PhotoImage(image=img)

    signup_logo_label= Label(signup_root,
                    compound=TOP,
                    image=final_img,
                    text='SignUp Here',
                    bg='black',
                    fg="white",
                    font=("Arial", 30, "bold")
                    )
    signup_logo_label.pack()

    signup_user_frame = Frame(signup_root,
                    bg='black')
    signup_user_frame.pack(pady=20)
    signup_user_label= Label(signup_user_frame,
                    text='Username',
                    bg='black',
                    width=20,
                    fg="white",
                    font=("Arial", 20, "bold")
                    )
    signup_user_label.pack(side=LEFT)

    signup_user_entry = Entry(signup_user_frame,
                    bg='black',
                    fg="white",
                    width=20,
                    font=("Arial", 20, "bold")                
                    )
    signup_user_entry.pack()

    signup_pass_frame = Frame(signup_root,
                    bg='black')
    signup_pass_frame.pack(pady=20)
    signup_pass_label= Label(signup_pass_frame,
                    text='Password',
                    bg='black',
                    width=20,
                    fg="white",
                    font=("Arial", 20, "bold")
                    )
    signup_pass_label.pack(side=LEFT)

    signup_pass_entry = Entry(signup_pass_frame,
                    bg='black',
                    fg="white",
                    width=20,
                    font=("Arial", 20, "bold")                
                    )
    signup_pass_entry.pack()

    signup_email_frame = Frame(signup_root,
                        bg='black')
    signup_email_frame.pack(pady=20)
    signup_email_label= Label(signup_email_frame,
                    text='Email',
                    bg='black',
                    width=20,
                    fg="white",
                    font=("Arial", 20, "bold")
                    )
    signup_email_label.pack(side=LEFT)

    signup_email_entry = Entry(signup_email_frame,
                    bg='black',
                    fg="white",
                    width=20,
                    font=("Arial", 20, "bold")                
                    )
    signup_email_entry.pack()

    signup_mobile_frame = Frame(signup_root,
                    bg='black')
    signup_mobile_frame.pack(pady=20)
    signup_mobile_label= Label(signup_mobile_frame,
                    text='Mobile',
                    width=20,
                    bg='black',
                    fg="white",
                    font=("Arial", 20, "bold")
                    )
    signup_mobile_label.pack(side=LEFT)

    signup_mobile_entry = Entry(signup_mobile_frame,
                    bg='black',
                    width=20,
                    fg="white",
                    font=("Arial", 20, "bold")                
                    )
    signup_mobile_entry.pack()

    signup_btn_frame = Frame(signup_root,
                    bg='black')
    signup_btn_frame.pack(pady=20)

    
    register_btn = Button(signup_btn_frame,
                    bg='green',
                    fg='white',
                    text='Register',
                    command=lambda:register_click(
                        signup_user_entry.get(),
                        signup_pass_entry.get(),
                        signup_email_entry.get(),
                        signup_mobile_entry.get()
                    ),
                    font=("Arial", 20, "bold"),
                    width=10,
                    bd=5,
                    relief='raised'      
                    )
    register_btn.pack(side=LEFT)

    signup_root.mainloop()
