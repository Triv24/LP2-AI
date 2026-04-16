def printConfiguration(colorArray):
    print("The assigned colors are as follows:")
    for i in range(len(colorArray)):
        print("Vertex:", i, "Color:", colorArray[i])
def isSafe(graph, colorArray):
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] and colorArray[j] == colorArray[i]:
                return False
    return True
def graphColoringAlgorithm(graph, m, i, colorArray):
    if i == len(graph):
        if isSafe(graph, colorArray):
            printConfiguration(colorArray)
            return True
        return False

    for j in range(1, m + 1):
        colorArray[i] = j
        if graphColoringAlgorithm(graph, m, i + 1, colorArray):
            return True
        colorArray[i] = 0
    return False


if __name__ == '__main__':
    num_vertices = int(input("Enter the number of vertices: "))
    graph = []
    print("Enter the adjacency matrix for the graph (0 for no edge, 1 for edge):")
    for _ in range(num_vertices):
        graph.append(list(map(int, input().split())))
    m = int(input("Enter the maximum number of colors allowed: "))

    colorArray = [0] * num_vertices

    if graphColoringAlgorithm(graph, m, 0, colorArray):
        print("Coloring is possible!")
    else:
        print("Coloring is not possible!")
