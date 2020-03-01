import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import statistics as stat


# Create Network: This function is to create a network based on the provided information
# in the Kangaroo and Bison Network files.
# Parameters: The Imported, created Graph and The Lines from that Graph

def CreateNetwork (Graph,File,flag):
    Opened_File = open(File, 'r')
    Lines = Opened_File.readlines()

    for ln in Lines[2:-1]:
        Start_node = int(ln.split(' ')[0])
        End_node = int(ln.split(' ')[1])
        Edge_length = float(ln.split(' ')[2])
        Graph.add_edge(Start_node, End_node, weight=Edge_length)

    pos = nx.spring_layout(Graph)
    if flag == True:
        plt.figure(1)
        plt.title('Directed Bison graph')
    else:
        plt.figure(2)
        plt.title('Undirected Kangaroo graph')
    # Nodes
    nx.draw_networkx_nodes(Graph, pos, node_size=50)
    # Edges
    nx.draw_networkx_edges(Graph, pos, width=1)
    #plt.show()

#Compare: A funciton to check is two graphs are isomorphic AKA equivalent
def Compare(G1,G2,):
    if nx.is_isomorphic(G1,G2):
        print("These Graphs are Equivalent")
    else:
        print("These Graphs are NOT Equivalent")

# Add10Edges: adds ten edges to a graph based on two arbritary integers
def Add10Edges(Graph,size):
    for i in range(1,10):
        x = random.randrange(1,size,1)
        y = random.randrange(1,size,1)
        while x == y:
            x = random.randrange(1,size,1)
        Graph.add_edge(x,y)

# Tree Or Forest: Checks if a graph is a tree forest for neither
def TreeOrForest(Graph):
    if nx.is_tree(Graph):
        print("The Minimum Spanning Tree Generated from this Network is a Tree")
    elif nx.is_forest(Graph):
        print("The Minimum Spanning Tree Generated from this Network is a Forest")
    else:
        print("Neither a Tree nor Forest")

# Stats: computes mean and standard deviations creating a label out of the two
def Stats(LIST):
    mean = stat.mean(LIST)
    std_Deviation = stat.stdev(LIST)
    xLabel = 'Mean = ' + str(mean) + ' & Standard Deviation = ' + str(std_Deviation)
    return xLabel

