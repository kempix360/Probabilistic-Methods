import random
import matplotlib.pyplot as plt

n = 100000

# task 1
array = []

for _ in range(n):
    rand = random.random()
    x = 100 * rand + 50
    array.append(x)

ranges = [0] * 10
for number in array:
    ranges[int((number - 50) / 10)] += 1
print(ranges)

# plt.hist(array)
plt.show()

# task 2
def generator(n):
    num_of_1 = 0
    num_of_2 = 0
    num_of_3 = 0
    num_of_4 = 0
    for _ in range(n):
        rand_num = random.random()
        if rand_num < 0.2:
            num_of_1 += 1
        elif rand_num < 0.5:
            num_of_2 += 1
        elif rand_num < 0.9:
            num_of_3 += 1
        else:
            num_of_4 += 1

    return num_of_1, num_of_2, num_of_3, num_of_4


print("Task 2:")
num_of_1, num_of_2, num_of_3, num_of_4 = generator(n)
print("Number of 1: " + str(num_of_1))
print("Number of 2: " + str(num_of_2))
print("Number of 3: " + str(num_of_3))
print("Number of 4: " + str(num_of_4))
