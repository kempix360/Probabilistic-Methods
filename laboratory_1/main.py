from math import sqrt


def getdata(file_name):
    data = []
    number_of_lines = 15

    # Reading number_of_lines first lines
    with open(file_name, 'r') as file:
        file.readline()  # Skip the first line
        for _ in range(number_of_lines):
            line = file.readline().strip().split(' ')
            id, town, population, latitude, longitude = line
            data.append((int(id), town, int(population), float(latitude), float(longitude)))

    return data


def generate_permutations(array, K):
    permutations = []

    for i in range(len(array)):
        cities = array.copy()
        cities_k = [cities[i]]
        cities.pop(i)
        add_element_permutations(cities, cities_k, K, permutations)

    return permutations


def add_element_permutations(cities, cities_k, K, permutations):
    if len(cities_k) < K:
        for index in range(0, len(cities)):
            cities_copy = cities.copy()
            cities_k_copy = cities_k.copy()
            cities_k_copy.append(cities[index])
            cities_copy.pop(index)
            add_element_permutations(cities_copy, cities_k_copy, K, permutations)
    else:
        permutations.append(cities_k)


def generate_combinations(array, K):
    combinations = []

    for i in range(len(array)):
        cities = array.copy()  # Create a copy of the original array
        cities_k = [cities[i]]
        add_element_combinations(cities, cities_k, K, combinations)

    return combinations


def add_element_combinations(cities, cities_k, K, combinations):
    if len(cities_k) < K:
        for index in range(0, len(cities)):
            if cities[index] <= cities_k[-1]:
                continue
            cities_copy = cities.copy()
            cities_k_copy = cities_k.copy()
            cities_k_copy.append(cities[index])
            add_element_combinations(cities_copy, cities_k_copy, K, combinations)
    else:
        combinations.append(cities_k)


# array = list(range(1, 7))
# N = 6
# K = 3

# permutations = generate_permutations(array, K)
# for perm in permutations:
#    print(perm)

# combinations = generate_combinations(array, K)
# for comb in combinations:
#     print(comb)

data = getdata("cities.in")
N = 4
K = 3
data_1 = data[:N]
print(data_1)

cities_permutations = generate_permutations(data_1, K)
for i in range(len(cities_permutations)):
    city_ids = [city[0] for city in cities_permutations[i]]
    print(f"{i+1}: {city_ids}")

# 1d
minimum_distance = float('inf')
result_permutation = ()
for permutation in cities_permutations:
    distance = 0
    for i in range(1, len(permutation)):
        x1 = permutation[i][3]
        x2 = permutation[i-1][3]
        y1 = permutation[i][4]
        y2 = permutation[i-1][4]
        distance += sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance < minimum_distance:
        minimum_distance = distance
        result_permutation = permutation


print("Shortest path: ", minimum_distance)
cities_names = [city[1] for city in result_permutation]
cities_string = ', '.join(cities_names)
print(f"Cities on the path: {cities_string}")

# 2d
cities_combinations = generate_combinations(data, K)
for i in range(len(cities_combinations)):
    city_ids = [city[0] for city in cities_combinations[i]]
    print(f"{i+1}: {city_ids}")
max_population = 0
result_combination = ()
for combination in cities_combinations:
    total_population = 0
    for city in combination:
        total_population += city[2]

    if total_population > max_population:
        max_population = total_population
        result_combination = combination

print("Biggest population: ", int(max_population/K))
cities_names = [city[1] for city in result_combination]
cities_string = ', '.join(cities_names)
print(f"Set of cities: {cities_string}")