my_dict = {'x': 10, 'y': 20, 'z': True}
print(my_dict)

print(my_dict['y'])
print(my_dict.get('h'))

my_dict.update({'g': 3000, 't': 149})
print(my_dict.pop('z'))
print(my_dict)

my_set = {1, 3 , 3, False, 'Aye', 1}
my_set.update({12, 'Kanagroo'})
print(my_set)

my_set.discard(3)
print(my_set)
