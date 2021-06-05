
class Contact:
    def __init__(self, name = "New Contact", phone_numbers = [], phone_number_names = [], email = "Email", address = "Address"):
        self.name = name
        self.phone_numbers = phone_numbers
        self.phone_number_names = phone_number_names
        self.email = email
        self.address = address

    def __repr__(self):
        return 'Contact: {!r} with phone numbers of {!r}, address: {!r}, email: {!r}'.format(self.name, self.phone_numbers, self.address, self.email)
    
    
