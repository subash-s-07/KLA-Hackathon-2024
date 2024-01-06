import json

f = open(r'Student Handout\Input data\level1a.json')
data = json.load(f)

dist = []
order_dict = {}
neig = list(data['neighbourhoods'].keys())

for i in range(0, len(data['neighbourhoods'])):
    temp = data['neighbourhoods'][neig[i]]['order_quantity']
    dist.append(temp)
    order_dict[neig[i]] = temp

print(order_dict)

W = data['vehicles']['v0']['capacity']
W=500
dp = [[0 for _ in range(W + 1)] for _ in range(len(order_dict) + 1)]

for i in range(1, len(order_dict) + 1):
    for j in range(1, W + 1):
        if j >= dist[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - dist[i - 1]] + order_dict[neig[i - 1]])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp)

i = len(order_dict)
j = W
alloc = []

while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    else:
        j = j - dist[i - 1]
        alloc.append(neig[i - 1])
print(order_dict)
print(alloc)
