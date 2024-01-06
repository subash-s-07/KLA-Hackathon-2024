import math
"""Level 0 using Nearest Neighbor Algorithm----------------------------------------------------------"""
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
import json
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
tour, total_distance = solve_tsp_nearest(dist)
for i in range(0,len(tour)):
    tour[i]=neig[tour[i]]
print("Tour:", tour)
print("Total distance:", total_distance)
""" Solution:
Tour: [0, 14, 9, 4, 17, 2, 19, 10, 15, 18, 5, 16, 11, 13, 7, 8, 20, 6, 1, 12, 3, 0]
Total distance: 12440"""
