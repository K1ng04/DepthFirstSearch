graph = {1: [2,3],
         2: [4, 5], 
         3: [6],
         4: [],
         5: [6],
         6: [7]    
}


visited = []
queue = [] 
def dfs(visited, graph, val):
    """
    Function used to illustrate the Depth First Search Algorithm Using Python

                  1
                 / \
                2   3
               / \   \
              4   5-> 6
                       \
                        7
    """
    if val not in visited:
        print(val)
        visited.append(val)
        try:
            for neighbour in graph[val]:
                 dfs(visited, graph, neighbour)
        except:
            pass
dfs(visited, graph, 1)
    
