#dfs 

graph = { 
    'A' : ['E' , 'B'],
    'B' : ['C' , 'D' , 'A'],
    'C' : ['E' , 'D'],
    'D' : ['C' , 'B'],
    'E' : ['A', 'C']
}
visited = set()                                                                                                             

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
dfs(visited , graph , 'A','C')

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
bfs(vis , graph , 'A','C')
    
    
