import networkx as nx
import matplotlib.pyplot as plt
import dijkstra

start=int(input('введите стартовую точку: '))

n=float('inf')
#граф улиц
streets = [ 
    [n, 1, 1, 0.8, 0.5, n, n, n, n, n, n, n],
    [1, n, n, n, n, 1, n, n, n, n, n,],
    [1, n, n, n, n, 0.3, 0.6, n, n, n, n],
    [0.8, n, n, n, n, n, 0.7, 0.8, n, 0.5, n],
    [0.5, n, n, n, n, n, n, 0.6, n, n, n,],
    [n, 1, 0.3, n, n, n, n, n, n, n, n],
    [n, n, 0.6, 0.7, n, n, n, n, n, n, 0.8],
    [n, n, n, 0.8, 0.6, n, n, n, 0.5, n, n],
    [n, n, n, n, n, n, n, 0.5, n, 0.7, n],
    [n, n, n, 0.5, n, n, n, n, 0.7, n, 0.4],
    [n, n, n, n, n, n, 0.8, n, n, 0.4, n]
    ]

min_len,graph=dijkstra.result(streets,start)

print('минимальный маршрут от стартовой до любой другой: ', min_len)

G = nx.Graph()

#добавление вершин на граф. а - первая координата, б - вторая, wght - вес, взятый из улиц
for i in range(len(graph)):
    a=graph[i][0]
    b=graph[i][1]
    wght=streets[a][b]
    
    if wght != float('inf'):
        G.add_edge(str(a), str(b), weight=wght)

#тут рисуется граф
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()