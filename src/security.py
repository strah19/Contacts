import math

class PasswordStrength:
    def __init__(self, name, length, special_charcters, caps, nums):
        self.name = name
        self.length = length
        self.special_charcters = special_charcters
        self.caps = caps
        self.nums = nums
    def check_password(self, password):
        pass_len = len(password)
        symbols = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',';','<',',','>','.','?','/'}
        symbol_counter = 0
        cap_count = 0
        num_count = 0
        if pass_len >= self.length[0] and pass_len <= self.length[1]:
            for p in password:
                for s in symbols:
                    if p == s:
                        symbol_counter += 1
            cap_count = sum(p.isupper()for p in password)
            num_count = sum(p.isdigit()for p in password)
        if symbol_counter >= self.special_charcters[0] and symbol_counter <= self.special_charcters[1] and cap_count >= self.caps[0] and cap_count <= self.caps[1] and num_count >= self.nums[0] and num_count <= self.nums[1]:
            return True

        return False

    def get_password_strength(self):
        return self.name

class AccountSecurity:
    sec = open("security.txt", "r+")       
    
    def __init__(self):
        self.username = ""

    def __del__(self):
        AccountSecurity.sec.close()

    def create_new_account(self, username, password):
        if self.check_existing_accounts(username + '\n'):
            return False;

        AccountSecurity.sec.seek(0, 2)
        AccountSecurity.sec.write(username + '\n')
        AccountSecurity.sec.write(password + '\n')

        self.username = username

        AccountSecurity.sec.seek(0)
        return True

    def check_existing_accounts(self, new_username):
        created_usernames = []

        index = 0
        for line in AccountSecurity.sec:
            if index % 2 == False:
                created_usernames.append(line)
            index += 1

        for username in created_usernames:
            if username == new_username:
                return True
        
        AccountSecurity.sec.seek(0)
        return False

    def enter_username(self, username):
        self.username = username
    
    def enter_password(self, password):
        AccountSecurity.sec.seek(0)
        found = False
        for line in AccountSecurity.sec:
            if line == self.username + '\n':
                found = True
            elif found and line == password + '\n':
                AccountSecurity.sec.seek(0)
                return True
        AccountSecurity.sec.seek(0)
        return False

    def check_password_strength(self, password):
        password_strengths = [PasswordStrength("Strong", (8, math.inf), (1, math.inf), (1, math.inf), (2, 2)), PasswordStrength("Weak", (1, 7), (0, 0), (0, 0), (0, 0))]

        for strength in password_strengths:
            if strength.check_password(password):
                return strength.get_password_strength()
        return "Password does not fit in any strength."

    def get_username(self):
        return self.username

