import tkinter as tk
from tkinter.font import Font
from tkinter import Frame

class Login:
    def __init__(self, ui):
        self.frame = Frame(ui)
        self.frame.pack()

        font_style = Font(family="Helvetica", size=24)
        label = tk.Label(self.frame, text="Contacts Login", font = font_style)
        label.pack()

        username_label = tk.Label(self.frame, text="Username")
        self.username_input = tk.Entry(self.frame)

        username_label.pack()
        self.username_input.pack()

        password_label = tk.Label(self.frame, text="Password")
        self.password_input = tk.Entry(self.frame, show="*")

        password_label.pack()
        self.password_input.pack()

        self.login = tk.Button(self.frame, text="Login", command=self.on_login)
        self.login.pack()
        self.login_status = ""

        self.create_account = tk.Button(self.frame, text="Create Account?", command=self.on_create_account)
        self.create_account.pack()
        self.creating_new_account = False

        self.error_label = tk.Label(self.frame, text="**Error during login.**", fg="red")

    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        self.frame.pack_forget()
        self.frame.destroy()

    def get_username_input(self):
        return self.username_input.get()

    def get_password_input(self):
        return self.password_input.get()

    def on_login(self):
        if self.creating_new_account:
            self.login_status = "Create"
        else:
            self.login_status = "Login"

    def on_create_account(self):
        if self.create_account["text"] == "Cancel":
            self.change_error_message("")
            self.login["text"] = "Login"
            self.create_account["text"] = "Create Account?"
            self.creating_new_account = False
        else:
            self.change_error_message("Fill in username and password for new account!", "black")
            self.login["text"] = "Create"
            self.create_account["text"] = "Cancel"
            self.creating_new_account = True

    def get_login_frame(self):
        return self.frame

    def change_error_message(self, msg, color="red"):
        self.error_label.pack()
        self.error_label["text"] = msg
        self.error_label["fg"] = color