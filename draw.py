import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
df=pd.read_excel(r'E:\competitions\Statistical modeling\data\second\similarity_matrix222.xlsx')
similr_matrix=df.values
G=nx.Graph()
for i in range(similr_matrix.shape[0]):
    for j in range(i,similr_matrix.shape[1]):
        if i != j and similr_matrix[i,j] > 0.5:
            G.add_edge(i,j,weight=similr_matrix[i,j])
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=False,node_color='skyblue',edge_color='lightblue')
plt.show()