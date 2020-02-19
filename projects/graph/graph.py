"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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
        print(path)

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

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited_vertices = set()

        queue.enqueue([ starting_vertex ])

        while queue.size() > 0:
            current_path = queue.dequeue()
            current_node = current_path[-1]

            if current_node == destination_vertex: return current_path

            else:
                if current_node not in visited_vertices:
                    visited_vertices.add(current_node)
                    neighboring_vertices = self.get_neighbors(current_node)

                    for neighbor in neighboring_vertices:
                        path_copy = list( current_path )
                        path_copy.append( neighbor )

                        queue.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited_vertices = set()

        stack.push([ starting_vertex ])

        while stack.size() > 0:
            current_path = stack.pop()
            current_node = current_path[-1]

            if current_node == destination_vertex: return current_path

            else:
                if current_node not in visited_vertices:
                    visited_vertices.add(current_node)
                    neighboring_vertices = self.get_neighbors(current_node)

                    for neighbor in neighboring_vertices:
                        path_copy = list( current_path )
                        path_copy.append(neighbor)

                        stack.push(path_copy)


    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('VERTICES:\n', graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('BFT')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT:')
    graph.dft(1)
    print( 'DFT RECURSIVE\n', graph.dft_recursive(1) )

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS:\n', graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS:\n', graph.dfs(1, 6))
    #print(graph.dfs_recursive(1, 6))
