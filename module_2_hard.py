result = []

def func(n):
    for num2 in range(1,20):
        for num3 in range(1,20):
            if n % (num2 + num3) == 0 and num2 < num3:
                result.append(num2)
                result.append(num3)
    return(result)




results = func(20)
print(results)
results_str = ''
for num in results:
    results_str += str(num)
print(results_str)


