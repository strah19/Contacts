import tkinter as tk
from contact import Contact
import login 
import account
import account_ui
import contact_ui

class Application(tk.Frame):
    def __init__(self):     
        self.ui = tk.Tk(className=' Contacts')
        self.ui.geometry("720x480")
        photo = tk.PhotoImage(file = "icon.png")
        self.ui.iconphoto(False, photo)
        self.ui.resizable(False, False)
        self.acc = account.Account()

        self.login_ui = login.Login(self.ui)
        self.account_ui = account_ui.AccountUI()
        self.selected_contact = Contact()
        self.contact_ui = contact_ui.ContactUI()
        self.logged_in = False

    def __del__(self):
        if self.logged_in:
            self.acc.save_contacts()
        
    def update(self):
        self.ui.after(200, self.contact_task)
        self.ui.mainloop() 

    def contact_task(self):
        if self.logged_in == False:
            self.login()
        else:
            if self.account_ui.logged_out:
                self.account_ui.hide()
                self.login_ui = login.Login(self.ui)
                self.acc.save_contacts()
                self.contact_ui.hide_contact()
                self.acc.log_out()
                self.contact_ui = contact_ui.ContactUI()
                self.logged_in = False
            elif self.account_ui.contacts_list.curselection() and self.selected_contact != self.acc.contacts[self.account_ui.contacts_list.curselection()[0]]:
                self.selected_contact = self.acc.contacts[self.account_ui.contacts_list.curselection()[0]]
                self.contact_ui.hide_contact()
                self.contact_ui.show_contact(self.selected_contact)
            if self.contact_ui.closed:
                self.contact_ui.closed = False
                self.contact_ui.hide_contact()
                self.account_ui.contacts_list.selection_clear(first=0, last=len(self.acc.contacts) - 1)
                self.selected_contact = Contact()
            if self.contact_ui.saving:
                self.contact_ui.saving = False
                self.selected_contact.name = self.contact_ui.get_element("Name").input.get()
                self.selected_contact.address = self.contact_ui.get_element("Address").input.get()
                self.selected_contact.email = self.contact_ui.get_element("Email").input.get()

                index = 0
                for phone in self.contact_ui.elements:
                    if isinstance(phone, contact_ui.ContactUIElementInputToInput):
                        self.selected_contact.phone_numbers[index] = phone.input.get()
                        self.selected_contact.phone_number_names[index] = phone.edit_label.get()
                        index = index + 1

                self.account_ui.update(self.acc)

                for phone_type, p_num in zip(self.selected_contact.phone_number_names, self.selected_contact.phone_numbers):
                    if phone_type == "" and p_num == "":
                        self.selected_contact.phone_number_names.remove(phone_type)
                        self.selected_contact.phone_numbers.remove(p_num)

                        self.contact_ui.hide_contact()
                        self.contact_ui.show_contact(self.selected_contact)
            if self.account_ui.create:
                self.acc.add_contact(Contact("New Contact"))
                self.account_ui.update(self.acc)
                self.account_ui.create = False
            if self.account_ui.removing and self.account_ui.contacts_list.curselection():
                self.account_ui.removing = False
                self.acc.delete_contact(self.selected_contact)
                self.account_ui.update(self.acc)
                self.contact_ui.hide_contact()
            if self.contact_ui.add_phone:
                self.contact_ui.add_phone = False

                self.selected_contact.name = self.contact_ui.get_element("Name").input.get()
                self.selected_contact.address = self.contact_ui.get_element("Address").input.get()
                self.selected_contact.email = self.contact_ui.get_element("Email").input.get()

                self.selected_contact.phone_number_names.append("Phone Number Name")
                self.selected_contact.phone_numbers.append("Number")

                self.contact_ui.hide_contact()
                self.contact_ui.show_contact(self.selected_contact)

        self.ui.after(200, self.contact_task)

    def login(self):
        if self.login_ui.login_status == "Login":
            self.acc.account_security.enter_username(self.login_ui.get_username_input())
            if self.acc.log_in(self.login_ui.get_username_input(), self.login_ui.get_password_input()) == True:
                self.login_ui.clear_frame()
                self.acc.read_in_contacts()
                self.account_ui.show(self.acc)
                self.logged_in = True
            else:
                self.login_ui.change_error_message("**Username or password is incorrect.**")
        elif self.login_ui.login_status == "Create":
            if self.acc.account_security.check_password_strength(self.login_ui.get_password_input()) == "Strong":
                if self.acc.account_security.create_new_account(self.login_ui.get_username_input(), self.login_ui.get_password_input()) == True:
                    self.login_ui.clear_frame()
                    self.acc.logged_in = True
                    self.acc.username = self.acc.account_security.get_username()
                    self.account_ui.show(self.acc)
                    self.logged_in = True
                else:
                    self.login_ui.change_error_message("**Account of this username already exists!**", color="red")
            else:
                self.login_ui.change_error_message("Password for new account is not Strong. Please pick a better password", color="red")

        self.login_ui.login_status = ""
