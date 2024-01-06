import json
f=open(r'Student Handout\Input data\level1a.json')
data = json.load(f)
dist=[]
neig=list(data['neighbourhoods'].keys())
for i in range(0,len(data['neighbourhoods'])):
    temp=data['neighbourhoods'][neig[i]]['order_quantity']
    dist.append(temp)
print(dist)
W=data['vehicles']['v0']['capacity']
dp=[0 for _ in range(W+1)]