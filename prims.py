INF=99999999  #assume_infinite number
v=5 #No_of_vertices in graph
g=[
     [0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]
]      
selected = [0,0,0,0,0] 
no_edge = 0 
selected[0] = True
print("Edge : Weight\n")
while(no_edge<v-1): 
    minimum = INF               
    x=0
    y=0
    for i in range(v):
        if selected[i]:
            for j in range(v):
                if((not selected[j]) and g[i][j]):
                    if minimum > g[i][j]:
                        minimum = g[i][j]
                        x=i
                        y=j
    print(str(x)+"-"+str(y)+":"+str(g[x][y]))
    selected[y]= True
    no_edge += 1
--------------------------------------------------------------
output - 
Edge : Weight

0-1:9
1-3:19
3-4:31
3-2:51
