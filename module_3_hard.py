data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(structs):
    summ = 0
    for struct in structs:
        if isinstance(struct, dict):
            for key, value in struct.items():
                if isinstance(key, int):
                    summ += key
                if isinstance(value, int):
                    summ += value
                if isinstance(key, str):
                    summ += len(key)
                if isinstance(value, str):
                    summ += len(value)
        elif isinstance(struct, str):
            summ += len(struct)
        elif isinstance(struct, (int, float)):
            summ += struct
        else:
            summ += calculate_structure_sum(struct)
    return summ


result = calculate_structure_sum(data_structure)
print(result)

