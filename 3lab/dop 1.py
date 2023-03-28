import numpy as np
import heapq


def get_neighbors(x, y, z, X, Y, Z):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y, z))
    if y > 0:
        neighbors.append((x, y - 1, z))
    if z > 0:
        neighbors.append((x, y, z - 1))
    if x < X - 1:
        neighbors.append((x + 1, y, z))
    if y < Y - 1:
        neighbors.append((x, y + 1, z))
    if z < Z - 1:
        neighbors.append((x, y, z + 1))
    return neighbors


def greedy_shortest_path(array, X, Y, Z):
    visited = set()
    heap = [(0, (0, 0, 0), [])]

    while heap:
        curr_dist, curr_node, curr_path = heapq.heappop(heap)
        x, y, z = curr_node
        if curr_node == (X - 1, Y - 1, Z - 1):
            return curr_path + [curr_node]

        if curr_node not in visited:
            visited.add(curr_node)
            neighbors = get_neighbors(x, y, z, X, Y, Z)
            for neighbor in neighbors:
                if neighbor not in visited:
                    dist = array[neighbor]
                    heapq.heappush(heap, (dist, neighbor, curr_path + [curr_node]))

    return []


if __name__ == "__main__":
    X, Y, Z = 3, 3, 3
    array = np.random.randint(1, 11, (X, Y, Z))
    print(array)
    shortest_path = greedy_shortest_path(array, X, Y, Z)
    print("Shortest path:", shortest_path)

