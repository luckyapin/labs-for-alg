import networkx as nx
import matplotlib.pyplot as plt
from main3 import streets


G = nx.Graph()

for i in range(len(streets)):
    for j in range(len(streets)):
        if streets[i][j] != float('inf'):
            G.add_edge(str(i), str(j), weight=streets[i][j])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
