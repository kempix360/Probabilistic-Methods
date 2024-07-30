import random
import numpy as np

number = 100000

ex = [1, 2, 3, 4]
f_x1 = [0.2, 0.2, 0.2, 1]
f_x2 = [1, 1, 1, 1]
f_x3 = [0, 0.5, 0.5, 1]
f_x4 = [0, 0, 1, 1]

results = [[0 for _ in range(4)] for _ in range(4)]

for i in range(number):
    x = 0
    f = []
    probability_x = random.random()

    if probability_x < 0.5:
        x = 1
        f = f_x1
    elif probability_x < 0.7:
        x = 2
        f = f_x2
    elif probability_x < 0.9:
        x = 3
        f = f_x3
    else:
        x = 4
        f = f_x4

    y_index = 0
    y = random.random()
    for j in range(4):
        if y < f[j]:
            y_index = j
            break

    results[x-1][y_index] += 1

print(np.matrix(results))
print("\n")
for i in range(4):
    for j in range(4):
        print("x:" + str(i+1) + " y: " + str(j+1) + " number: " + str(results[i][j]))

