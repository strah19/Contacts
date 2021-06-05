import tkinter as tk
from tkinter.font import Font
from tkinter import Frame
from tkinter import *
from tkinter import ttk
from account import Account
from account_ui import AccountUI

from contact import Contact

class ContactUIElement:
    def __init__(self, id):
        self.label = tk.Label()
        self.input = tk.Entry()
        self.id = id
        self.data = None

    def show(self, x, y):
        if self.input.cget("text"):
            self.hide()
        self.label = tk.Label(text=self.id + ": ")
        self.input = tk.Entry()
        self.input.insert(0, str(self.data))

        self.label.place(x=x, y=y)
        self.input.place(x=x + 100, y=y)

    def hide(self):
        self.label.place_forget()
        self.input.place_forget()
        self.input.delete(0, END)

class ContactUIElementInputToInput(ContactUIElement):
    def __init__(self, id, label_id):
        ContactUIElement.__init__(self, id)
        self.edit_label = tk.Entry()
        self.data = label_id
    def show(self, x, y):
        if self.input.cget("text"):
            self.hide()
        self.input = tk.Entry()
        self.input.insert(0, str(self.id))

        self.edit_label = tk.Entry()
        self.edit_label.insert(0, self.data)

        self.edit_label.place(x=x, y=y)
        self.input.place(x=x + 130, y=y)

    def hide(self):
        self.input.place_forget()
        self.input.delete(0, END)
        self.edit_label.place_forget()
        self.edit_label.delete(0, END)

class ContactUI:
    def __init__(self):
        self.y = 40
        self.elements = []
        self.save = tk.Button()
        self.close = tk.Button()
        self.add_phone_btn = tk.Button()
        self.closed = False
        self.saving = False
        self.add_phone = False

    def show_contact(self, contact : Contact):
        self.elements = [ContactUIElement("Name"), ContactUIElement("Email"), ContactUIElement("Address")]

        for phone_type, phone in zip(contact.phone_number_names, contact.phone_numbers):
            self.elements.append(ContactUIElementInputToInput(phone, phone_type))      

        self.y = 40
        self.get_element("Name").data = contact.name
        self.get_element("Email").data = contact.email
        self.get_element("Address").data = contact.address
        for element in self.elements: 
            element.show(370, self.y)
            self.y = self.y + 30

        self.save = tk.Button(text="Save Contact", command=self.save_contact)
        self.save.place(x=370, y=self.y)
        self.y = self.y + 30
        self.close = tk.Button(text="Close Contact", command=self.close_contact)
        self.close.place(x = 370, y=self.y)
        self.y = self.y + 30
        self.add_phone_btn = tk.Button(text="Add Phone Number", command=self.fn_add_phone)
        self.add_phone_btn.place(x=370, y=self.y)

    def hide_contact(self):
        for element in self.elements:
            element.hide()
        self.save.place_forget()
        self.close.place_forget()
        self.add_phone_btn.place_forget()

    def get_element(self, id) -> ContactUIElement:
        for element in self.elements:
            if id == element.id:
                return element
        return None

    def close_contact(self):
        self.closed = True

    def save_contact(self):
        self.saving = True

    def fn_add_phone(self):
        self.add_phone = True
