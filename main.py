import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import statistics as stat


# Create Network: This function is to create a network based on the provided information
# in the Kangaroo and Bison Network files.
# Parameters: The Imported, created Graph and The Lines from that Graph

def create_network(graph, file, flag):
    opened_file = open(file, 'r')
    lines = opened_file.readlines()

    for ln in lines[2:-1]:
        start_node = int(ln.split(' ')[0])
        end_node = int(ln.split(' ')[1])
        edge_length = float(ln.split(' ')[2])
        graph.add_edge(start_node, end_node, weight=edge_length)

    pos = nx.spring_layout(graph)
    if flag == True:
        plt.figure(1)
        plt.title('Directed Bison graph')
    else:
        plt.figure(2)
        plt.title('Undirected Kangaroo graph')
    # Nodes
    nx.draw_networkx_nodes(graph, pos, node_size=50)
    # Edges
    nx.draw_networkx_edges(graph, pos, width=1)
    # plt.show()


# Compare: A function to check is two graphs are isomorphic AKA equivalent

def compare(g1, g2):
    if nx.is_isomorphic(g1, g2):
        print("These graphs are Equivalent")
    else:
        print("These graphs are NOT Equivalent")


# Add10Edges: adds ten edges to a graph based on two arbritary integers
def add_10_edges(graph, size):
    for i in range(1, 10):
        x = random.randrange(1, size, 1)
        y = random.randrange(1, size, 1)
        while x == y:
            x = random.randrange(1, size, 1)
        graph.add_edge(x, y)


# Tree Or Forest: Checks if a graph is a tree forest for neither
def tree_or_forest(graph):
    if nx.is_tree(graph):
        print("The Minimum Spanning Tree Generated from this Network is a Tree")
    elif nx.is_forest(graph):
        print("The Minimum Spanning Tree Generated from this Network is a Forest")
    else:
        print("Neither a Tree nor Forest")


# Stats: computes mean and standard deviations creating a label out of the two
def stats(data):
    mean = stat.mean(data)
    std_deviation = stat.stdev(data)
    x_label = 'Mean = ' + str(mean) + ' & Standard Deviation = ' + str(std_deviation)
    return x_label