# Main Function for the program.
def main():
    #Directed Bison Network
    BisonFile = 'moreno_bison/out.moreno_bison_bison'
    BisonGraph = nx.DiGraph()

    BisonNetwork = CreateNetwork(BisonGraph,BisonFile,True)

    #Undirected Kangaroo Network
    KangarooFile = 'moreno_kangaroo/out.moreno_kangaroo_kangaroo'
    KangarooGraph = nx.Graph()

    KangaroonNetwork = CreateNetwork(KangarooGraph,KangarooFile,False)

    # Part A: Connected Component Analysis
    # Connected Component Analysis of Bison Directed Graph
    print("PART A:\n")
    print("Bison Directed Graph Connected Component Analysis",
          "\nWeakly connected: ", nx.is_weakly_connected(BisonGraph),
          "\nNumber of Weakly CCs: ", nx.number_weakly_connected_components(BisonGraph),
          "\nSize of largest CC: ", len(max(nx.weakly_connected_components(BisonGraph), key=len)),
          "\nSize of smallest CC: ", len(min(nx.weakly_connected_components(BisonGraph), key=len)))

    # Connected Component Analysis of Kangaroo Undirected Graph
    print("\nKangaroo Undirected Graph Connected Component Analysis",
          "\nConnected: ", nx.is_connected(KangarooGraph),
          "\nNumber of CCs: ", nx.number_connected_components(KangarooGraph),
          "\nSize of largest CC: ", len(max(nx.connected_components(KangarooGraph), key=len)),
          "\nSize of smallest CC: ", len(min(nx.connected_components(KangarooGraph), key=len)))


    # Part B Computing Degrees and finding the Probability distribution
    # Creation of an arrayList to store the degree for each node of Bison Network
    BisonDegrees = []
    for node in range(1,26):
        BisonDegrees.append(BisonGraph.degree(node))

    # Computing Mean and Standard Deviation for Directed
    xLabel = Stats(BisonDegrees)

    # Creating a Histogram to plot the data of the degrees Bison Network
    plt.figure(3)
    plt.title('Part B: Histogram Directed Bison')
    plt.xlabel(xLabel)
    plt.hist(BisonDegrees,bins = 'auto')

    # Creation of an arrayList to store the degree for each node of Kangaroo Network
    KangarooDegrees = []
    for node in range(1,17):
        KangarooDegrees.append(KangarooGraph.degree(node))

    # Computing Mean and Standard Deviation for Undirected
    xLabel = Stats(KangarooDegrees)

    # Creating a Histogram to plot the data of the degrees for Kangaroo Network
    plt.figure(4)
    plt.title('Part B: Histogram Undirected Kangaroo')
    plt.xlabel(xLabel)
    plt.hist(KangarooDegrees,bins = 'auto')
    #lt.show()

    #Part C Find the Path between 2 abritrary vertices in the largest CC
    # Creating two arbritrary nodes making sure they aren't the same number
    Node1 = random.randrange(1,27,1)
    Node2 = random.randrange(1,27,1)
    while Node1 == Node2:
        Node1 = random.randrange(1,27,1)

    # I put a cutoff on the list of simple paths for now so I can atleast run something
    # cut off is the act of only focusing on the paths <= 5
    # This section creates a list of all simple paths and then creates a list with the lengths of these paths
    BisonPaths = list(nx.all_simple_paths(BisonGraph,Node1,Node2,cutoff = 5))
    BisonP_Lengths = []

    for node in range(0,len(BisonPaths)-1):
        BisonP_Lengths.append(len(BisonPaths[node]))

    xLabel = Stats(BisonP_Lengths)

    # Creating a histogram for the degrees of the graph
    plt.figure(5)
    plt.title('Part C: Histogram Directed Bison Paths')
    plt.xlabel(xLabel)
    plt.hist(BisonP_Lengths, bins = 'auto')
    #plt.show()

    # Creating two arbritrary nodes making sure they aren't the same number
    Node1 = random.randrange(1,17,1)
    Node2 = random.randrange(1,17,1)
    while Node1 == Node2:
        Node1 = random.randrange(1,17,1)

    # This section creates a list of all simple paths and then creates a list with the lengths of these paths
    KangarooPaths = list(nx.all_simple_paths(KangarooGraph,Node1,Node2,cutoff = 5))
    KangarooP_Lengths = []

    for node in range(0,len(KangarooPaths)-1):
        KangarooP_Lengths.append(len(KangarooPaths[node]))

    xLabel = Stats(KangarooP_Lengths)

    # Creating a histogram for the degrees of the graph
    plt.figure(6)
    plt.title('Part C: Histogram Undirected Kangaroo Paths')
    plt.xlabel(xLabel)
    plt.hist(KangarooP_Lengths, bins = 'auto')

    #plt.show()

    # Part D Find the Simple Circuits between 2 abritrary vertices in the largest CC
    # UNABLE TO RUN BISON CIRCUITS ON LAPTOP THERE ARE TO MANY AND I CANNOT CREATE A CUTOFF

    # Creates a list of simple cycles and then creates another list of the lengths of the cycles
    # BisonCircuits = list(nx.simple_cycles(BisonGraph))
    # BisonC_Lengths = []
    # for node in range(0,len(BisonCircuits)-1):
    #    BisonC_Lengths.append(len(BisonCircuits[node]))
    #
    # xLabel = Stats(BisonC_Lengths)
    #
    # plt.figure(7)
    # plt.title('PART D: Histogram Directed Bison Circuits)
    # plt.xlabel(xLabel)
    # plt.hist(BisonC_Lengths, bins = 'auto')

    # You can't use the simple cycle function for undirected graphs so I used the basis function.
    # Creates a list of simple cycles and then creates another list of the lengths of the cycles
    KangarooCircuits = nx.cycle_basis(KangarooGraph)
    KangarooC_Lengths = []
    for node in range(0,len(KangarooCircuits)-1):
       KangarooC_Lengths.append(len(KangarooCircuits[node]))

    xLabel = Stats(KangarooC_Lengths)
    plt.figure(7)
    plt.title('PART D: Histogram Undirected Kangaroo Circuits')
    plt.xlabel(xLabel)
    plt.hist(KangarooC_Lengths, bins = 'auto')
    #plt.show()


    # Part E Check if Eulerian, Find a Eulerian Path
    print("\nPART E:")
    print("\nDirected Bison Graph")
    print("Euelerian: ", nx.is_eulerian(BisonGraph))
    print("Has a Eulerian Path: ", nx.has_eulerian_path(BisonGraph))

    print("\nUndirected Kangaroo Graph")
    print("Euelerian: ", nx.is_eulerian(KangarooGraph))
    print("Has a Eulerian Path: ", nx.has_eulerian_path(KangarooGraph))

    # Part F: Convert to Matrix.
    #I don't know if this covers everything?
    BisonMatrix = nx.to_numpy_matrix(BisonGraph)
    plt.matshow(BisonMatrix)
    #plt.show()

    KangarooMatrix = nx.to_numpy_matrix(KangarooGraph)
    plt.matshow(KangarooMatrix)
    #plt.show()

    # Part G: Copy Largest CC comparing it to a copy and a slightly differnt CC
    print("\nPart G:\n")
    BisonN1 = nx.Graph()
    LargestCCBison = list(max(nx.weakly_connected_components(BisonGraph), key=len))
    for i in LargestCCBison:
        BisonN1.add_edge(i,i+1)
    BisonN2 = BisonN1.copy()

    print("Is BisonN1 Equivalent to BisonN2?")
    Compare(BisonN1,BisonN2)

    print("\nIs BisonN1 Equivalent to N3?")
    BisonN3 = BisonN2.copy()
    Add10Edges(BisonN3,len(BisonN3))
    Compare(BisonN1,BisonN3)

    KangarooN1 = nx.Graph()
    LargestCCKangaroo = list(max(nx.connected_components(KangarooGraph), key=len))
    for i in LargestCCKangaroo:
        KangarooN1.add_edge(i,i+1)
    KangarooN2 = KangarooN1.copy()

    print("\nIs KangarooN1 Equivalent to KangarooN2?")
    Compare(KangarooN1,KangarooN2)

    print("\nIs KangarooN1 Equivalent to N3?")
    KangarooN3 = KangarooN2.copy()
    Add10Edges(KangarooN3,len(KangarooN3))
    Compare(KangarooN1,KangarooN3)

    #Part H: Generate Minimum Spanning Tree
    print("\nPart H:\n")

    Kangaroo_MinTree = nx.minimum_spanning_tree(KangarooGraph)
    print("~A Minimum Spanning Tree was created for the Undirected Kangaroo Graph~")
    TreeOrForest(Kangaroo_MinTree)
    x = 0
    y = 0
    while(not(Kangaroo_MinTree.has_edge(x,y))):
        x = random.randrange(1,17,1)
        y = random.randrange(1,17,1)
        while x == y:
            x = random.randrange(1,17,1)

    print("\nAn edge from the spanning tree was removed")
    Kangaroo_MinTree.remove_edge(x,y)
    TreeOrForest(Kangaroo_MinTree)

    #Part I: Dijkstra's Algorithm

    BisonPairs = list(nx.all_pairs_node_connectivity(BisonGraph))
    ConnectedNodes = []
    for i in BisonPairs:
        for j in BisonPairs:
            if BisonGraph.has_edge(i,j+1):
                ConnectedNodes.append([i,j+1])

    # I don't understand why its registering the input of the append as a list? the dj path length function returns a number.
    # dijkstra_Paths = []
    # for i in ConnectedNodes:
    #     for j in range(1,2):
    #         dijkstra_Paths.append(int(nx.dijkstra_path_length(BisonGraph,ConnectedNodes[i][j],ConnectedNodes[i][j+1])))
    #
    # xLabel = Stats(dijkstra_Paths)
    #
    # plt.figure()
    # plt.xlabel(xLabel)
    # plt.title('Directed Bison Dijkstra Path Lengths')
    # plt.hist(dijkstra_Paths)
    # plt.show()
    #
    # I am very sorry I don't really know how to do the matrix part

    # For showing the matrix as an image use plt.matshow( NAME OF MATRIX )

    # Repeat for Kangaroo Undirected









main()





