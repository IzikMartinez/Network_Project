import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


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
    plt.show()

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
    print("Bison Directed Graph Connected Component Analysis",
          "\nWeakly connected: ", nx.is_weakly_connected(BisonGraph),
          "\nNumber of Weakly CCs: ", nx.number_weakly_connected_components(BisonGraph),
          "\nSize of largest CC: ", len(max(nx.weakly_connected_components(BisonGraph), key=len)),
          "\nSize of smallest CC: ", len(min(nx.weakly_connected_components(BisonGraph), key=len)))

    print("\nKangaroo Undirected Graph Connected Component Analysis",
          "\nConnected: ", nx.is_connected(KangarooGraph),
          "\nNumber of CCs: ", nx.number_connected_components(KangarooGraph),
          "\nSize of largest CC: ", len(max(nx.connected_components(KangarooGraph), key=len)),
          "\nSize of smallest CC: ", len(min(nx.connected_components(KangarooGraph), key=len)))

    # Part B Computing Degrees and finding the Probability distribution
    BisonDegrees = []
    for node in range(1,26):
        BisonDegrees.append(BisonGraph.degree(node))

    plt.figure()
    plt.title('Histogram Directed Bison')
    plt.hist(BisonDegrees,bins = 17)


    KangarooDegrees = []
    for node in range(1,17):
        KangarooDegrees.append(KangarooGraph.degree(node))

    plt.figure()
    plt.title('Histogram Undirected Kangaroo')
    plt.hist(KangarooDegrees,bins = 9)
    plt.show()

main()





