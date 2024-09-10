
immutable_var = 1, 3, 'hi', True, [1,2,3]
print('tuple:', immutable_var)

#Меняет элемент
#immutable_var[0] = 100

mutable_list = [10, 20, 30]
print('list:', mutable_list)

mutable_list[:3] = 1, 2 ,3
print('Changed list:', mutable_list)


mmutable_var = 2, 4, 'by', False, [5, 6, 7]
print('tuple + list:', mmutable_var)

#Меняет данные внутри элемента(списка), элементом является сам список а не данные внутри него
mmutable_var[4][:3] = 50, 60, 70
print('Changed tuple + list:', mmutable_var)
