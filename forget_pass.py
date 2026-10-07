from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def show_hide_password():

    if change_entry.cget("show") == "*":
        change_entry.config(show="")
        show_btn.config(text="Hide")

    else:
        change_entry.config(show="*")
        show_btn.config(text="Show")


def reset_password(contact, new_password):

    if contact == "" or new_password == "":
        messagebox.showwarning(
            "Blank Detected",
            "Kindly fill all details"
        )
        return

    try:
        file = open("user_details.txt", "r")
        data = file.read().strip()
        file.close()

        if data == "":
            messagebox.showerror(
                "Error",
                "No user registered"
            )
            return

        users = eval(data)

    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "No user registered"
        )
        return

    except Exception:
        messagebox.showerror(
            "Error",
            "Unable to read user details"
        )
        return

    for user in users:

        if user["mobile"] == contact:

            user["password"] = new_password

            file = open("user_details.txt", "w")
            file.write(str(users))
            file.close()

            messagebox.showinfo(
                "Success",
                "Password changed successfully"
            )

            forget_root.destroy()

            import login_pg
            login_pg.login_page()

            return

    messagebox.showwarning(
        "Not Found",
        "Contact number is not registered"
    )


def forget():

    global forget_root
    global change_entry
    global show_btn

    forget_root = Tk()
    forget_root.title("Forget Password")
    forget_root.geometry("1920x1080")
    forget_root.config(bg="#071A3D")

    img = Image.open(
        "C:/Users/panka/OneDrive/Desktop/code/LOGIN_SCREEN/LOGIN_SCREEN/forget_pass.jpg"
    )

    img = img.resize((250, 200))
    final_img = ImageTk.PhotoImage(img)

    logo_label = Label(
        forget_root,
        compound=TOP,
        image=final_img,
        text="Forget Password",
        fg="#FCFDFD",
        bg="#071A3D",
        font=("Elephant", 20, "bold")
    )

    logo_label.pack(ipady=30)

    contact_frame = Frame(
        forget_root,
        bg="#071A3D"
    )

    contact_frame.pack(pady=20)

    contact_label = Label(
        contact_frame,
        text="Contact No.",
        fg="white",
        bg="#071A3D",
        font=("Arial", 15, "bold")
    )

    contact_label.pack(side=LEFT, padx=10)

    contact_entry = Entry(
        contact_frame,
        width=20,
        font=("Arial", 15)
    )

    contact_entry.pack(side=LEFT)

    change_frame = Frame(
        forget_root,
        bg="#071A3D"
    )

    change_frame.pack(pady=20)

    change_label = Label(
        change_frame,
        text="New Password",
        fg="white",
        bg="#071A3D",
        font=("Arial", 15, "bold")
    )

    change_label.pack(side=LEFT, padx=10)

    change_entry = Entry(
        change_frame,
        width=20,
        font=("Arial", 15),
        show="*"
    )

    change_entry.pack(side=LEFT)

    show_btn = Button(
        change_frame,
        text="Show",
        command=show_hide_password,
        bg="#071A3D",
        fg="cyan",
        font=("Arial", 12, "bold"),
        bd=0
    )

    show_btn.pack(side=LEFT, padx=5)

    submit_btn = Button(
        forget_root,
        text="Submit",
        bg="#0233ba",
        fg="white",
        width=20,
        height=3,
        font=("Arial", 10, "bold"),
        command=lambda: reset_password(
            contact_entry.get(),
            change_entry.get()
        )
    )

    submit_btn.pack(pady=20)

    forget_root.mainloop()