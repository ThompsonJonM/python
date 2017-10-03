# Lists are what arrays would be in JS
simple_array = [1, 2, 3]

print('The first element of simple_array is {0}.'.format(simple_array[0]))

# Add elements
simple_array.append(4)
print(simple_array)

# 
simple_array += [5]
print(simple_array)

#
simple_array.extend([6, 7, 8])
print(simple_array)