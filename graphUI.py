m = 999999
V = int(input("number of vertices"))


def print_solution(color):
    print("Solution Exists: Following are the assigned colors")
    print(" ".join(map(str, color)))


def is_safe(v, graph, color, c):
    
    for i in range(V):
        if graph[v][i] and c == color[i]:
            return False
    return True


def graph_coloring_check(graph, m, color, v):
   
    if v == V:
        return True

    for c in range(1, m + 1):
        
        if is_safe(v, graph, color, c):
            color[v] = c

           
            if graph_coloring_check(graph, m, color, v + 1):
                return True

            color[v] = 0

    return False


def graph_coloring(graph):
    color = [0] * V

    if not graph_coloring_check(graph, m, color, 0):
        print("Solution does not exist")
        return False

    print_solution(color)
    return True


graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]



graph_coloring(graph)

