import math


class Linear_Generator:
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.X = seed

    def generate(self, n):
        array = []
        for i in range(n):
            self.X = (self.a * self.X + self.c) % self.m
            array.append(self.X)
        return array

    def count(self, array):
        ranges = [0] * 10
        for number in array:
            ranges[int(number * 10 / self.m)] += 1
        return ranges


a = 69069
c = 1
m = 2 ** 31
seed = 15

linear_generator = Linear_Generator(a, c, m, seed)
array = linear_generator.generate(100000)
print(array)
print("Amounts of numbers in ranges:")
print(linear_generator.count(array))


class Register_Generator:
    def __init__(self, p, q, seed):
        self.seed = seed
        self.p = p
        self.q = q

    def generate(self, n):
        x = self.seed + [0] * 25
        array = []
        for _ in range(n):
            for i in range(len(self.seed), len(x)):
                x[i] = (x[i - self.p] ^ x[i - self.q])
            number = 0
            for j in range(1, len(x) + 1):
                number += 2 ** (-j) * x[j-1]
            array.append(number)
            x[:7] = x[-7:]
        return array

    def count(self, array):
        ranges = [0] * 10
        for number in array:
            ranges[int(number * 10)] += 1
        return ranges


p = 7
q = 3
seed = [1, 0, 0, 1, 1, 0, 1]
register_generator = Register_Generator(p, q, seed)
array = register_generator.generate(100000)
print(array)
print("Amounts of numbers in ranges:")
print(register_generator.count(array))
