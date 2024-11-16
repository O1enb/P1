
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = list(abs(len(x) - len(y))  for x,y in zip(first, second) if len(x) != len(y))
print(first_result)

second_result = list(True if len(first[i]) == len(second[i]) else False for i in range(0,min(len(first), len(second))))
print(second_result)