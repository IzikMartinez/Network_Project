import networkx as nx
import pandas as pd

JazzTSV = 'arenas-jazz/out.arenas-jazz'
Jazz_Read = pd.read_csv(JazzTSV, sep='\t')

print(Jazz_Read.head(10))

# I found a way to read the TSV file but so far I don't know how to use it correctly so I
# could have read it incorrectly. If you look at the TSV file for Jazz musicians it has 2 columns
# I assumed them to be which nodes are connected but I also looked at the Dutch college file
# and its completely different ruining all my theories.


