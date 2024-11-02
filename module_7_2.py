import io


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    str_num = 0
    strings_positions = {}
    for string in strings:
        file.write(f'{string}\n')
        str_num += 1
        strings_positions.update({(str_num, file.tell()): string})
    file.close()
    return strings_positions

info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

result = custom_write('products.txt', info)
for elem in result.items():
    print(elem)