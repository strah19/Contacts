from contact import Contact
from security import AccountSecurity
import pickle
from pathlib import Path

class Account:
    def __init__(self):
        self.contacts = []
        self.logged_in = False
        self.username = ""
        self.account_security = AccountSecurity()

    def add_contact(self, contact : Contact):
        if self.logged_in:
            self.contacts.append(contact)

    def delete_contact(self, contact : Contact):
        if self.logged_in:
            self.contacts.remove(contact)

    def log_in(self, username, password): 
        if self.logged_in:
            return False
        if self.account_security.check_existing_accounts(username + '\n') == False:
            return False
        
        self.account_security.enter_username(username)
        if self.account_security.enter_password(password) == True:
            self.logged_in = True
            self.username = self.account_security.get_username()
        return self.logged_in

    def log_out(self):
        self.logged_in = False

    def read_in_contacts(self):
        my_file = Path(self.username + ".p")
        if my_file.is_file():
            f = open(self.username + ".p", "rb")
            f.seek(0) 
            first_char = f.read(1) 
            if not first_char:
               pass
            else:
                f.seek(0)
                self.contacts = pickle.load(f)
                for contact in self.contacts:
                    contact = Contact(contact)
        else:
            f = open(self.username + ".p","w+")
            f.close()

    def save_contacts(self):
        pickle.dump( self.contacts, open(self.username + ".p", "wb" ))

    def __call__(self):
        print("Account: {!r}".format(self.username))
        for contact in self.contacts:
            print(repr(contact))

    def __getitem__(self, index)-> Contact:
        return self.contacts[index]

    def __len__(self):
        return len(self.contacts)

    def __reversed__(self):
        return self[::-1]
        




