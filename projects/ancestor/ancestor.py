from ancestor_graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for tupl in ancestors:
        if tupl[0] not in graph.vertices and tupl[1] not in graph.vertices:
            graph.add_vertex( tupl[1] )
            graph.add_vertex( tupl[0] )

            graph.add_edge( tupl[1], tupl[0] )

        elif tupl[0] not in graph.vertices:
            graph.add_vertex( tupl[0] )
            graph.add_edge( tupl[1], tupl[0] )

        elif tupl[1] not in graph.vertices:
            graph.add_vertex( tupl[1] )
            graph.add_edge( tupl[1], tupl[0] )

        else:
            graph.add_edge( tupl[1], tupl[0] )

    lineage = graph.dft( starting_node )
    


    if len( lineage ) > 2: 
        earliest_child = lineage[-3]
        parents = graph.get_neighbors( earliest_child )

        if lineage[-1] in parents and lineage[-2] in parents:
            if lineage[-1] > lineage[-2]:
                return lineage[-2]

    if len( lineage ) > 1: return lineage[-1]
    else: return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor( test_ancestors, 8 )