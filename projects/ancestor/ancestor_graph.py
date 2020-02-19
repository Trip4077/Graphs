class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []

    def __str__(self):
        return ' '.join([ str(node) for node in self.stack ])

    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if not vertex_id in self.vertices: self.vertices[vertex_id] = set()

        else: return "Vertice Already Exists"

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices: self.vertices[v1].add(v2)

        else: return "Invalid ID"

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices: return self.vertices[vertex_id]

        else: return "Invalid ID"

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited_vertices = set()
        path = []

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            current_node = queue.dequeue()
       
            # check if node has been visited
            if current_node not in visited_vertices:
                visited_vertices.add(current_node)
                path.append(current_node)

                neighboring_vertices = self.get_neighbors(current_node)

                for neighbor in neighboring_vertices:
                    queue.enqueue(neighbor)
        print(path)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited_vertices = set()
        path = []

        stack.push(starting_vertex)

        while stack.size() > 0:
            current_node = stack.pop()

            if current_node not in visited_vertices:
                visited_vertices.add(current_node)
                path.append(current_node)

                neighboring_vertices = self.get_neighbors(current_node)

                for neighbor in neighboring_vertices:
                    stack.push(neighbor)
        
        return path

    def dft_recursive(self, starting_vertex, visited_vertices=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited_vertices.add(starting_vertex)
    
        neighboring_vertices = self.get_neighbors(starting_vertex)

        if len( neighboring_vertices ) == 0: return

        for neighbor in neighboring_vertices:
            if neighbor not in visited_vertices:
                self.dft_recursive(neighbor, visited_vertices)

        return visited_vertices