import math
import json
import random

def solve_tsp_aco(distances, start_node, num_ants=10, num_iterations=100, alpha=1.0, beta=2.0, rho=0.5, Q=100.0):
    num_cities = len(distances)
    pheromone = [[1.0 / num_cities] * num_cities for _ in range(num_cities)]

    best_tour = None
    best_distance = float('inf')

    for iteration in range(num_iterations):
        ant_tours = []

        # Construct solutions with ants, starting from the specified node
        for ant in range(num_ants):
            tour = construct_tour(distances, pheromone, alpha, beta, start_node)
            ant_tours.append((tour, total_distance(tour, distances)))

        # Update pheromone levels
        update_pheromone(pheromone, ant_tours, rho, Q)

        # Update best tour
        for tour, distance in ant_tours:
            if distance < best_distance:
                best_tour = tour
                best_distance = distance

    return best_tour, best_distance

def construct_tour(distances, pheromone, alpha, beta, start_node):
    num_cities = len(distances)
    unvisited_cities = set(range(num_cities))
    unvisited_cities.remove(start_node)
    current_city = start_node
    tour = [current_city]

    while unvisited_cities:
        probabilities = calculate_probabilities(current_city, unvisited_cities, pheromone, distances, alpha, beta)
        next_city = random.choices(list(unvisited_cities), weights=probabilities)[0]
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city

    return tour

def calculate_probabilities(current_city, unvisited_cities, pheromone, distances, alpha, beta):
    epsilon = 1e-10  # Small constant to avoid division by zero
    probabilities = []

    for city in unvisited_cities:
        pheromone_value = pheromone[current_city][city]
        distance_value = 1.0 / (distances[current_city][city] + epsilon)
        probabilities.append((pheromone_value ** alpha) * (distance_value ** beta))

    total_prob = sum(probabilities)
    probabilities = [prob / total_prob for prob in probabilities]
    return probabilities


def update_pheromone(pheromone, ant_tours, rho, Q):
    evaporation = 1.0 - rho
    for i in range(len(pheromone)):
        for j in range(len(pheromone[i])):
            pheromone[i][j] *= evaporation

    for tour, distance in ant_tours:
        pheromone_contrib = Q / distance
        for i in range(len(tour) - 1):
            pheromone[tour[i]][tour[i + 1]] += pheromone_contrib

def total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Load data from JSON file
with open(r'Student Handout\Input data\level0.json') as f:
    data = json.load(f)

# Prepare distance matrix
dist = []
rest_to_neig = data['restaurants']['r0']['neighbourhood_distance']
neig = list(data['neighbourhoods'].keys())

for i in range(len(data['neighbourhoods'])):
    temp = list(data['neighbourhoods'][neig[i]]['distances'])
    temp.insert(0, rest_to_neig[i])
    dist.append(temp)

rest_to_neig.insert(0, 0)
dist.insert(0, rest_to_neig)
neig.insert(0, 'r0')
start_node = 0  # Change this to the desired starting node index

# Solve TSP using ACO with a specified starting node
best_tour, best_distance = solve_tsp_aco(dist, start_node, num_ants=10, num_iterations=100, alpha=1.0, beta=2.0, rho=0.5, Q=100.0)

# Convert indices back to neighborhood names
best_tour = [neig[i] for i in best_tour]
best_tour.append('ro')
print("Best ACO Tour with specified starting node:", best_tour)
print("Best ACO Total distance:", best_distance)
