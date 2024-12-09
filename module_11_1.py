import numpy as np
import random as rnd
import requests as rq

l1 = np.array(list(rnd.randint(1000, 10000) for _ in range(1, 100)))
result = np.array(list(l1[i] - l1[i-1] for i in range(len(l1))))

result2 = np.array(l1 * np.roll(l1, -1))

result3 = np.array([result, result2])

result4 = np.transpose(result3)

print(result)
print(result2)
print(result3)
print(result4)


r = rq.get("https://www.google.com")

if r.status_code == 200:
    print('success')
else:
    print('Fail')

print(r.text)

r = rq.options("https://www.google.com")

print(r.text)