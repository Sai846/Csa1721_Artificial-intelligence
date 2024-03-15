from itertools import permutations

def calculate_distance(city1, city2):
    # Assuming city1 and city2 are tuples (x, y) representing coordinates
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def total_distance(route, cities):
    total = 0
    for i in range(len(route) - 1):
        total += calculate_distance(cities[route[i]], cities[route[i + 1]])
    total += calculate_distance(cities[route[-1]], cities[route[0]])  # Return to the starting city
    return total

def brute_force_tsp(cities):
    shortest_route = None
    min_distance = float('inf')

    for route in permutations(range(len(cities))):
        distance = total_distance(route, cities)
        if distance < min_distance:
            min_distance = distance
            shortest_route = route

    return shortest_route, min_distance

# Example usage:
cities = [(0, 0), (1, 2), (3, 1), (2, 3)]  # Example coordinates of cities
shortest_route, min_distance = brute_force_tsp(cities)
print("Shortest Route:", shortest_route)
print("Minimum Distance:", min_distance)
