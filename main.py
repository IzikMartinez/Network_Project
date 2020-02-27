import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random


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
    #lt.show()

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

    # Creating a Histogram to plot the data of the degrees Bison Network
    plt.figure(3)
    plt.title('Part B: Histogram Directed Bison')
    plt.hist(BisonDegrees,bins = 17)

    # Creation of an arrayList to store the degree for each node of Kangaroo Network
    KangarooDegrees = []
    for node in range(1,17):
        KangarooDegrees.append(KangarooGraph.degree(node))

    # Creating a Histogram to plot the data of the degrees for Kangaroo Network
    plt.figure(4)
    plt.title('Part B: Histogram Undirected Kangaroo')
    plt.hist(KangarooDegrees,bins = 9)
    #lt.show()

    #Part C Find the Path between 2 abritrary vertices in the largest CC
    Node1 = random.randrange(1,27,1)
    Node2 = random.randrange(1,27,1)
    while Node1 == Node2:
        Node1 = random.randrange(1,27,1)

    # I put a cutoff on the list of simple paths for now so I can atleast run something
    # cut off is the act of only focusing on the paths <= 5
    BisonPaths = list(nx.all_simple_paths(BisonGraph,Node1,Node2,cutoff = 5))
    BisonLens = []

    for node in range(0,len(BisonPaths)-1):
        BisonLens.append(len(BisonPaths[node]))

    plt.figure(5)
    plt.title('Part C: Histogram Directed Bison Paths')
    plt.hist(BisonLens, bins = 5)
    #lt.show()

    Node1 = random.randrange(1,17,1)
    Node2 = random.randrange(1,17,1)
    while Node1 == Node2:
        Node1 = random.randrange(1,17,1)

    KangarooPaths = list(nx.all_simple_paths(KangarooGraph,Node1,Node2,cutoff = 5))
    KangarooLens = []

    for node in range(0,len(KangarooPaths)-1):
        KangarooLens.append(len(KangarooPaths[node]))

    plt.figure(6)
    plt.title('Part C: Histogram Undirected Kangaroo Paths')
    plt.hist(KangarooLens, bins = 5)

    plt.show()

    # Part D Find the Simple Circuits between 2 abritrary vertices in the largest CC
    # This will Tell us how many simple circuits are in the Bison Network I can't do a cut of on this but
    # I am very confident it work.
    #print(len(list(nx.simple_cycles(BisonGraph))))

    # SKIPPING PART D FOR NOW

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
    # Part G:



main()





