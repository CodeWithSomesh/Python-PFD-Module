import random

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = {}

class Graph:
    def __init__(self):
        self.vertices = {} # use dictionary to store the vertice and the edges
        self.adjacency_list = {} # use dictionery to store the to vertex and weight of the edges
        self.count = 0 #initialize the count to 0

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []

        # Check if the edge already exists 
        edge_exists = False
        for v, w in self.adjacency_list[vertex1]:  # the v and w is the tuples in the adjacency vertex1 list
            if v == vertex2:  #if the vertex of the adjacent vertex1 list is the same as the vertex 2 
                edge_exists = True
                self.count-=1 #decrement the count by 1,have no add the vertex2 and weight to the adjacency list of vertex1 array
                break

        if not edge_exists:  
            self.adjacency_list[vertex1].append((vertex2, weight))  # Add the vertex2 and weight to the adjacency list of vertex1 array
            self.vertices[vertex1].edges[vertex2] = weight  # Set the weight of the edge from vertex1 to vertex2 equal to the random weight 

    def list_adjacent_vertex(self, vertex):
        return self.vertices[vertex].edges #return the specific vertex edges

    def heaviest_vertex(self, vertex):
        if self.vertices[vertex].edges:  # Check if the vertex has any edges
            return max(self.vertices[vertex].edges, key=self.vertices[vertex].edges.get) # Return the heaviest vertex using max method
        else:
            return None  # Return None if the vertex has no edges
        
    def get_adjacent_vertices(self, vertex):
        return self.adjacency_list.get(vertex, []) # return the adjacent vertices of the specific vertex

# For creating the 2 graphs
def create_graph(vertices, num_edges):
    graph = Graph()
    
    # Add the vertices to the graph
    for vertex in vertices:
        graph.add_vertex(vertex) 

    # Ensure each vertex has one edge
    for i in range(len(vertices) -1):  # Loop through all vertices except the last one (minus 1 to avoid index out of range error)
        weight = random.randint(1, 30)
        graph.add_edge(vertices[i], vertices[i + 1], weight) # Add the edge between the current vertex and the next vertex
        graph.count += 1

    while graph.count < num_edges: # Loop until reach the required edges number
        # get random vertex from the vertices list
        from_vertex = random.choice(vertices) 
        to_vertex = random.choice(vertices)

        weight = random.randint(1, 10)
        graph.add_edge(from_vertex, to_vertex, weight)
        graph.count += 1
    return graph

if __name__ == "__main__":
    # Define vertices
    vertices1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    vertices2 = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

    # Create two graph objects
    graph1 = create_graph(vertices1, 30)
    graph2 = create_graph(vertices2, 30)

    # Display the graph 1
    print("\nGraph 1:")
    print("Vertices From -> To (Weight)\n")
    for graph_1_vertex in vertices1:
        adjacent_vertices = graph1.get_adjacent_vertices(graph_1_vertex)
        for adj_vertex, weight in adjacent_vertices:
            print(f"{graph_1_vertex} -> {adj_vertex} ({weight})")

    # Display the graph 2
    print("\nGraph 2:")
    print("Vertices From -> To (Weight)\n")
    for graph_2_vertex in vertices2:
        adjacent_vertices = graph2.get_adjacent_vertices(graph_2_vertex)
        for adj_vertex, weight in adjacent_vertices:
            print(f"{graph_2_vertex} -> {adj_vertex} ({weight})")

    while True:
        vertex = input("\nEnter a vertex: ")

        # Check if the vertex exists
        if vertex in graph1.vertices:
            adjacent_vertices1 = '-'.join(graph1.list_adjacent_vertex(vertex))
            heaviest_vertex1 = graph1.heaviest_vertex(vertex)
            print(f"\nGraph 1 \nVertex {vertex}: Adjacent vertices => {adjacent_vertices1 if adjacent_vertices1 else 'None'}, Heaviest vertex: {heaviest_vertex1 if heaviest_vertex1 is not None else 'None'}")
        else:
            print("\nGraph 1 \nError: The Vertex input does not exist in Graph 1.")

        if vertex in graph2.vertices:
            adjacent_vertices2 = '-'.join(graph2.list_adjacent_vertex(vertex))
            heaviest_vertex2 = graph2.heaviest_vertex(vertex)
            print(f"\nGraph 2 \nVertex {vertex}: Adjacent vertices => {adjacent_vertices2 if adjacent_vertices2 else 'None'}, Heaviest vertex: {heaviest_vertex2 if heaviest_vertex2 is not None else 'None'}")
        else:
            print("\nGraph 2 \nError: The Vertex input does not exist in Graph 2.")

        # Ask the user if they want to continue
        continue_query = input("\nDo you want to continue? (Y/N): ")
        if continue_query.lower() == 'n':
            break
        elif continue_query.lower() == 'y':
            continue
        else:
            print("Error: Invalid input. Exisitng...")
            break
