from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        ###TODO
        curr_node = frontier.pop()
        neighbors = graph[curr_node]
        for neighbor in neighbors:
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
     
    return result

def connected(graph):
    #base case 
    if len(graph) == 0:
        return True
    for node in graph:
        start_node = node
        break
    return len(reachable(graph, start_node)) == len(graph)
    ### TODO


def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    visited=set()
    count = 0
    for node in graph:
        if node not in visited:
            count +=1 
            results = reachable(graph, node)
            for result in results:
                if result not in visited:
                    visited.add(result)

    return count



    
