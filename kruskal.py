wi = 0

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find_parent(self, parent, i):
        
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)

       
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self,wi):

        result = []

      
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []
        for node in range(self.V):

            parent.append(node)
            rank.append(0)

        i, e = 0, 0
        while e < self.V - 1:
        
            u, v, w = self.graph[i]
            i += 1

   
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        print("Edges in the minimum spanning tree:")
        for u, v, weight in result:
            print(f"{u} - {v} : {weight}")
            wi += weight
        return wi



g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 2)
g.add_edge(3, 5, 6)
g.add_edge(4, 5, 3)

temp = g.kruskal_mst(wi)
print("Total weight of MST : ", temp)


















# Sort all the edges from low weight to high
# Take the edge with the lowest weight and add it to the spanning tree. 
# If adding the edge created a cycle, then reject this edge.
# Keep adding edges until we reach all vertices.