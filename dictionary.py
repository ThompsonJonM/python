list = []

person_keys = ['first_name', 'last_name', 'height', 'gender']

# print(dict.fromkeys(person_keys))

person = dict.fromkeys(person_keys)

person['first_name'] = input('What is your first name?')
person['last_name'] = input('What is your last name?')
person['height'] = input('What is your height?')
person['gender'] = input('What do you identify as?')

print(person)
