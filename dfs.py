def dfs (visited, graph , node):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited, graph , neighbour)

graph = {
     '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : ['5','7'],
  '4' : ['8'],
  '8' : []
}

visited = set()
dfs(visited, graph, '3')


