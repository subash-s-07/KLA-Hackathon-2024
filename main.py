import math
import json
"""Level 0 using Nearest Neighbor Algorithm----------------------------------------------------------"""
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
    return tour  # Move this line outside the while loop

def solve_tsp_nearest(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_distance = 0
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    
    # Repeat until all cities have been visited
    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = math.inf

        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance

        # Move to the nearest city
        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_distance += nearest_distance

    # Complete the tour by returning to the starting city
    tour.append(0)
    total_distance += distances[current_city][0]

    return tour, total_distance
# New total_distance function
def total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
f=open(r'Student Handout\Input data\level0.json')
data = json.load(f)
dist=[]
rest_to_neig=data['restaurants']['r0']['neighbourhood_distance']
neig=list(data['neighbourhoods'].keys())
for i in range(0,len(data['neighbourhoods'])):
    temp=list(data['neighbourhoods'][neig[i]]['distances'])
    temp.insert(0,rest_to_neig[i])
    dist.append(temp)
rest_to_neig.insert(0,0)
dist.insert(0,rest_to_neig)
neig.insert(0,'r0')
tour, total_dist = solve_tsp_nearest(dist)
optimized_tour = two_opt(tour, dist)
for i in range(0,len(tour)):
    tour[i]=neig[tour[i]]
print("Nearest Neighbor Tour:", tour)
print("Nearest Neighbor Total distance:", total_dist)
print("Optimized Total distance:", total_distance(optimized_tour, dist))
for i in range(0,len(tour)):
    optimized_tour[i]=neig[optimized_tour[i]]
print("Optimized Tour:", optimized_tour)

"""
Optimized Total distance: 11062
Optimized Tour: ['r0', 'n13', 'n8', 'n3', 'n16', 'n1', 'n2', 'n14', 'n17', 'n19', 'n7', 'n6', 'n5', 'n0', 'n11', 'n4', 'n15', 'n10', 'n12', 'n9', 'n18', 'r0']
"""