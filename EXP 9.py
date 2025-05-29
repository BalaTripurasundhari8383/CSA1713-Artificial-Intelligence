import itertools

def calculate_total_distance(permutation, distance_matrix):
    total_distance = 0
    for i in range(len(permutation) - 1):
        total_distance += distance_matrix[permutation[i]][permutation[i + 1]]
    total_distance += distance_matrix[permutation[-1]][permutation[0]]  # Return to start
    return total_distance

def travelling_salesman_brute_force(distance_matrix):
    cities = list(range(len(distance_matrix)))
    min_path = None
    min_distance = float('inf')

    for permutation in itertools.permutations(cities):
        current_distance = calculate_total_distance(permutation, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = permutation

    return min_path, min_distance

# Sample input: distance matrix (symmetric)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, distance = travelling_salesman_brute_force(distance_matrix)
print("Minimum path:", path)
print("Minimum distance:", distance)
