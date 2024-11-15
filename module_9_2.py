
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)

second_result = [(first_strings[i], second_strings[i]) for i in range(min(len(first_strings), len(second_strings)))]
print(second_result)

third_result = {string: len(string) for i in range(min(len(first_strings), len(second_strings))) for string in (first_strings[i], second_strings[i]) if len(first_strings) % 2}
print(third_result)