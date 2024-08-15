import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        self.vertices.add(from_vertex)
        self.vertices.add(to_vertex)

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges.get(current_vertex, []):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

for vertex, distance in distances.items():
    print(f"Відстань від {start_vertex} до {vertex}: {distance}")
