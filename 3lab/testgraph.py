import networkx as nx
import matplotlib.pyplot as plt
import dijkstra

start=int(input('введите стартовую точку: '))

n=float('inf')
# сюда нужно будет подать все улицы
streets = [
        [n, 10, 18, 8, n, n],
        [10, n, 16, 9, 21, n],
        [n, 16, n, n, 15, n],
        [7, 9, n, n, n, 12],
        [n, n, n, n, n, 23],
        [n, n, 15, n, 23, n]
    ]

min_len,graph=dijkstra.result(streets,start)

print('минимальный маршрут от стартовой до любой другой: ', min_len)

G = nx.Graph()
#объявление имен вершин
nodes = ["0", "1", "2", "3", "4", "5"]
G.add_nodes_from(nodes)
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