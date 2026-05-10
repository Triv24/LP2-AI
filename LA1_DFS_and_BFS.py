#dfs 

def create_graph():
    vertices = int(input("Enter total number of vertices : "))

    graph = {}

    for i in range(vertices) :
        vertex = input("Enter the Vertex : ")
        adj_list = input(f"Enter the space separated adjacent vertices for the vertex '{vertex}'' : ").split()
        graph[vertex] = adj_list
        
    return graph

graph = create_graph()
visited = set()  
start = input("Enter the starting Node : ")
goal = input("Enter the goal node : ")                                                                                                           

def dfs (visited , graph , s,goal):
    
    if s not in visited:
        print(s)
        visited.add(s)
        if s==goal:
            print("Goal node Visited")
            return True
        
        for child in graph[s]:
                if dfs(visited , graph , child,goal):
                    return True
    return False

            
            
print('dfs:')            
dfs(visited, graph, start, goal)

#bfs

vis =[]
queue = []

def bfs(vis , graph , s,goal):
    
    vis.append(s)
    queue.append(s)
    
    
    while queue :
        element = queue.pop(0)
        print(element)
        if element==goal:
            print("Goal node Visited")
            return True
        
        for child in graph[element]:
            if child not in vis:
                vis.append(child)
                queue.append(child)
                

print('bfs:')            
bfs(vis , graph , start, goal)
    
    
