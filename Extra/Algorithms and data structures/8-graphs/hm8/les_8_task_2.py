def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    points_dict = {}
    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'): #обходим граф в цикле

        is_visited[start]=True

        for i,vertex in enumerate(graph[start]): #проходим по строке матрицы смежности графа где хранится значение start
            list = []#set()
            # list.append(start)
            if vertex != 0 and not is_visited[i]:
                #есть ребро и вершину еще не посещали
                list.append(start) #add(i)
                points_dict[i] = list
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start] # в i вершине новое, более короткое расстояние
                    parent[i] = start #какая вершина является родительской
                    list.append(i)#add(start)
                    points_dict[i] = list

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                # list.append(i)  # add(start)
                # points_dict[i] = list
    return cost,points_dict

g = [
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0],

]
s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))