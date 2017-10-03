def greet(name):
    return 'Hi, {0}!'.format(name)

print(greet('Cicero'))

def test(name = 'Jona'):
    return 'Hello, {0}.'.format(name)

print(test('Dead leaves on the dirty ground'))
print(test())

def print_separator(repetitions = 18):
    print('-' * repetitions)

def print_name(first = 'Jane', middle = 'D', last = 'Doe'):
    print('{0} {1} {2}'.format(first, middle, last))

print_name(last = 'Cesar', middle = 'J', first = 'Gaius')

print_separator()

def reveal(*args):
    for arg in args:
        print('You passed the argument', arg)

reveal(1, 2, 3, 4, 'OMG')

print_separator()

def reveal_kwargs(**kwargs):
    for kwarg in kwargs:
        print('You passed the argument', kwarg)

reveal_kwargs(first = 'fish', second = 'stew')

print_separator()

def students_greet