# Main Function for the program.
def main():
    # Directed Bison Network
    bison_file = 'moreno_bison/out.moreno_bison_bison'
    bison_graph = nx.DiGraph()

    create_network(bison_graph, bison_file, True)

    # Undirected Kangaroo Network
    kangaroo_file = 'moreno_kangaroo/out.moreno_kangaroo_kangaroo'
    kangaroo_graph = nx.Graph()

    create_network(kangaroo_graph, kangaroo_file, False)

    # Part A: Connected Component Analysis
    # Connected Component Analysis of Bison Directed Graph
    print("PART A:\n")
    print("Bison Directed Graph Connected Component Analysis",
          "\nWeakly connected: ", nx.is_weakly_connected(bison_graph),
          "\nNumber of Weakly CCs: ", nx.number_weakly_connected_components(bison_graph),
          "\nSize of largest CC: ", len(max(nx.weakly_connected_components(bison_graph), key=len)),
          "\nSize of smallest CC: ", len(min(nx.weakly_connected_components(bison_graph), key=len)))

    # Connected Component Analysis of Kangaroo Undirected Graph
    print("\nKangaroo Undirected Graph Connected Component Analysis",
          "\nConnected: ", nx.is_connected(kangaroo_graph),
          "\nNumber of CCs: ", nx.number_connected_components(kangaroo_graph),
          "\nSize of largest CC: ", len(max(nx.connected_components(kangaroo_graph), key=len)),
          "\nSize of smallest CC: ", len(min(nx.connected_components(kangaroo_graph), key=len)))

    # Part B Computing Degrees and finding the Probability distribution
    # Creation of an arrayList to store the degree for each node of Bison Network
    bison_degrees = []
    for node in range(1, 26):
        bison_degrees.append(bison_graph.degree(node))

    # Computing Mean and Standard Deviation for Directed
    x_label = stats(bison_degrees)

    # Creating a Histogram to plot the data of the degrees Bison Network
    plt.figure(3)
    plt.title('Part B: Histogram Directed Bison')
    plt.xlabel(x_label)
    plt.hist(bison_degrees, bins='auto')

    # Creation of an arrayList to store the degree for each node of Kangaroo Network
    kangaroo_degrees = []
    for node in range(1, 17):
        kangaroo_degrees.append(kangaroo_graph.degree(node))

    # Computing Mean and Standard Deviation for Undirected
    x_label = stats(kangaroo_degrees)

    # Creating a Histogram to plot the data of the degrees for Kangaroo Network
    plt.figure(4)
    plt.title('Part B: Histogram Undirected Kangaroo')
    plt.xlabel(x_label)
    plt.hist(kangaroo_degrees, bins='auto')
    # lt.show()

    # Part C Find the Path between 2 abritrary vertices in the largest CC
    # Creating two arbritrary nodes making sure they aren't the same number
    node1 = random.randrange(1, 27, 1)
    node2 = random.randrange(1, 27, 1)
    while node1 == node2:
        node1 = random.randrange(1, 27, 1)

    # I put a cutoff on the list of simple paths for now so I can atleast run something
    # cut off is the act of only focusing on the paths <= 5
    # This section creates a list of all simple paths and then creates a list with the lengths of these paths
    bison_paths = list(nx.all_simple_paths(bison_graph, node1, node2, cutoff=5))
    bison_p_lengths = []

    for node in range(0, len(bison_paths) - 1):
        bison_p_lengths.append(len(bison_paths[node]))

    x_label = stats(bison_p_lengths)

    # Creating a histogram for the degrees of the graph
    plt.figure(5)
    plt.title('Part C: Histogram Directed Bison Paths')
    plt.xlabel(x_label)
    plt.hist(bison_p_lengths, bins='auto')
    # plt.show()

    # Creating two arbitrary nodes making sure they aren't the same number
    node1 = random.randrange(1, 17, 1)
    node2 = random.randrange(1, 17, 1)
    while node1 == node2:
        node1 = random.randrange(1, 17, 1)

    # This section creates a list of all simple paths and then creates a list with the lengths of these paths
    kangaroo_paths = list(nx.all_simple_paths(kangaroo_graph, node1, node2, cutoff=5))
    kangaroo_p_lengths = []

    for node in range(0, len(kangaroo_paths) - 1):
        kangaroo_p_lengths.append(len(kangaroo_paths[node]))

    x_label = stats(kangaroo_p_lengths)

    # Creating a histogram for the degrees of the graph
    plt.figure(6)
    plt.title('Part C: Histogram Undirected Kangaroo Paths')
    plt.xlabel(x_label)
    plt.hist(kangaroo_p_lengths, bins='auto')

    # plt.show()

    # Part D Find the Simple Circuits between 2 abritrary vertices in the largest CC
    # UNABLE TO RUN BISON CIRCUITS ON LAPTOP THERE ARE TO MANY AND I CANNOT CREATE A CUTOFF

    # Creates a list of simple cycles and then creates another list of the lengths of the cycles
    # bison_circuits = list(nx.simple_cycles(bison_graph))
    # bison_c_lengths = []
    # for node in range(0,len(bison_circuits)-1):
    #    bison_c_lengths.append(len(bison_circuits[node]))
    #
    # x_label = stats(bison_c_lengths)
    #
    # plt.figure(7)
    # plt.title('PART D: Histogram Directed Bison Circuits')
    # plt.xlabel(x_label)
    # plt.hist(bison_c_lengths, bins = 'auto')

    # You can't use the simple cycle function for undirected graphs so I used the basis function.
    # Creates a list of simple cycles and then creates another list of the lengths of the cycles
    kangaroo_circuits = nx.cycle_basis(kangaroo_graph)
    kangaroo_c_lengths = []
    for node in range(0, len(kangaroo_circuits) - 1):
        kangaroo_c_lengths.append(len(kangaroo_circuits[node]))

    x_label = stats(kangaroo_c_lengths)
    plt.figure(7)
    plt.title('PART D: Histogram Undirected Kangaroo Circuits')
    plt.xlabel(x_label)
    plt.hist(kangaroo_c_lengths, bins='auto')
    # plt.show()

    # Part E Check if Eulerian, Find a Eulerian Path
    print("\nPART E:")
    print("\nDirected Bison Graph")
    print("Euelerian: ", nx.is_eulerian(bison_graph))
    print("Has a Eulerian Path: ", nx.has_eulerian_path(bison_graph))

    print("\nUndirected Kangaroo Graph")
    print("Euelerian: ", nx.is_eulerian(kangaroo_graph))
    print("Has a Eulerian Path: ", nx.has_eulerian_path(kangaroo_graph))

    # Part F: Convert to Matrix.
    # I don't know if this covers everything?
    bison_matrix = nx.to_numpy_matrix(bison_graph)
    plt.matshow(bison_matrix)
    # plt.show()

    kangaroo_matrix = nx.to_numpy_matrix(kangaroo_graph)
    plt.matshow(kangaroo_matrix)
    # plt.show()

    # Part G: Copy Largest CC comparing it to a copy and a slightly different CC
    print("\nPart G:\n")
    # copying the largest connected component from the Bison Directed graph
    bison_n1 = nx.Graph()
    largest_cc_bison = list(max(nx.weakly_connected_components(bison_graph), key=len))
    for i in largest_cc_bison:
        bison_n1.add_edge(i, i + 1)
    bison_n2 = bison_n1.copy()

    # Checking Equivalence between copied graphs
    print("Is bison_n1 Equivalent to bison_n2?")
    compare(bison_n1, bison_n2)

    # Checking Equivalence between copied graphs but one has an extra 10 edges
    print("\nIs bison_n1 Equivalent to N3?")
    bison_n3 = bison_n2.copy()
    add_10_edges(bison_n3, len(bison_n3))
    compare(bison_n1, bison_n3)

    # Repeat for Kangaroo Undirected Network
    kangaroo_n1 = nx.Graph()
    largest_cc_kangaroo = list(max(nx.connected_components(kangaroo_graph), key=len))
    for i in largest_cc_kangaroo:
        kangaroo_n1.add_edge(i, i + 1)
    kangaroo_n2 = kangaroo_n1.copy()

    print("\nIs kangaroo_n1 Equivalent to kangaroo_n2?")
    compare(kangaroo_n1, kangaroo_n2)

    print("\nIs kangaroo_n1 Equivalent to N3?")
    kangaroo_n3 = kangaroo_n2.copy()
    add_10_edges(kangaroo_n3, len(kangaroo_n3))
    compare(kangaroo_n1, kangaroo_n3)

    # Part H: Generate Minimum Spanning Tree
    print("\nPart H:\n")
    # Cannot generate SPanning tree for Directed networks
    # Generating a minimum spanning tree for Undirected network
    kangaroo_min_tree = nx.minimum_spanning_tree(kangaroo_graph)
    print("~A Minimum Spanning Tree was created for the Undirected Kangaroo Graph~")
    tree_or_forest(kangaroo_min_tree)

    # Finding two random nodes that are connected
    x = 0
    y = 0
    while (not (kangaroo_min_tree.has_edge(x, y))):
        x = random.randrange(1, 17, 1)
        y = random.randrange(1, 17, 1)
        while x == y:
            x = random.randrange(1, 17, 1)

    # Removing the found edge
    print("\nAn edge from the spanning tree was removed")
    kangaroo_min_tree.remove_edge(x, y)
    tree_or_forest(kangaroo_min_tree)

    # Part I: Dijkstra's Algorithm

    bison_pairs = list(nx.all_pairs_node_connectivity(bison_graph))
    connected_nodes = []
    for i in bison_pairs:
        for j in bison_pairs:
            if bison_graph.has_edge(i, j + 1):
                connected_nodes.append([i, j + 1])

    dijkstra_paths = []
    length = len(connected_nodes)
    for i in range(0, length - 1):
        for j in range(0, 1):
            dijkstra_paths.append(
                int(nx.dijkstra_path_length(bison_graph, connected_nodes[i][j], connected_nodes[i][j + 1])))

    x_label = stats(dijkstra_paths)

    plt.figure()
    plt.xlabel(x_label)
    plt.title('Directed Bison Dijkstra Path Lengths')
    plt.hist(dijkstra_paths)
    # plt.show()

    #Created a new temporary graph with edges from the connected nodes and weights from the distance list
    temp_bison = nx.DiGraph()
    for i in range(0, length - 1):
        j = 0
        temp_bison.add_edge(connected_nodes[i][j], connected_nodes[i][j + 1], weight=dijkstra_paths[i])

    # I dont really know if this creates a matrix for the weigths this is just what i did in a previous part
    bison_distance_matrix = nx.to_numpy_matrix(temp_bison)
    plt.matshow(bison_distance_matrix)
    plt.show()

    # Repeat for Kangaroo Undirected



    KangarooPairs = list(nx.all_pairs_node_connectivity(KangarooGraph))
    ConnectedNodesK = []
    for i in KangarooPairs:
        for j in KangarooPairs:
            if KangarooGraph.has_edge(i, j + 1):
                ConnectedNodesK.append([i, j + 1])

    dijkstra_PathsK = []
    length = len(ConnectedNodesK)
    for i in range(0, length):
        dijkstra_PathsK.append(int(nx.dijkstra_path_length(KangarooGraph, ConnectedNodesK[i][0], ConnectedNodesK[i][1])))
    xLabel = Stats(dijkstra_PathsK)

    plt.figure()
    plt.xlabel(xLabel)
    plt.title('Undirected Kangaroo Dijkstra Path Lengths')
    plt.hist(dijkstra_PathsK)
    plt.show()


    temp_kangaroo = nx.Graph()
    for i in range(0, length - 1):
        j = 0
        temp_kangaroo.add_edge(ConnectedNodesK[i][j], ConnectedNodesK[i][j + 1], weight=dijkstra_PathsK[i])


    kangaroo_distance_matrix = nx.to_numpy_matrix(temp_kangaroo)
    plt.matshow(kangaroo_distance_matrix)
    plt.show()


main()





