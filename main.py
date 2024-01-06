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
print(dist)
n=20

