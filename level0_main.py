import math
import json

def two_opt(tour, distances):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue  # changes nothing, skip then
                new_tour = tour[:]
                new_tour[i:j] = tour[j - 1:i - 1:-1]  # reverse the sub-route
                if total_distance(new_tour, distances) < total_distance(tour, distances):
                    tour = new_tour
                    improved = True
    return tour

def solve_tsp_nearest(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_dist = 0
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True

    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = math.inf

        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance

        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_dist += nearest_distance

    tour.append(0)
    total_dist += distances[current_city][0]

    return tour, total_dist

def total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

f = open(r'Student Handout\Input data\level0.json')
data = json.load(f)
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

tour, total_dist = solve_tsp_nearest(dist)
optimized_tour = two_opt(tour, dist)

for i in range(len(tour)):
    tour[i] = neig[tour[i]]

print("Nearest Neighbor Tour:", tour)
print("Nearest Neighbor Total distance:", total_dist)
print("Optimized Total distance:", total_distance(optimized_tour, dist))

for i in range(len(optimized_tour)):
    optimized_tour[i] = neig[optimized_tour[i]]

print("Optimized Tour:", optimized_tour)
output_dict={"v0": {"path":optimized_tour}}
json_object = json.dumps(output_dict, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)