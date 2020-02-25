import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# Create Network: This function is to create a network based on the provided information
# in the Kangaroo and Bison Network files.
# Parameters: The Imported, created Graph and The Lines from that Graph
def CreateNetwork (Graph,File):
    Opened_File = open(File, 'r')
    Lines = Opened_File.readlines()

    for ln in Lines[2:-1]:
        Start_node = int(ln.split(' ')[0])
        End_node = int(ln.split(' ')[1])
        Edge_length = float(ln.split(' ')[2])
        Graph.add_edge(Start_node, End_node, weight=Edge_length)

    pos = nx.spring_layout(Graph)
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

    BisonNetwork = CreateNetwork(BisonGraph,BisonFile)

    #Undirected Kangaroo Network
    KangarooFile = 'moreno_kangaroo/out.moreno_kangaroo_kangaroo'
    KangarooGraph = nx.Graph()

    KangaroonNetwork = CreateNetwork(KangarooGraph,KangarooFile)

main()






