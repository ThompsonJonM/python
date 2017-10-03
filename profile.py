# Python dictionary which is similar
# to JS objects
student_profile = {
    'first_name' : 'Jane',
    'last_name' : 'Doe',
    'middle_initial' : 'Q',
    'address' : 'Melbourne, Australia',
    'email' : 'jane@gmail.com',
    'phone_number' : '5555555500',
    }

# print(student_profile)

# print(student_profile.keys())

# print(student_profile.values())

# print('Your first name is: {0}'.format(student_profile['first_name']))

# print('Your address is: {0}'.format(student_profile['address']))

for key, value in student_profile.items():
    print('Key => {0}, value => {1}'.format(key, value))