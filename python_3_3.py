

def print_perams(a = 1, b = "str", c = True):
    print(a,b,c)


print_perams(b = 25)
print_perams(c = [1,2,3])

values_list = [12, False, "Yes"]
values_dict = {'a': "NO", 'b': True, 'c': 37.43}

print_perams(*values_list)
print_perams(**values_dict)

values_list_2 = [34.6, "Yesnt"]

print_perams(*values_list_2, 42)
