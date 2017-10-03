class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

jim = User('Jim', 'Doe', 'jim@gmail.com')

print(jim.first_name)
print(jim.last_name)
print(jim.email)