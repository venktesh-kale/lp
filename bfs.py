from collections import deque

def bfs(graph, queue, visited):
    if not queue:
        return 
    node = queue.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    bfs(graph, queue, visited)

    
graph = { 
  '0':['1','2'],
  '1':['0','2','3'],
  '2':['0','1','4'],
  '3':['1','4'],
  '4':['2','3']
}

start = '1'
queue = deque([start])
visited = set()
visited.add(start)

print("BF traversal of the graph : ")
bfs(graph, queue, visited)

