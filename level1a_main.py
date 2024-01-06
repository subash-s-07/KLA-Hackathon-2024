import json
import math
def knapsack(W,order_dict,order):
    dp = [[0 for _ in range(W + 1)] for _ in range(len(order_dict) + 1)]

    for i in range(1, len(order_dict) + 1):
        for j in range(1, W + 1):
            if j >= order[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - order[i - 1]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]
    i = len(order_dict)
    j = W
    alloc = []

    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            alloc.append(list(order_dict.keys())[i-1])
            j = j - order[i - 1]
        i -= 1
    return alloc
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
def total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
f = open(r'Student Handout\Input data\level1a.json')
data = json.load(f)

dist = []
order_dict = {}
order=[]
neig_dict={}
neig = list(data['neighbourhoods'].keys())
rest_to_neig=data['restaurants']['r0']['neighbourhood_distance']
neig=list(data['neighbourhoods'].keys())
for i in range(0, len(data['neighbourhoods'])):
    temp = data['neighbourhoods'][neig[i]]['order_quantity']
    order.append(temp)
    order_dict[neig[i]] = temp
no_of_orders=len(order)
W = data['vehicles']['v0']['capacity']
rest_to_neig.insert(0,0)
c=0
while(order_dict):
    c+=1
    alloc=knapsack(W,order_dict,list(order_dict.values()))
    for i in range(0,len(alloc)):
        order_dict.pop(alloc[i])
    dist=[]
    for i in range(len(alloc)):
        temp=list(data['neighbourhoods'][alloc[i]]['distances'])
        temp1=[]
        rest_temp=[]
        for j in range(len(alloc)):
            temp1.append(temp[int(alloc[j][1:])])
            rest_temp.append(rest_to_neig[int(alloc[j][1:])+1])
        temp1.insert(0,rest_to_neig[int(alloc[i][1:])+1])
        dist.append(temp1)
    rest_temp.insert(0,0)
    dist.insert(0,rest_temp)
    neig.insert(0,'r0')
    tour, total_dist = solve_tsp_nearest(dist)
    optimized_tour = two_opt(tour, dist)
    print(alloc)
    print("Optimized Total distance:", total_distance(optimized_tour, dist))
    for i in range(0,len(tour)):
        if optimized_tour[i]==0:
            optimized_tour[i]='r0'
        else:
            optimized_tour[i]=alloc[optimized_tour[i]-1]
    print("Optimized Tour:", optimized_tour)
print("No of trips :",c)