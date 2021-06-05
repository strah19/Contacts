import tkinter as tk
from tkinter.font import Font
from tkinter import Frame
from tkinter import *
from tkinter import ttk

from account import Account

class AccountUI:
    def show(self, account : Account):
        self.username_label = tk.Label(text="Username: " + account.username)
        self.username_label.pack(side=LEFT, anchor=NW)

        self.logged_out = False
        self.log_out = tk.Button(text="Log Out", command=self.fn_log_out)
        self.log_out.pack(side=RIGHT, anchor=NE)

        self.top_sep = ttk.Separator(orient='horizontal')
        self.top_sep.place(x=0, y=26, relwidth=1, relheight=1)

        self.x_sep = ttk.Separator(orient='vertical')
        self.x_sep.place(y=27, relx=0.5, relwidth=1, relheight=1)

        self.add_btn = tk.Button(text="Create Contact", command=self.fn_create_contact)
        self.add_btn.place(x=0, y=350)
        self.create = False

        self.contact_label = tk.Label(text="Contacts")
        self.contact_label.place(x=0, y=30)

        self.contacts_list = tk.Listbox()
        self.contacts_list.place(x=0, y=60)

        self.remove_btn = tk.Button(text="Remove Contact", command=self.fn_remove)
        self.removing = False
        self.remove_btn.place(x=0, y=376)

        self.update(account)

    def hide(self):
        self.add_btn.place_forget()
        self.contacts_list.place_forget()
        self.top_sep.place_forget()
        self.x_sep.place_forget()
        self.username_label.pack_forget()
        self.log_out.pack_forget()
        self.contact_label.place_forget()
        self.remove_btn.place_forget()

    def update(self, account : Account):    
        self.contacts_list.delete(0, 'end')
        index = 0
        for contact in account:
            self.contacts_list.insert(index, contact.name)
            index = index + 1

    def fn_log_out(self):
        self.logged_out = True

    def fn_create_contact(self):
        self.create = True

    def fn_remove(self):
        self.removing = True
    

    
        